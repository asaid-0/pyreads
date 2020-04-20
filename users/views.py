from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Category
from .forms import UserForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import get_user_model

# Create your views here.


def home(request):
    categories = Category.objects.all()

    context = {"categories": categories}
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


def get_projects(request, id):
    user = User.objects.get(id=id)
    projects = user.project_set.all()

    context = {"projects": projects}
    return render(request, "users/user_projects.html", context)


def get_donations(request, id):
    user = User.objects.get(id=id)
    donations = user.project_donations.all()
    context = {"donations": donations}
    return render(request, "users/user_donations.html", context)


def get_category_projects(request, id):
    category = Category.objects.get(id=id)
    projects = category.project_set.all()
    context = {"projects": projects, "category": category}
    return render(request, "users/category_projects.html", context)
