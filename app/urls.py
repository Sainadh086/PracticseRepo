from django.urls import path
from . import views 

urlpatterns = [
    
    path('', views.index, name='index'),
    path('project', views.project, name='project'),
    path('model', views.model, name='model'),
    path('about', views.about, name='about'),
    path('test', views.test, name='test'),

]