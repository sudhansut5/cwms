# from django.db.models import Q
# from .models import Process, SubProcess, User

# def get_sub_processes(process_id):
#     sub_processes = SubProcess.objects.filter(process_id=process_id)
#     return [{'id': sub_process.id, 'name': sub_process.name} for sub_process in sub_processes]

# def get_analysts(sub_process_id):
#     analysts = User.objects.filter(sub_process_id=sub_process_id)
#     return [{'id': analyst.id, 'username': analyst.username} for analyst in analysts]
