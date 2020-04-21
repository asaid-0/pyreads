from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum
from .models import User, Category, Project, Rate
from .forms import UserForm
from django.shortcuts import redirect
from django.contrib.auth import get_user_model


# Create your views here.


def home(request):
    categories = Category.objects.all()
    projects = Project.objects.all()
    latest_projects = Project.objects.all().order_by('-id')[:5]
    high_rated_set = Rate.objects.values('project_id').annotate(
        sum_rate=Sum('rate')).order_by('-sum_rate')[:5]
    context = {
        "categories": categories,
        "latest_projects": latest_projects,
        "high_rated_set": high_rated_set,
        "projects": projects
    }
    return render(request, "users/home.html", context)


def show_profile(request):
    if request.user.is_authenticated:
        current_user = request.user
        user = User.objects.get(id=current_user.id)
        context = {"user": user}
        return render(request, "users/user_profile.html", context)
    else:
        return redirect("home")


def edit_profile(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == "POST":
            form = UserForm(request.POST, request.FILES, instance=current_user)
            if form.is_valid:
                current_user = form.save(commit=False)
                current_user.save()
                return redirect("profile")
        else:
            form = UserForm(instance=current_user)

        return render(request, "users/edit_profile.html", {"form": form})
    else:
        return redirect("home")


def delete_account(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == "POST":
            current_user.delete()
            return redirect("home")
        else:
            return redirect("profile")
    else:
        return redirect("home")


def get_projects(request):
    if request.user.is_authenticated:
        current_user = request.user
        user = User.objects.get(id=current_user.id)
        projects = user.project_set.all()
        context = {"projects": projects}
        return render(request, "users/user_projects.html", context)
    else:
        return redirect("home")


def get_donations(request):
    if request.user.is_authenticated:
        current_user = request.user
        user = User.objects.get(id=current_user.id)
        donations = user.project_donations.all()
        context = {"donations": donations}
        return render(request, "users/user_donations.html", context)
    else:
        return redirect("home")

