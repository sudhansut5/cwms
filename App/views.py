from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from .forms import CustomUserCreationForm


from .models import Process, SubProcess, PasswordResetToken, CustomUser
from django.core.mail import send_mail
from django.utils import timezone

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('custom_login')
    else:
        form = CustomUserCreationForm()

    processes = Process.objects.all()
    sub_processes = SubProcess.objects.all()

    return render(request, 'App/signup.html', {'form': form, 'processes': processes, 'sub_processes': sub_processes})

    if not user.analyst_email.endswith('@ana.com') or not user.supervisor_email.endswith('@ana.com'):
        error_message = 'Invalid email domain. Please use @ana.com for analyst and supervisor email.'
        messages.error(request, error_message)
        return render(request, 'signup.html')

class PasswordResetRequestView(View):
    def get(self, request):
        return render(request, 'App/password_reset_request.html')

    def post(self, request):
        email = request.POST.get('email')

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            messages.error(request, 'User does not exist.')
            return redirect('password_reset_request')

        # Generate a unique token and save it in the database
        token = PasswordResetToken.objects.create(user=user)
        
        # Send a password reset email with a link containing the token
        reset_link = f"http://yourdomain.com/password-reset/confirm/{token.token}/"
        send_mail('Password Reset', f'Click the following link to reset your password: {reset_link}', 'sudhansut5@gmail.com', [email])

        messages.success(request, 'Password reset email sent.')
        return redirect('custom_login')

class PasswordResetConfirmView(View):
    def get(self, request, token):
        try:
            password_reset_token = PasswordResetToken.objects.get(token=token)
        except PasswordResetToken.DoesNotExist:
            messages.error(request, 'Invalid token.')
            return redirect('custom_login')

        if password_reset_token.is_valid():
            return render(request, 'App/password_reset_confirm.html', {'token': token})
        else:
            messages.error(request, 'Expired token.')
            return redirect('custom_login')

    def post(self, request, token):
        new_password = request.POST.get('new_password')

        try:
            password_reset_token = PasswordResetToken.objects.get(token=token)
        except PasswordResetToken.DoesNotExist:
            messages.error(request, 'Invalid token.')
            return redirect('custom_login')

        if password_reset_token.is_valid():
            # Update the user's password
            user = password_reset_token.user
            user.set_password(new_password)
            user.save()

            # Delete the used token
            password_reset_token.delete()

            messages.success(request, 'Password reset successful.')
            return redirect('custom_login')
        else:
            messages.error(request, 'Expired token.')
            return redirect('custom_login')

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Change 'main:index' to your desired login success URL
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'App/login.html', {'form': form})

@login_required
def custom_logout(request):
    logout(request)
    # Redirect to your desired logout success URL
    return redirect('custom_login')
