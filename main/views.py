from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Report, DataUtility
from App.models import Process, SubProcess  # Add this import
from django.contrib.auth.models import AnonymousUser
from .models import Production,Quality_tracker,DataExtraction
from django.core.serializers import serialize
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.http import HttpResponse
from .forms import ProductionForm,QualityForm,RandomizerForm
from pytz import timezone
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q,Sum,F, ExpressionWrapper, fields
from django.db.models.functions import Cast
from datetime import timedelta
from django.contrib.auth.models import User
from django.db.models import Value as V, CharField, F, Count,Value
from django.db.models.functions import Concat
from django.db.models import Count, Q
import datetime
from datetime import datetime
import json
from random import sample
import random
import math
from django.core.exceptions import ValidationError
from django.contrib import messages
import calendar
from django.db.models.functions import TruncMonth
from collections import OrderedDict

def home(request):
    username=None
    if request.user.is_authenticated:
       username = request.user.username
    return render(request, 'main/index.html')

@login_required
def production_tracker(request):
    if request.method == 'POST':
        form = ProductionForm(request.POST)
        if form.is_valid():
            latest_entry = Production.objects.last()
            # Retrieve the start_time from the form data
            start_time = form.cleaned_data['start_time']
            form.instance.end_time = timezone.now()

            # Save the form
            form.save()

            # Explicitly set the timezone to Indian Standard Time

            # Save the form data to the database

            return redirect('home')
    else:
        form = ProductionForm()

    user = request.user
    context = {
        'user': user,
        'analyst_name': user.analyst_name,
        'process': user.process,
        'sub_process': user.sub_process,
        'form': form,
    }

    return render(request, 'main/production_tracker.html', context)

# Quality tracker  code save the data for database quality_tracker 
@login_required
def quality_tracker(request, id):
    production = Production.objects.get(id=id)
    form = None
    if request.method == 'POST':
        
        # Check if the production_id exists in the QualityTracker table with qc_status as None
        quality_tracker_exists = Quality_tracker.objects.filter(Production__qc_status='Pending', Production_id=id).first()
        if quality_tracker_exists:
            # If the quality tracker object exists, update the qc_status to 'complete'
            production.qc_status = 'Complete'
            production.save()

        form_data = request.POST
        qstart_time = form_data.get('qstart_time')
        qend_time = datetime.now()
        # Calculate duration
        qstart_time = datetime.fromisoformat(qstart_time)  # Parsing isoformat datetime
        duration = qend_time - qstart_time

        # Calculate duration in hours, minutes, and seconds
        total_seconds = duration.total_seconds()
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)


        # Format duration as HH:MM:SS
        qduration = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

        quality_tracker = Quality_tracker.objects.create(
            Production=production,
            qstart_time = qstart_time,
            q1_result=form_data.get('q1_result'),
            q1_comment=form_data.get('q1_comment'),
            q2_result=form_data.get('q2_result'),
            q2_comment=form_data.get('q2_comment'),
            q3_result=form_data.get('q3_result'),
            q3_comment=form_data.get('q3_comment'),
            q4_result=form_data.get('q4_result'),
            q4_comment=form_data.get('q4_comment'),
            q5_result=form_data.get('q5_result'),
            q5_comment=form_data.get('q5_comment'),
            q6_result=form_data.get('q6_result'),
            q6_comment=form_data.get('q6_comment'),
            q7_result=form_data.get('q7_result'),
            q7_comment=form_data.get('q7_comment'),
            q8_result=form_data.get('q8_result'),
            q8_comment=form_data.get('q8_comment'),
            q9_result=form_data.get('q9_result'),
            q9_comment=form_data.get('q9_comment'),
            q10_result=form_data.get('q10_result'),
            q10_comment=form_data.get('q10_comment'),
            auditor_name = request.user.get_username(),
            transaction_number=form_data.get('transaction_number'),
            qnotes=form_data.get('qnotes'),
            qdate_received=form_data.get('date_received'),
            qdate_reviewed=form_data.get('date_reviewed'),
            qduration=qduration,
            # Set other fields here
        )
        qend_time = datetime.now()
        quality_tracker.qend_time = qend_time
        
        # Calculate duration
        # duration = qend_time - datetime.strptime(qstart_time, '%Y-%m-%d %H:%M:%S')
        # quality_tracker.qduration = duration.total_seconds() / 60  # Duration in minutes


        # Initialize the number of passed checks

        num_passed = 0
        # Iterate through q1 to q10
        
        for q in [quality_tracker.q1_result, quality_tracker.q2_result, quality_tracker.q3_result, quality_tracker.q4_result, quality_tracker.q5_result,
            quality_tracker.q6_result, quality_tracker.q7_result, quality_tracker.q8_result, quality_tracker.q9_result, quality_tracker.q10_result]:
            # Check if the value is equal to 'Pass'
            if q == 'Pass':
                num_passed += 1
            elif q== 'NA':
                num_passed += 1
        # Calculate the total score
        final_score = min(100, num_passed * 10)


        # If we increase the fatal question, it is important to include it here; otherwise, the fatal question would fail and the final score will not display zero.
        # Check if any fatal question is marked as fail
        if any(q in ['Fail'] for q in [quality_tracker.q1_result,quality_tracker.q3_result, quality_tracker.q5_result,
            quality_tracker.q7_result,quality_tracker.q9_result]):
            final_score = 0
        quality_tracker.final_score = final_score
        # Save the Quality Tracker entry
        quality_tracker.save()
        return redirect('quality_tracker', id=production.id)
    else:
        # Create a new QualityForm instance with the production instance as the instance
        form = QualityForm(instance=production)
        form.fields['qstart_time'].initial = timezone.now()
        

    # Render the quality_tracker template with the production and form instances
    return render(request, 'main/quality_tracker.html', {'production': production, 'form': form,'auditor_name': request.user.get_username()})

