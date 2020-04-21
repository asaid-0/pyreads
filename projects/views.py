from django.shortcuts import render
from .forms import AddProjectForm
from django.shortcuts import redirect
from users.models import Project, Comment
from django.http import HttpResponse


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
                return redirect("user_projects")
        else:
            form = AddProjectForm()

        return render(request, "projects/add_project.html", {"form": form})
    else:
        return redirect("home")


def view_project(request, id):
    project = Project.objects.filter(id = int(id))
    if project.exists():
        context = {"project": project.first()}
    else:
        context = {"project": None}
        
    return render(request, "projects/view.html", context)

def add_comment(request, id):
    project = Project.objects.filter(id = int(id))
    if not (project.exists() and request.user.is_authenticated):
        return redirect("home")

    if request.method.lower() == "get":
        return redirect("view_project", id=project.first().id)


    user = request.user
    create_comment = Comment(content=request.POST.get('content'), user=user, project=project.first())
    create_comment.save()
    return redirect("view_project", id=project.first().id)

    
    # return render(request, "users/user_profile.html", context)