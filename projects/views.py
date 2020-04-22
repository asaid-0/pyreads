from django.shortcuts import render
from .forms import AddProjectForm, ImageForm, CommentForm
from django.shortcuts import redirect
from django.db.models import Sum
from users.models import Project, Comment, Category, Donation, Project_pictures, User
from django.http import HttpResponse


# Create your views here.


def add_project(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == "POST":
            form = AddProjectForm(request.POST)
            image_form = ImageForm(request.POST, request.FILES)
            if form.is_valid() and image_form.is_valid():
                new_project = form.save(commit=False)
                new_project.owner_id = current_user.id
                new_project.save()
                form.save_m2m()
                for file in request.FILES.getlist('picture'):
                    picture = Project_pictures(
                        project = new_project,
                        picture = file
                    )
                    picture.save()
                return redirect("user_projects")
        else:
            form = AddProjectForm()
            image_form = ImageForm()
        return render(
            request,
            "projects/add_project.html",
            {"form": form, "image_form": image_form},
        )
    else:
        return redirect("home")


def view_project(request, id):
    project = Project.objects.get(id=int(id))
    project_donations = project.donation_set.aggregate(total_amount=Sum('amount'))
    context = {"project": project , "project_donations": project_donations, "form": CommentForm() }
        
    return render(request, "projects/view.html", context)


def delete_project(request , id):
    if request.user.is_authenticated:
        if request.method == "POST":
            project = Project.objects.get(id =id)
            project_donations = project.donation_set.aggregate(total_amount=Sum('amount'))
            project_donations = project_donations if  project_donations['total_amount'] else {'total_amount': 0} 
            if (project.total_target*0.25 >  project_donations['total_amount']) or project_donations.total_amount == None:
                project.delete()
                return redirect("user_projects") # with message deleted successfully
            else:
                return redirect("user_projects")
        else:
            return redirect("user_projects")
    else:
        return redirect("home")





def add_comment(request, id):
    form = CommentForm(request.POST)
    project = Project.objects.filter(id=int(id))
    if not (project.exists() and request.user.is_authenticated):
        return redirect("home")

    if request.method.lower() == "get":
        return redirect("view_project", id=project.first().id)

    if form.is_valid():
        user = request.user
        create_comment = form.save(commit=False)
        create_comment.user = user
        create_comment.project = project.first()
        create_comment.save()
        return redirect("view_project", id=project.first().id)
    else:
        return render(
            request,
            f"projects/view.html",
            {"project": project.first(), "form": form}
        )




def get_category_projects(request, id):
    category = Category.objects.get(id=id)
    projects = category.project_set.all()
    context = {"projects": projects, "category": category}
    return render(request, "projects/category_projects.html", context)