#here is Randomizer code find the data through the percentage and select the field 
@login_required
def randomizer(request):
    quality = Quality_tracker.objects.all()
    form = RandomizerForm()
    default_start_date = timezone.now().date()
    context = {'form': form, 'default_start_date': default_start_date,'quality':quality}
 
    if request.method == 'POST':
        form = RandomizerForm(request.POST)
        if form.is_valid():
            date_received = form.cleaned_data['date_received']
            date_reviewed = form.cleaned_data['date_reviewed']
            percentage = form.cleaned_data['percentage']
            select_field = form.cleaned_data['select_field']
           
            if select_field == 'analyst_name':
 
                # Round the percentage value to the nearest integer if it's a float
                percentage = math.ceil(percentage)
 
                # Filter the production data based on the date range
                production_data = Production.objects.filter(date_received__range=[date_received, date_reviewed])
 
                # Concatenate the analyst_name, transaction_number, process,sub_process,status fields
                production_data = production_data.annotate(combined_name_number=Concat('analyst_name', Value('-'), 'transaction_number', Value('-'), 'process',Value('-'),'sub_process',Value('-'),'status',output_field=CharField()))
 
                # Group the production data by analyst_name
                grouped_data = production_data.values('analyst_name').annotate(total=Count('id'))
                random.seed(42)
                # Calculate the number of items to select per analyst based on the percentage
                analyst_data = []
                for group in grouped_data:
                    num_items_to_select = math.ceil(group['total'] * (percentage / 100))
                    analyst_subset = production_data.filter(analyst_name=group['analyst_name'])
                    analyst_subset = random.sample(list(analyst_subset), min(num_items_to_select, len(analyst_subset)))
                    analyst_data.extend(analyst_subset)
 
                context.update({'random_data': analyst_data})
 
            elif select_field =='process':
                # Round the percentage value to the nearest integer if it's a float
                percentage = math.ceil(percentage)
 
                # Filter the production data based on the date range
                production_data = Production.objects.filter(date_received__range=[date_received, date_reviewed])
 
                # Concatenate the analyst_name, transaction_number, process fields
                production_data = production_data.annotate(combined_name_number=Concat('analyst_name', Value('-'), 'transaction_number', Value('-'), 'process',output_field=CharField()))
 
                # Group the production data by process
                grouped_data = production_data.values('process').annotate(total=Count('id'))
                random.seed(42)
                # Calculate the number of items to select per process based on the percentage
                process_data = []
                for group in grouped_data:
                    num_items_to_select = math.ceil(group['total'] * (percentage / 100))
                    process_subset = production_data.filter(process=group['process'])
                    process_subset = random.sample(list(process_subset), min(num_items_to_select, len(process_subset)))
                    process_data.extend(process_subset)
 
                context.update({'random_data': process_data})
 
            elif select_field =='sub_process':
                # Round the percentage value to the nearest integer if it's a float
                percentage = math.ceil(percentage)
 
                # Filter the production data based on the date range
                production_data = Production.objects.filter(date_received__range=[date_received, date_reviewed])
 
                # Concatenate the analyst_name, transaction_number, sub_process fields
                production_data = production_data.annotate(combined_name_number=Concat('analyst_name', Value('-'), 'transaction_number', Value('-'),'sub_process',output_field=CharField()))
 
                # Group the production data by sub_process
                grouped_data = production_data.values('sub_process').annotate(total=Count('id'))
                random.seed(42)
                # Calculate the number of items to select per sub_process based on the percentage
                sub_process_data = []
                for group in grouped_data:
                    num_items_to_select = math.ceil(group['total'] * (percentage / 100))
                    sub_process_subset = production_data.filter(sub_process=group['sub_process'])
                    sub_process_subset = random.sample(list(sub_process_subset), min(num_items_to_select, len(sub_process_subset)))
                    sub_process_data.extend(sub_process_subset)
 
                context.update({'random_data': sub_process_data})
 
            elif select_field =='status':
                # Round the percentage value to the nearest integer if it's a float
                percentage = math.ceil(percentage)
 
                # Filter the production data based on the date range
                production_data = Production.objects.filter(date_received__range=[date_received, date_reviewed])
 
                # Concatenate the analyst_name, transaction_number, status fields
                production_data = production_data.annotate(combined_name_number=Concat('analyst_name', Value('-'), 'transaction_number', Value('-'),'status',output_field=CharField()))
 
                # Group the production data by status
                grouped_data = production_data.values('status').annotate(total=Count('id'))
                random.seed(42)
                # Calculate the number of items to select per status based on the percentage
                status_data = []
                for group in grouped_data:
                    num_items_to_select = math.ceil(group['total'] * (percentage / 100))
                    status_subset = production_data.filter(status=group['status'])
                    status_subset = random.sample(list(status_subset), min(num_items_to_select, len(status_subset)))
                    status_data.extend(status_subset)
 
                context.update({'random_data': status_data})
            else:
                return render(request, 'main/randomizer.html', context)              
 
    return render(request, 'main/randomizer.html', context)


