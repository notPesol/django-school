from django.shortcuts import redirect, render #ดึงมาจาก template
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

from django.contrib.auth.models import User

def register(request):
	if request.method == 'POST':
		data = request.POST.copy()
		first_name = data.get('first_name')
		last_name = data.get('last_name')
		email = data.get('email')
		password = data.get('password')

		newuser = User()
		newuser.username = email
		newuser.first_name = first_name
		newuser.last_name = last_name
		newuser.email = email
		newuser.set_password(password)
		newuser.save()
		# from django.shortcuts import redirect
		return redirect('login')

	return render(request, 'school/register.html')

