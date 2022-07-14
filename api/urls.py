from django.urls import path
from . import views
#from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, #RegisterPage, TaskReorder
#from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('getnotes/', views.getNotes, name='getNotes'),
    path('createnote/', views.createNote, name='createNote'),
    path('test/', views.testapi, name='testapi'),
    #path('editnote/<str:noteId>', views.editNote, name='editNote'),
    #path('delnote/<str:noteId>', views.editNote, name='editNote'),

]