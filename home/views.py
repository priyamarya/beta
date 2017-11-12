from django.shortcuts import render
from users.models import Users


# Create your views here.
def Home(request):
	#import ipdb; ipdb.set_trace()
	if str(request.user) != 'AnonymousUser':
		user = request.user
		user = Users.objects.get(u_name=user)
		context = {
			"user" : user,
			'nbar' :'home',
		}
		return render(request,"home.html",context)
	else:
		user='none'
		context = {
			'user' : user,
			'nbar' : 'home',
		}

	return render(request,"home.html",context)


def Home2(request):
	#import ipdb; ipdb.set_trace()
	if str(request.user) != 'AnonymousUser':
		user = request.user
		user = Users.objects.get(u_name=user)
		
		context = {
			"user" : user,
			'nbar' : 'home',
		}
	else:
		user= "none"
		context = {
			'user' : user,
			'nbar' : 'home',
		}
	return render(request,"home.html",context)



def home(request):
	
	return render(request,'home.html',{'nbar' : 'home',})

def contact(request):
	return  render(request,'contact.html',{'nbar' : 'contact',})

def faqs(request):
	
	return render(request,'faqs.html',{'nbar' : 'faqs',})

def account(request):
	
	return render(request,'account.html',{'nbar' : 'account',})

def about(request):
	
	return render(request,'about.html',{'nbar' : 'about',})

def workwithus(request):
	
	return render(request,'workwithus.html',{'nbar' : 'workwithus',})

def privacy(request):
	
	return render(request,'privacypolicy.html',{'nbar' : 'privacy',})

	
def welcome(request):
	return render(request,'welcome.html',{'nbar' : 'privacy',})
def dummy(request):
	return render(request,'dummy.html',{'nbar' : 'privacy',})


