from django.shortcuts import render
from users.models import Users

# Create your views here.
def Home(request):
	#import ipdb; ipdb.set_trace()
	if str(request.user) != 'AnonymousUser':
		user = request.user
		user = Users.objects.get(u_name=user)
		context = {
			"user" : user
		}
		return render(request,"home.html",context)
	else:
		user='none'
		context = {
			'user' : user
		}

	return render(request,"landingpage.html",context)


def Home2(request):
	#import ipdb; ipdb.set_trace()
	if str(request.user) != 'AnonymousUser':
		user = request.user
		user = Users.objects.get(u_name=user)
		context = {
			"user" : user
		}
	else:
		user= "none"
		context = {
			'user' : user
		}
	return render(request,"base.html",context)
