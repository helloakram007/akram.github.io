from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    

    path('', views.home,name='home'),
    path('contact', views.contact,name='contact'),
    path('blog', views.blog,name='blog'),
    path('Portfoli', views.Portfoli,name='Portfoli'),
    path('<str:slug>',views.blogPost,name="blogpost"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

