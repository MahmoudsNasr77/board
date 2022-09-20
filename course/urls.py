app_name="course"
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.CoursesList.as_view(),name='view_course'),
     path('<str:slug>',views.single_course,name='view_single_course'),
     path('<str:slug>/addComment',views.addComment,name='addComment'),
     
]