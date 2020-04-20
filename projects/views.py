from django.shortcuts import render
from .forms import AddProjectForm
from django.shortcuts import redirect

# Create your views here.

def add_project(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == "POST":
            form = AddProjectForm(request.POST)
            if form.is_valid:
                new_project = form.save(commit=False)
                new_project.owner_id = current_user.id
                new_project.save()
                return redirect("user_projects", current_user.id)
        else:
            form = AddProjectForm()

        return render(request, "projects/add_project.html", {"form": form})
    else:
        return redirect("home")