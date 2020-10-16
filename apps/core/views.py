from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import TemplateView, ListView
from .models import User, Web, Skill, Experience, Testimonial, Project

class Home(ListView):    
    model = User
    template_name = 'core/home.html'


class About(ListView):    
    model = User
    template_name = 'core/about.html'


def contact(request):    
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = "De : " +  name + "\nCorreo: " + email + "\nMensaje: " + request.POST['message']
        email_from = settings.EMAIL_HOST_USER
        email_to = settings.EMAIL_HOST_USER
        send_mail('Mensaje desde la aplicación web', message, email_from, [email_to],)
        return render(request, 'core/home.html')
    return render(request, 'core/contact.html')



def experience(request):  
    education = Experience.objects.filter(type_experience='Education')    
    professional = Experience.objects.filter(type_experience='Professional Experience')  
    context = {
        'education' : education,
        'professional': professional
    }
    print(education)
    return render(request, 'core/experience.html', context)



def skill(request):
    list1 = Skill.objects.filter(pk__lt=6)
    list2 =  Skill.objects.filter(pk__gt=5)
    context = {
        'list1': list1,
        'list2': list2,
    }
    return render(request, 'core/skills.html', context)



def testimonials(request):  
    testimonials = Testimonial.objects.all()
    context = {'testimonials' : testimonials}  
    return render(request, 'core/testimonials.html', context)



def projects(request):    
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'core/projects.html', context)