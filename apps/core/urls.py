from django.urls import path
from .views import Home, About, Skill, Experience
from . import views

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about', About.as_view(), name='about'),
    path('contact', views.contact, name='contact'),    
    path('experience', views.experience, name='experience'),    
    path('skills', views.skill, name='skills'),
    path('testimonials', views.testimonials, name='testimonials'),
    path('projects', views.projects, name='projects'),
]
