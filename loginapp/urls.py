from django.urls import path
from loginapp import views
app_name='loginapp'
urlpatterns =[
    path('loginlogic/',views.loginlogic,name='loginlogic'),
    path('registlogic/',views.registlogic,name="registlogic"),
    path('getcap/',views.getcap,name='getcap'),
    path('checkname/', views.checkname, name='checkname'),
    path('checkcaptcha/', views.checkcaptcha, name='checkcaptcha'),

]