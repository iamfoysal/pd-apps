from django.urls import path
from app1 import views

app_name = "my_app"

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('form/', views.form, name='form')
    # path('demo/', views.form, name='demo')



]