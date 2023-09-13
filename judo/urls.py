from django.urls import path
from judo import views  # Replace 'gujc_project' and 'judo' with your actual project and app names

app_name = 'judo'  # Replace 'judo' with your app name
urlpatterns = [
    # Your existing URLs
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('merch/', views.merch, name='merch'),
    path('contact/', views.contact, name='contact'),
    path('staff/dashboard/', views.dashboard, name='dashboard'),
    path('staff/merch/', views.staff_merch, name='staff_merch'),
    path('staff/faq/', views.staff_faq, name='staff_faq'),
    path('staff/faq/edit_faq/<int:faq_id>/', views.edit_faq, name='edit_faq'),
    path('staff/faq/delete_faq/<int:faq_id>/', views.delete_faq, name='delete_faq'),

    
    
]
# Staff URLs
'''
path('staff/dashboard/', views.staff_dashboard, name='dashboard'),
path('staff/merch/', views.staff_merch, name='staff_merch'),
path('staff/faq/', views.staff_faq, name='staff_faq'),
path('staff/login/', views.staff_login, name='staff_login'),
'''