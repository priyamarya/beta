from django.shortcuts import render,get_object_or_404
from .forms import SubscriptionForm
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from django.utils import timezone
import datetime
from django.contrib.auth.decorators import login_required
from users.models import Users
from .models import Subscription
from newspapers.models	 import Newspapers 
# Create your views here.

@login_required(login_url='/users/login/')
def Subscribe(request):
	import ipdb; ipdb.set_trace()
	if request.method == "POST":
		form = SubscriptionForm(request.POST or None)
		user = request.user
		user = Users.objects.get(u_name=user)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.sub_user = user
			instance.start_date = str(datetime.date.today())
			instance.save()
			form.save_m2m()
			
			context = {
				'title' : "thhanksss",
			}
		else:
			context={'title': "sorry"}
	else:
		form = SubscriptionForm()
		context = {'title':"please fill the form.",'form':form,}
		context.update(csrf(request))
	return render(request,'subscribe.html',context)

@login_required(login_url='/users/login/')
def subscription(request):
	#import ipdb; ipdb.set_trace()
	user=request.user
	user = Users.objects.get(u_name=user)
	queryset=Subscription.objects.all()
	if queryset.filter(sub_user=user).exists():
		user=Subscription.objects.get(sub_user=user)
		papers=user.sub_paper.all()
		context={
			"papers": papers,
			"start_date" : user.start_date,
			"message":"You have subscribed for:-",
			"address":user.address

		}
	else:
		context={
			'message':"You have not subscribed for any newspaper till now. start your subscription today!!"
		}
	return render(request,"subscription.html",context)

@login_required(login_url='/users/login/')
def editsubscription(request):
	#import ipdb; ipdb.set_trace()
	user = request.user
	user = get_object_or_404(Users,u_name=user)
	queryset=Subscription.objects.all()
	if queryset.filter(sub_user=user).exists():
		instance=Subscription.objects.get(sub_user=user)
		if request.method == "GET":
			form = SubscriptionForm(request.POST or None, instance=instance)
			context={
				"form" : form
			}
		else:
			form = SubscriptionForm(request.POST or None, instance=instance)
			if form.is_valid():
				instance= form.save(commit=False)

				instance.save()
				form.save_m2m()
			context={
				"form":form
			}
			return render(request,"home.html",context)
	context.update(csrf(request))
	return render(request,"subscribe.html",context)

@login_required(login_url='/users/login/')
def Bill(request):
	#import ipdb; ipdb.set_trace()
	bill=0
	user=request.user
	user=Users.objects.get(u_name=user)
	user=Subscription.objects.get(sub_user=user)
	today=datetime.date.today()
	start=user.start_date
	days=(today-start).days
	if (len(user.sub_paper.all())>1):
		queryset = user.sub_paper.all()
		for papers in queryset:
			paper=str(papers)
			paper=Newspapers.objects.get(title=paper)
			amount=paper.price
			bill+=days*amount
	else:
		queryset = user.sub_paper.all()
		paper=str(queryset[0])
		paper=Newspapers.objects.get(title=paper)
		amount=paper.price
		bill+=days*amount
	context={
		"bill":bill
	}
	context.update(csrf(request))
	return render(request,"bill.html",context)



@login_required(login_url="/users/login/")
def allpapers(request):
	#import ipdb; ipdb.set_trace()
	user = request.user
	user=Users.objects.get(u_name=user)
	user=Subscription.objects.get(sub_user=user)

	queryset=user.sub_paper.all()
	querylist=[]
	for paper in queryset:
		querylist.append(str(paper))

	length=len(queryset)
	context={
		"queryset": queryset,
		"length":length,
		"querylist":querylist

	}
	context.update(csrf(request))
	return render(request,"allpaper.html",context)

@login_required(login_url="/user/login")
def paperbill(request,paper):
	#import ipdb; ipdb.set_trace()
	paper=Newspapers.objects.get(title=paper)
	user=request.user
	user=Users.objects.get(u_name=user)
	user=Subscription.objects.get(sub_user=user)
	today=datetime.date.today()
	start=user.start_date
	days=(today-start).days
	bill=days*paper.price
	context={
		"bill": bill,
	}
	return render(request,"paperbill.html",context)

@login_required(login_url="/user/login")
def allbills(request):
	#import ipdb; ipdb.set_trace()
	bill=0
	user=request.user
	user=Users.objects.get(u_name=user)
	user=Subscription.objects.get(sub_user=user)
	today=datetime.date.today()
	start=user.start_date
	days=(today-start).days
	querylist=[]
	queryset = user.sub_paper.all()
	if (len(user.sub_paper.all())>1):
		queryset = user.sub_paper.all()
		for papers in queryset:
			paper=str(papers)
			paper=Newspapers.objects.get(title=paper)
			amount=paper.price
			bill+=days*amount
			querylist.append(str(paper))
	else:
		queryset = user.sub_paper.all()
		paper=str(queryset[0])
		paper=Newspapers.objects.get(title=paper)
		amount=paper.price
		bill+=days*amount
		querylist.append(str(queryset[0]))
	context={
		"bill":bill,
		"querylist":querylist,
		"days": days,
		"queryset": queryset
	}

	context.update(csrf(request))
	return render(request,"allbills.html",context)
