from django.shortcuts import redirect, render #ดึงมาจาก template
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required # เอาไว้ตรวจ login

from django.contrib.auth.models import User

from .models import ExamScore, AllStudent, Profile, DocumentUpload

#สำหรับจัดการไฟล์
from django.core.files.storage import FileSystemStorage


# Create your views here.
def homePage(request):
	#return HttpResponse("<h1>Hello Pesol</h1>")
	return render(request, 'school/home.html')

def aboutPage(request):
	return render(request, 'school/about.html')

def contactUs(request):
	return render(request, 'school/contact.html')



def showScore(request):
	score = ExamScore.objects.all() # ดึงค่ามาจาก database ทั้งหมด
	context = {'score': score}
	return render(request, 'school/showscore.html', context)


def register(request):
	if request.method == 'POST':
		data = request.POST.copy()

		if data.get('password') != data.get('re_password'):
			context = {'error': 'รหัสผ่านไม่ตรงกัน !'}
			return render(request, 'school/register.html', context)

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

		try:
			newuser.save()
			# from django.shortcuts import redirect
			return redirect('login')
		except:
			context = {'error': 'อีเมลล์ดังกล่าว มีคนใช้แล้ว !'}
			return render(request, 'school/register.html', context)

	return render(request, 'school/register.html')


##### Search Page #####
@login_required # function บังคับ login ก่อน
def searchStudent(request):

	if request.user.profile.usertype != 'teacher':
		return redirect('home-page')

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



@login_required # function บังคับ login ก่อน
### Edit Profile ###
def editProfile(request):

	username = request.user.username

	current = User.objects.get(username=username)

	context = {'data': current}

	if request.method == 'POST' and request.FILES['photoprofile']:
		data = request.POST.copy()
		first_name = data.get('first_name')
		last_name = data.get('last_name')
		email = data.get('email')
		#password = data.get('password')

		myprofile = User.objects.get(username=username)
		try:
			setProfile = Profile.objects.get(user=myprofile)
		except:
			setProfile = Profile()
			setProfile.user = myprofile

		### file system #######
		file_image = request.FILES['photoprofile']
		file_image_name = file_image.name
		fs = FileSystemStorage()
		image_folder = 'photo_profile/'
		file_name = fs.save(image_folder + file_image_name, file_image)
		upload_file_url = fs.url(file_name)
		
		setProfile.photoprofile = upload_file_url[6:] # ตัด /media ออก
		setProfile.save()
		###################

		myprofile.first_name = first_name
		myprofile.last_name = last_name
		myprofile.email = email
		#newuser.set_password(password)

		myprofile.save()
		

		# from django.shortcuts import redirect
		return redirect('profile-page')

	return render(request, 'school/editprofile.html', context)




def showDocument(request):
	document = DocumentUpload.objects.all() # ดึงค่ามาจาก database ทั้งหมด
	context = {'document': document}
	return render(request, 'school/document.html', context)
