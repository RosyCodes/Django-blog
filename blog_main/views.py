# from django.http import HttpResponse
from django.shortcuts import render, redirect
from blogs.models import Category, Blog
from blog_profile.models import About, SocialLink
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth import views as auth_views

# for sent email rendering
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import reverse


class CustomPasswordResetView(auth_views.PasswordResetView):
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    html_email_template_name = 'password_reset_email.html'

    # renders the HTML tags in email sent to pure string
    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        """
        Sends a django.core.mail.EmailMultiAlternatives to `to_email`.
        """
        subject = render_to_string(subject_template_name, context)
        subject = ''.join(subject.splitlines())
        body = render_to_string(email_template_name, context)

        email_message = EmailMultiAlternatives(
            subject, body, from_email, [to_email])
        if html_email_template_name is not None:
            html_email = render_to_string(html_email_template_name, context)
            email_message.attach_alternative(html_email, 'text/html')

        email_message.send()


def home(request):
    featured_posts = Blog.objects.filter(
        is_featured=True, status='Published').order_by('-updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')
    # Fetch about us //  Instead of this, we used a context processor for about us
    # try:
    #     about = About.objects.get()
    # except:
    #     about = None

    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        # 'about': about,
    }
    # return HttpResponse('<h1>HomePage</h1>')
    return render(request, 'home.html', context)


def register(request):
    if request.method == 'POST':
        # pass the form user entry to the form
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # gets the user entry values
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # checks if username/password is found and then login
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('dashboard')

    form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')
