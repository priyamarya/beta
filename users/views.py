from django.shortcuts import render, render_to_response,HttpResponseRedirect,get_object_or_404
from django.http import Http404
from django.template.context_processors import csrf
from .models import Users, UserInfo
from django.contrib.auth.decorators import login_required	
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from .forms import UserInfoForm
# Create your views here.

def register(request):
	context = {}
	#import ipdb; ipdb.set_trace()
	if request.method == 'POST':
		try:
			name = request.POST.get("u_name")
			mob_no = request.POST.get("mobile")
			phone = request.POST.get("phone")
			email = request.POST.get("email")
			address = request.POST.get("address")
			password1 = request.POST.get("password1")
			password2 = request.POST.get("password2")
			if password2 == password1:
				user = User.objects.create_user(
					username=name,
					password=password1,
					email=email)
				user_info = Users(
					u_name=user,
					
					mob_no = mob_no,
					email_id = email,
					address = address,
					password = password1)
				user_info.save()
				context = {
				'success':True,
				'message' : 'Welcome to Sightnext',

				}
				
				context.update(csrf(request))
				return HttpResponseRedirect("/users/login/")
			else:
				print("not done pass")
				context = {
					'success':False,
					'message': 'Passwords did not match, enter again.'
				}
				context.update(csrf(request))
				return render_to_response('register.html', context)
		except:
			print("not done pass except")
			context = {
				'success': False,
				'message':'User profile can not be saved. please try agian.'
			}
			context.update(csrf(request))
			return render_to_response('register.html',context)
	else:
		print("not done post")
		context = {'user': request.user.username,'message': "please fill the form"}
		context.update(csrf(request))
		return render_to_response('register.html', context)

def login(request):
	context = {}
	#import ipdb; ipdb.set_trace()
	if request.method == "GET":
		if request.user.is_authenticated():
			context['user'] = request.user.username
			context.update(csrf(request))
			return render_to_response('login.html', context)
		else:
			context.update(csrf(request))
			return render(request,'login.html', context)
	else:
		name = request.POST.get('u_name')
		password = request.POST.get('password')
		user = auth.authenticate(username = name, password = password)
		if request.user.is_authenticated():
			context['status'] = "one User already logged in"
			context.update(csrf(request))
			return render_to_response("login.html", context)
		else:
			if user is not None:
				if user.is_active:
					auth.login(request,user)
					context = {
						'status' : "login successfull",
						"user" : request.user.username,
					}
					context.update(csrf(request))
					return HttpResponseRedirect("/users/%s/"%name)
				else:
					context = {
						'status' : "Account Deactivated",
						}	
			else:
				context = {"status" : "invalid login details", "user": request.user,}
				context.update(csrf(request))
				return render_to_response("login.html",context)


		

@login_required(login_url='/users/login/')
def logout(request):
	#import ipdb; ipdb.set_trace()
	context={}
	if request.user.is_authenticated():
		auth.logout(request)
		context['status'] = 'Logout successfull'
		context.update(csrf(request))
		return login(request)
	else:
		auth.logout(request)
		context['status'] = 'Logout successfull'
		context.update(csrf(request))
		return login(request)

@login_required(login_url='/users/login/')
def loginuser(request,username):
	
	if (username==request.user.username):

		if request.method == "GET":

			if request.user.is_authenticated():
				
				context={'user': request.user.username}
				context.update(csrf(request))
				return render(request,'home.html',context)
			else:
				context.update(csrf(request))
				return render(request,'home.html',context)
		else:
			context={}
			context.update(csrf(request))
			return render(request,'home.html',context)
	else:
		raise Http404

'''@login_required(login_url='users/(?P<username>[\w.@+-]+)/')
def profile_update(request,username):
	#import ipdb; ipdb.set_trace()
	title = "Update your profile here."
	instance=get_object_or_404(User,username=username)
	if request.method =="GET":
		form = UserInfoForm(request.POST or None)
		context = {
			"title": title,
			"form": form
		}	
	else:
		user = request.user
		user = Users.objects.get(u_name=user)
		form = UserInfoForm(request.POST,request.FILES or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user_link=user
			instance.save()

		print request.POST.get('full_name')
		print request.POST.get('sex')
		context = {
			"title": "thanks for telling us more about you.",
		}

			
	context.update(csrf(request))
	return render(request, "profile entry.html",context)
	'''

@login_required(login_url='users/(?P<username>[\w.@+-]+)/')
def profile_edit(request,username):
	#import ipdb; ipdb.set_trace()
	title = "Edit Our Profile Here"

	instance=get_object_or_404(User,username=username)
	instance = Users.objects.get(u_name=instance)
	if UserInfo.objects.filter(user_link=instance).exists():
		instance = UserInfo.objects.get(user_link=instance)
		if request.method =="GET":
			form = UserInfoForm(request.POST or None,instance=instance)
			context = {
				"title": title,
				"form": form
			}
			context.update(csrf(request))
			return render(request, "profile entry.html",context)	
		else:

			user = request.user
			user = Users.objects.get(u_name=user)
			form = UserInfoForm(request.POST,request.FILES or None, instance=instance)
			if form.is_valid():
				instance = form.save(commit=False)
				
				instance.save()

			print request.POST.get('full_name')
			print request.POST.get('sex')
			context = {
				"title": "thanks for telling us more about you.",
			}
			context.update(csrf(request))
			return HttpResponseRedirect("/users/%s/"%username)
	else:
		if request.method =="GET":
			form = UserInfoForm(request.POST or None)
			context = {
				"title": title,
				"form": form
			}	
		else:
			user = request.user
			user = Users.objects.get(u_name=user)
			form = UserInfoForm(request.POST,request.FILES or None)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.user_link=user
				instance.save()

			print request.POST.get('full_name')
			print request.POST.get('sex')
			context = {
				"title": "thanks for telling us more about you.",
			}

				
	context.update(csrf(request))
	return render(request, "profile entry.html",context)


def profile(request,username):
	#import ipdb; ipdb.set_trace()
	instance = User.objects.get(username=username)
	instance= Users.objects.get(u_name=instance)
	userinfo=UserInfo.objects.get(user_link=instance)

	context={
		"name" : userinfo.full_name,
		"sex" : userinfo.sex,
		"pic" : userinfo.profile_pic,
		"email" :instance.email_id,
		"username" : instance.u_name,
		"contact_no" : instance.mob_no,
		"address" : instance.address,
		"joining_date" : instance.joining_date

	}
	context.update(csrf(request))
	return render(request, "profile.html", context)