# here is click hyper link and then open page  (display_production_data)
@login_required
def display_production_data(request,id):
      analyst_name = Production.objects.get(id=id)
      analyst_name.date_received = analyst_name.date_received.strftime('%Y-%m-%d')
      analyst_name.date_reviewed = analyst_name.date_reviewed.strftime('%Y-%m-%d') if analyst_name.date_reviewed else ''
    
      if request.method == 'POST':
        form = ProductionForm(request.POST, instance=analyst_name)
        if form.is_valid():
            start_time = form.cleaned_data['start_time']
            form.instance.end_time = timezone.now()
            form.save()  # Save the form data to the database
           
            #return redirect(' ')

        else:
          form = ProductionForm(instance=analyst_name)
          form = ProductionForm(instance=analyst_name.date_received)
           
      return render(request,'main/display_production_data.html',{'analyst_name':analyst_name})  



@login_required
def query_tracker(request):
    
    return render(request,'main/query_tracker.html')

def reports(request):
    reports = Report.objects.all()
    return render(request, 'reports.html', {'reports': reports})

def data_utilities(request):
    data_utilities = DataUtility.objects.all()
    return render(request, 'data_utilities.html', {'data_utilities': data_utilities})




#here is production data display code = (display data) for Production Details view

@login_required
def display_data(request,analyst_name):
    user_data = Production.objects.filter(analyst_name=request.user.analyst_name)  #.order_by('-date_received')

    # Handle date range filtering
    date_received = request.GET.get('date_received')
    date_reviewed = request.GET.get('date_reviewed')

    if date_received and date_reviewed:
        user_data = user_data.filter(date_reviewed__range=[date_received, date_reviewed])

    # Set default start and end dates
    if not date_received:
        if user_data:
            default_start_date = min(user_data, key=lambda x: x.date_received).date_received
        else:
            default_start_date = datetime.now().date()
    else:
        default_start_date = datetime.strptime(date_received, '%Y-%m-%d').date()

    if not date_reviewed:
        if user_data:
            default_end_date = max(user_data, key=lambda x: x.date_reviewed).date_reviewed
        else:
            default_end_date = datetime.now().date()
    else:
        default_end_date = datetime.strptime(date_reviewed, '%Y-%m-%d').date()

    # Convert the queryset to JSON for simplicity. Adjust based on your needs.
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        table_html = render_to_string('main/table_content.html', {'user_data': user_data})
        return JsonResponse({'table_html': table_html}, safe=False)

    return render(request, 'main/display_data.html', {
        'user_data': user_data,
        'default_start_date': default_start_date,
        'default_end_date': default_end_date
    })


