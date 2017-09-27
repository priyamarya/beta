from django.shortcuts import render
from .models import Newspapers
from .forms import Newspaperforms

# Create your views here.

def paper_entry(request):
	context= {}
	if request.method = "GET":
		form = Newspaperforms(request.POST or None)
	else:
		form = Newspaperforms(request.POST or None)
		instance = form.save(commit=False)
		instance.save()
	context.update(csrf(request))
	return render(request,"paper entry.html",context)
