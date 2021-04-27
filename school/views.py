from django.shortcuts import render #ดึงมาจาก template
from django.http import HttpResponse

# Create your views here.
def homePage(request):
	#return HttpResponse("<h1>Hello Pesol</h1>")
	return render(request, 'school/home.html')

def aboutPage(request):
	return render(request, 'school/about.html')

def contactUs(request):
	return render(request, 'school/contact.html')


from .models import ExamScore

def showScore(request):
	score = ExamScore.objects.all() # ดึงค่ามาจาก database ทั้งหมด
	context = {'score': score}
	return render(request, 'school/showscore.html', context)