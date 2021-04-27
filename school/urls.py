from django.urls import path, include
from .views import * # ดึงฟังก์ชัน มาใช้งาน
urlpatterns = [
    #localhost:8000/
    path('', homePage, name='home-page'),
    path('about/', aboutPage, name='about-page'),
    path('contact/', contactUs, name='contact-page'),
    path('score/', showScore, name='score-page'),
]