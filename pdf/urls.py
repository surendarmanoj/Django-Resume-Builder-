from xml.etree.ElementInclude import include
from django.urls import path
from .views import accept,resume,resume_download

urlpatterns = [
    path("",accept,name='accept'),
    path("<int:pk>/",resume, name = 'resume'),
    path("<int:pk>/download/",resume_download, name='download'),
    
]