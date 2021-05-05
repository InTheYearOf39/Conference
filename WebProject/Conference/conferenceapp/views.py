from django.shortcuts import render, redirect
from conferenceapp.forms import RegistrationForm

# Create your views here.
def  home(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    else:
        form = RegistrationForm()

    return render(request,"conferenceapp/index.html",{'form':form})
