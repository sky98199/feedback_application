from django.shortcuts import render

from .forms import FbForm
from .models import FbModel

def home(request):
	if request.method == "POST":
		data=FbForm(request.POST)
		if data.is_valid():
			data.save()
			fm=FbForm()
			return render(request,"home.html",{"fm":fm,"msg":"we will get back to you"})
	else:
		fm= FbForm()
		return render(request,"home.html",{"fm":fm})
