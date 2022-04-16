from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render



class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":                       # If user submitted form data
        form = NewTaskForm(request.POST)               # takes the form submitted and saves it inside this form variable
        if form.is_valid():                            # check to see if form is valid
           task = form.cleaned_data["task"]            # if so, gets task and adds it to the list of existing tasks
           request.session["tasks"] += [task]
           return HttpResponseRedirect(reverse("tasks:index"))
        else:                                          #if form isnt valid
            return render(request, "tasks/add.html", { # renders the same .html back to user
                "form": form                           # passes in form submitted to see the errors made and to make modifications to their form
            })

    return render(request, "tasks/add.html", {         # if request method wasn't POST, renders .html
        "form": NewTaskForm()                          # renders an empty form
    })