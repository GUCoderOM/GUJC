from django.urls import path
from judo import views  # Replace 'gujc_project' and 'judo' with your actual project and app names

from judo.views import (
    CreateCheckoutSessionView,
    SuccessView,
    CancelView,
)

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
    path('staff/merch/edit_item/<int:item_id>/', views.edit_item, name='edit_item'),
    path('staff/merch/delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
    path('staff/faq/', views.staff_faq, name='staff_faq'),
    path('staff/faq/edit_faq/<int:faq_id>/', views.edit_faq, name='edit_faq'),
    path('staff/faq/delete_faq/<int:faq_id>/', views.delete_faq, name='delete_faq'),

    path('cancel/', CancelView.as_view(), name='cancel'),
    path('error/', CancelView.as_view(), name='error'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<fk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')

    
    
]
# Staff URLs
'''
path('staff/dashboard/', views.staff_dashboard, name='dashboard'),
path('staff/merch/', views.staff_merch, name='staff_merch'),
path('staff/faq/', views.staff_faq, name='staff_faq'),
path('staff/login/', views.staff_login, name='staff_login'),
'''