@login_required
def display_query_data(request):
    
    return render(request, 'main/display_query_data.html')

# here us Display Quality Tracker code 
@login_required
def display_quality_tracker(request):
    auditors = Quality_tracker.objects.order_by('auditor_name').values_list('auditor_name', flat=True).distinct()
    userdata=None
    if request.method == 'POST':
        # Handle date range filtering
        auditor_name = request.POST.get('auditor_name', '')
        qdate_received = request.POST.get('qdate_received', '')
        qdate_reviewed = request.POST.get('qdate_reviewed', '')
        
 
        # Convert date strings to datetime objects
        qdate_received_date = datetime.strptime(qdate_received, '%Y-%m-%d') if qdate_received else None
        qdate_reviewed_date = datetime.strptime(qdate_reviewed, '%Y-%m-%d') if qdate_reviewed else None

        # show all button 
 
        if auditor_name and qdate_received_date and qdate_reviewed_date:
            if auditor_name == 'all':
                userdata = Quality_tracker.objects.filter(qdate_reviewed__range=[qdate_received_date, qdate_reviewed_date])
           
            elif auditor_name and qdate_received_date and qdate_reviewed_date:
                userdata = Quality_tracker.objects.filter(auditor_name=auditor_name, qdate_reviewed__range=[qdate_received_date, qdate_reviewed_date])
           
        else:
            userdata = []
 
        # Initialize auditors variable after handling filters
       
        return render(request, 'main/display_quality_tracker.html', {'auditors': auditors,'userdata':userdata})
    else:
        return render(request, 'main/display_quality_tracker.html', {'auditors':auditors})


 #This is the code for data extraction. Combine the data from Production and Quality into a single list and present both. 
