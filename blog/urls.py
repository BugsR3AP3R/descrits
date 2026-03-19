from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('carnet-de-lecture/', views.carnet, name='carnet'),
    path('fiction-et-confidences/', views.textes, name='textes'),
    path('pensees-en-vrac/', views.pensees, name='pensees'),
    path('a-propos/', views.about, name='about'),
    path('article/<slug:slug>/', views.post_detail, name='post_detail'),
]
