from django.urls import path
from judo import views  # Replace 'gujc_project' and 'judo' with your actual project and app names

app_name = 'judo'  # Replace 'judo' with your app name
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('merch/', views.merch, name='merch'),
    path('contact/', views.contact, name='contact'),
   
]