@login_required
def data_extraction(request):
    context = {}
    if request.method == 'POST':
        date_received = request.POST['date_received']
        date_reviewed = request.POST['date_reviewed']
        process = request.POST['process']
        sub_process = request.POST['sub_process']
        analyst_name = request.POST['analyst_name']
        

        # Query the Production model based on user input
        productions = Production.objects.filter(
        date_received__range=[date_received, date_reviewed],
        process=process,
        sub_process=sub_process
)    

        if analyst_name != 'all':
            productions = productions.filter(analyst_name=analyst_name)

        # Query the Quality_tracker model based on the Production objects
        quality_trackers = Quality_tracker.objects.filter(Production__in=productions)
         
        # Combine the Production and Quality_tracker data into a single list of dictionaries
        data = []
        for production in productions:
            quality_tracker = quality_trackers.filter(Production=production).first()
            data.append({
                'analyst_name': production.analyst_name,
                'date_received': production.date_received,
                'date_reviewed': production.date_reviewed,
                'transaction_number': production.transaction_number,
                'process': production.process,
                'sub_process': production.sub_process,
                'tat': production.tat,
                'status': production.status,
                'query': production.query,
                'notes': production.notes,
                'auditor_name': quality_tracker.auditor_name if quality_tracker else None,
                'qc_status':production.qc_status if production else None,
                'qstart_time': quality_tracker.qstart_time if quality_tracker else None,
                'qend_time': quality_tracker.qend_time if quality_tracker else None,
                'qduration':quality_tracker.qduration if quality_tracker else None,
                'q1_result': quality_tracker.q1_result if quality_tracker else None,
                'q1_comment': quality_tracker.q1_comment if quality_tracker else None,
                'q2_result':quality_tracker.q2_result if quality_tracker else None,
                'q2_comment': quality_tracker.q2_comment if quality_tracker else None,
                'q3_result':quality_tracker.q3_result if quality_tracker else None,
                'q3_comment': quality_tracker.q3_comment if quality_tracker else None,
                'q4_result':quality_tracker.q4_result if quality_tracker else None,
                'q4_comment': quality_tracker.q4_comment if quality_tracker else None,
                'q5_result':quality_tracker.q5_result if quality_tracker else None,
                'q5_comment': quality_tracker.q5_comment if quality_tracker else None,
                'q6_result':quality_tracker.q6_result if quality_tracker else None,
                'q6_comment': quality_tracker.q6_comment if quality_tracker else None,
                'q7_result':quality_tracker.q7_result if quality_tracker else None,
                'q7_comment': quality_tracker.q7_comment if quality_tracker else None,
                'q8_result':quality_tracker.q8_result if quality_tracker else None,
                'q8_comment': quality_tracker.q8_comment if quality_tracker else None,
                'q9_result':quality_tracker.q9_result if quality_tracker else None,
                'q9_comment': quality_tracker.q9_comment if quality_tracker else None,
                'q10_result':quality_tracker.q10_result if quality_tracker else None,
                'q10_comment': quality_tracker.q10_comment if quality_tracker else None,
                'qnotes': quality_tracker.qnotes if quality_tracker else None,
                'final_score': quality_tracker.final_score if quality_tracker else None,
                # Add more fields as needed
            })
        context = {'data': data}
    else:
        if 'analyst_name' not in request.session:
            request.session['analyst_name'] = list(Production.objects.order_by('analyst_name').values_list('analyst_name', flat=True).distinct())
        if 'process' not in request.session:
            request.session['process'] = list(Production.objects.order_by('process').values_list('process', flat=True).distinct())
        if 'sub_process' not in request.session:
            request.session['sub_process'] = list(Production.objects.order_by('sub_process').values_list('sub_process', flat=True).distinct())

        context['analyst_name'] = request.session['analyst_name']
        context['process'] = request.session['process']
        context['sub_process'] = request.session['sub_process']

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if 'process' in request.POST:
            process_id = request.POST.get('process')
            # Retrieve subprocesses based on the selected process
            sub_process_values = Production.objects.filter(process=process_id).values_list('sub_process', flat=True).distinct()
            sub_process_json = [{"id": sub_process_id, "name": sub_process_name} for sub_process_id, sub_process_name in sub_process_values.items()]
            return JsonResponse(sub_process_json, safe=False)
        elif 'sub_process' in request.POST:
            sub_process = request.POST.get('sub_process')
            # Retrieve ProductionTracker objects based on the selected subprocess
            production_tracker = Production.objects.filter(production__sub_process=sub_process)
            # Extract analysts from ProductionTracker objects
            analysts = production_tracker.values_list('analyst_name', flat=True).distinct()
            return JsonResponse(list(analysts), safe=False)

    return render(request, 'main/data_extraction.html', context)

def get_analyst_name(request):
    sub_process = request.GET.get('sub_process')
    analyst_name = Production.objects.filter(sub_process=sub_process).values_list('analyst_name', flat=True).distinct()
    return JsonResponse(list(analyst_name), safe=False)

def get_sub_process(request):
    process  = request.GET.get('process')
    sub_process = Production.objects.filter(process=process).values_list('sub_process', flat=True).distinct()
    return JsonResponse(list(sub_process), safe=False)



