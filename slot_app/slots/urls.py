from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save/', views.save_record, name='save_record'),
    path('total/', views.total, name='total'),
    path('delete/<int:pk>/', views.delete_record, name='delete_record'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
]
