from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('datasetfinder',views.datasetfinder,name='datasetfinder'),
    path('generate_dataset',views.generate_dataset,name='generate_dataset'),
    path('download/<str:filename>/', views.download_file, name='download-file'),
]