@login_required
def dashboard(request):
    if request.method == 'POST':
        date_received = request.POST.get('date_received')
        date_reviewed = request.POST.get('date_reviewed')
 
        date_received_datetime = datetime.strptime(date_received, '%Y-%m-%d')
        date_reviewed_datetime = datetime.strptime(date_reviewed, '%Y-%m-%d')
 
        production_by_month = Production.objects.filter(qc_status='Complete')
        data = []
        labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        month_numbers = range(1, 13)
        for month_number in month_numbers:
            total_qc = production_by_month.filter(date_received__month=month_number).count()
            data.append(total_qc)
 
        production = Production.objects.filter(date_received__range=[date_received_datetime, date_reviewed_datetime])
        total_production = production.count()
 
        quality_error = Quality_tracker.objects.filter(qdate_received__range=[date_received_datetime, date_reviewed_datetime])
        total_error = quality_error.filter(final_score=0).count()
 
        total_qc = production.filter(qc_status='Complete').count()
        if total_production != 0:
            qc_score_str = f"{round((total_qc/total_production)*100, 1):.0f}%"
        else:
            qc_score_str = "N/A"
 
        durations = [sum(int(part) * 60 ** i for i, part in enumerate(reversed(value.duration.split(':'))) if part.isdigit()) if value.duration else 0 for value in production]
        total_seconds = sum(durations)
        total_durations = str(timedelta(seconds=total_seconds))
        total_production_data = []

        # Filter Production objects within the specified date range
        production_queryset = Production.objects.filter(date_received__range=[date_received_datetime, date_reviewed_datetime])

        # Iterate over each production record and collect date_received values
        for production_data in production_queryset:
            formatted_date = production_data.date_received.strftime('%Y, %m, %d')  # Format date as 'YYYY, MM, DD'
            total_production_data.append(formatted_date)

        # Convert month numbers to month names in the format 'MMM'
        converted_dates = [date.replace(date.split(',')[1], convert_month(date.split(',')[1])) for date in total_production_data]
        # Create a dictionary to store the month name and occurrence count
        month_count = {}
        for date in converted_dates:
            month = date.split(',')[1].strip()
            if month in month_count:
                month_count[month] += 1
            else:
                month_count[month] = 1
        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        sorted_month_count = OrderedDict(sorted(month_count.items(), key=lambda x: month_names.index(x[0])))

        # QA score code start here
        # Filter Production objects within the specified data range qc_status ='Complete'
        production_qa_queryset = Production.objects.filter(date_received__range=[date_received_datetime, date_reviewed_datetime], qc_status='Complete')
        total_qa_data = []
        for production_qa in production_qa_queryset:
            qadate_formatted = production_qa.date_received.strftime('%Y, %m, %d')
            total_qa_data.append(qadate_formatted)

        qaconverted_dates = [date.replace(date.split(',')[1], convert_month(date.split(',')[1])) for date in total_qa_data]
        month_count = {}
        for date in qaconverted_dates:
            month = date.split(',')[1].strip()
            if month in month_count:
                month_count[month] += 1
            else:
                month_count[month] = 1

        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        formatted_month_count = OrderedDict(sorted(month_count.items(), key=lambda x: month_names.index(x[0])))

        # print(formatted_month_count)
        # print(sorted_month_count)
        QA_score = dict()
        for key in formatted_month_count.keys() & sorted_month_count.keys():
            percentage = (formatted_month_count[key] / sorted_month_count[key])*100
            percentage_string = "{:.0f}%".format(percentage)  # Format percentage with 0 decimal places and add "%"
            percentage_int = int(percentage_string.replace('%', ''))  # Remove "%" symbol and convert to integer
            QA_score[key] = percentage_int

        # Months formatting for QA_Score
        # month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        # QA_score= OrderedDict(sorted(month_count.items(), key=lambda x: month_names.index(x[0])))
        # print(sorted_month_count)
        # print(list(sorted_month_count.values()))

        quality_error_queryset = Quality_tracker.objects.filter(qdate_received__range=[date_received_datetime, date_reviewed_datetime],final_score = 0)
        total_Error = []
        for production_error in quality_error_queryset:
            error_date_formatted = production_error.qdate_received.strftime('%Y, %m, %d')
            total_Error.append(error_date_formatted)

        error_converted_dates = [date.replace(date.split(',')[1], convert_month(date.split(',')[1])) for date in total_Error]
        month_count = {}
        for date in error_converted_dates:
            month = date.split(',')[1].strip()
            if month in month_count:
                month_count[month] += 1
            else:
                month_count[month] = 1

        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        formatted_error_count = OrderedDict(sorted(month_count.items(), key=lambda x: month_names.index(x[0])))
        # print(formatted_error_count)

        # AHT code start here
        Aht_total_durations = {}
        production_aht = Production.objects.filter(date_received__range=[date_received_datetime, date_reviewed_datetime])

        for value in production_aht:
            aht_duration_seconds = sum(int(part) * 60 ** i for i, part in enumerate(reversed(value.duration.split(':'))) if part.isdigit()) if value.duration else 0
            # Calculate the month for the current value with abbreviated month names
            month_names = value.date_received.strftime('%b')  # Use '%b' for abbreviated month names
            # Update the total duration for the month
            Aht_total_durations[month_names] = Aht_total_durations.get(month_names, 0) + aht_duration_seconds

        for month, total_seconds in Aht_total_durations.items():
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            total_duration_str = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"
            Aht_total_durations[month] = total_duration_str 

 
        context = {
            'total_production': total_production,
            'total_error': total_error,
            'qc_score_str': qc_score_str,
            'total_durations': total_durations,
            'labels': labels,
            'data': data,
            'month_count': json.dumps(sorted_month_count),
            'QA_score': json.dumps(QA_score),
            'formatted_error_count': json.dumps(formatted_error_count),
            'Aht_total_durations': json.dumps(Aht_total_durations)
        }
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            return JsonResponse(context)
        return render(request, 'main/dashboard.html', context)
 
    return render(request, 'main/dashboard.html')


