from django.shortcuts import redirect, render #ดึงมาจาก template
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required # เอาไว้ตรวจ login


# Create your views here.
def homePage(request):
	#return HttpResponse("<h1>Hello Pesol</h1>")
	return render(request, 'school/home.html')

def aboutPage(request):
	return render(request, 'school/about.html')

def contactUs(request):
	return render(request, 'school/contact.html')


from .models import ExamScore, AllStudent

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


##### Search Page #####
@login_required # function บังคับ login ก่อน
def searchStudent(request):

	if request.method == 'POST':
		data = request.POST.copy()
		search_id = data.get('search') # เอามาจาก แอททิบิว name ใน html
		
		print(search_id, type(search_id))
		try:
			result = AllStudent.objects.get(student_id=search_id)
			print('RESULT: ', result)
			context = {'result': result,
						'check': 'found'}
		except:
			context = {'result': 'ไม่มีข้อมูล',
						'check': ''}
			
		return render(request, 'school/search.html', context)
	
	# MODELS.objects.all() ดึงค่าทั้งหมด
	# MODELS.objects.get(student_id = '631001') ดึงค่าแค่ตัวเดียว หากเกินจะ error
	# MODELS.objects.filter(level = 'ม.1') ดึงค่ามากกว่า 0 ค่า ผลออกมาเป็นชนิด list
	#search = AllStudent.objects.get(student_id = )
	return render(request, 'school/search.html')