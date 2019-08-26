from django.urls import path,include
from emplist import views
app_name='emp'
urlpatterns = [
    path('addlogic/', views.addlogic, name='addlogic'),
    path('emplist/', views.emplist, name='emplist'),
    path('delete/', views.delete, name='delete'),
    path('loadupdate/', views.loadupdate, name='loadupdate'),
    path('updatestatus/', views.updatestatus, name='updatestatus'),
    path('update/', views.update, name='update'),
    path('login/', views.login, name='login'),
]