def convert_month(month):
    month = month.strip()  # Remove leading/trailing spaces
    return datetime.strptime(month, "%m").strftime("%b")

def qaconvert_month(month_num):
    month_name = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'Jun', '07': 'Jul', '08': 'Aug', '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
    return month_name[month_num]



#====================================================================================================================#
#just using for test off adding new things and remove old 

def tests(request):
    if request.method == 'POST':
        date_received = request.POST.get('date_received')
        date_reviewed = request.POST.get('date_reviewed')
 
        date_received_datetime = datetime.strptime(date_received, '%Y-%m-%d')
        date_reviewed_datetime = datetime.strptime(date_reviewed, '%Y-%m-%d')
 
        production_by_month = Production.objects.filter(qc_status='Complete')
        data = []
        labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        month_numbers = range(1, 13)
        for month_number in month_numbers:
            total_qc = production_by_month.filter(date_received__month=month_number).count()
            data.append(total_qc)
 
        production = Production.objects.filter(date_received__range=[date_received_datetime, date_reviewed_datetime])
        total_production = production.count()
 
        quality_error = Quality_tracker.objects.filter(qdate_received__range=[date_received_datetime, date_reviewed_datetime])
        total_error = quality_error.filter(final_score=0).count()
 
        total_qc = production.filter(qc_status='Complete').count()
        if total_production != 0:
            qc_score_str = f"{round((total_qc/total_production)*100, 1):.0f}%"
        else:
            qc_score_str = "N/A"
 
        durations = [sum(int(part) * 60 ** i for i, part in enumerate(reversed(value.duration.split(':'))) if part.isdigit()) if value.duration else 0 for value in production]
        total_seconds = sum(durations)
        total_durations = str(timedelta(seconds=total_seconds))
        total_production_data = []

        # Filter Production objects within the specified date range
        production_queryset = Production.objects.filter(date_received__range=[date_received_datetime, date_reviewed_datetime])

        # Iterate over each production record and collect date_received values
        for production_data in production_queryset:
            formatted_date = production_data.date_received.strftime('%Y, %m, %d')  # Format date as 'YYYY, MM, DD'
            total_production_data.append(formatted_date)

        # Convert month numbers to month names in the format 'MMM'
        converted_dates = [date.replace(date.split(',')[1], convert_month(date.split(',')[1])) for date in total_production_data]
        # Create a dictionary to store the month name and occurrence count
        month_count = {}
        for date in converted_dates:
            month = date.split(',')[1].strip()
            if month in month_count:
                month_count[month] += 1
            else:
                month_count[month] = 1
        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        sorted_month_count = OrderedDict(sorted(month_count.items(), key=lambda x: month_names.index(x[0])))

        # QA score code start here
        # Filter Production objects within the specified data range qc_status ='Complete'
        production_qa_queryset = Production.objects.filter(date_received__range=[date_received_datetime, date_reviewed_datetime], qc_status='Complete')
        total_qa_data = []
        for production_qa in production_qa_queryset:
            qadate_formatted = production_qa.date_received.strftime('%Y, %m, %d')
            total_qa_data.append(qadate_formatted)

        qaconverted_dates = [date.replace(date.split(',')[1], convert_month(date.split(',')[1])) for date in total_qa_data]
        month_count = {}
        for date in qaconverted_dates:
            month = date.split(',')[1].strip()
            if month in month_count:
                month_count[month] += 1
            else:
                month_count[month] = 1

        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        formatted_month_count = OrderedDict(sorted(month_count.items(), key=lambda x: month_names.index(x[0])))

        # print(formatted_month_count)
        # print(sorted_month_count)
        QA_score = dict()
        for key in formatted_month_count.keys() & sorted_month_count.keys():
            percentage = (formatted_month_count[key] / sorted_month_count[key])*100
            percentage_string = "{:.0f}%".format(percentage)  # Format percentage with 0 decimal places and add "%"
            percentage_int = int(percentage_string.replace('%', ''))  # Remove "%" symbol and convert to integer
            QA_score[key] = percentage_int


        quality_error_queryset = Quality_tracker.objects.filter(qdate_received__range=[date_received_datetime, date_reviewed_datetime],final_score = 0)
        total_Error = []
        for production_error in quality_error_queryset:
            error_date_formatted = production_error.qdate_received.strftime('%Y, %b, %d')
            total_Error.append(error_date_formatted)

        error_converted_dates = [date for date in total_Error]
        month_count = {}
        for date in error_converted_dates:
            month = date.split(',')[1].strip()
            if month in month_count:
                month_count[month] += 1
            else:
                month_count[month] = 1

        # month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        formatted_error_count = dict(sorted(month_count.items(), key=lambda item: list(month_names).index(item[0])))
        # print(formatted_error_count)

        # AHT code start here
        Aht_total_durations = {}
        production_aht = Production.objects.filter(date_received__range=[date_received_datetime, date_reviewed_datetime])

        for value in production_aht:
            aht_duration_seconds = sum(int(part) * 60 ** i for i, part in enumerate(reversed(value.duration.split(':'))) if part.isdigit()) if value.duration else 0
            # Calculate the month for the current value with abbreviated month names
            month_names = value.date_received.strftime('%b')  # Use '%b' for abbreviated month names
            # Update the total duration for the month
            Aht_total_durations[month_names] = Aht_total_durations.get(month_names, 0) + aht_duration_seconds

        for month, total_seconds in Aht_total_durations.items():
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            total_duration_str = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"
            Aht_total_durations[month] = total_duration_str 

 
        context = {
            'total_production': total_production,
            'total_error': total_error,
            'qc_score_str': qc_score_str,
            'total_durations': total_durations,
            'labels': labels,
            'data': data,
            'month_count': json.dumps(sorted_month_count),
            'QA_score': json.dumps(QA_score),
            'formatted_error_count': json.dumps(formatted_error_count),
            'Aht_total_durations': json.dumps(Aht_total_durations)
        }
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            return JsonResponse(context)
        return render(request, 'main/tests.html', context)
 
    return render(request, 'main/tests.html')


def convert_month(month):
    month = month.strip()  # Remove leading/trailing spaces
    return datetime.strptime(month, "%m").strftime("%b")

def qaconvert_month(month_num):
    month_name = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'Jun', '07': 'Jul', '08': 'Aug', '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
    return month_name[month_num]
