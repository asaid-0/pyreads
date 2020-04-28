from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum, Avg
from .models import User, Category, Project, Rate, Project_pictures, Donation
from .forms import UserForm, ConfirmPasswordForm
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    categories = Category.objects.all()
    projects = Project.objects.all()
    latest_projects = Project.objects.all().order_by("-id")[:5]
    high_rated_set = (
        Rate.objects.values("project_id")
        .annotate(avg_rate=Avg("rate"))
        .order_by("-avg_rate")[:5]
    )
    
    context = {
        "categories": categories,
        "latest_projects": latest_projects,
        "high_rated_set": high_rated_set,
        "projects": projects,
    }
    return render(request, "users/home.html", context)


@login_required
def show_profile(request):
    current_user = request.user
    password_form = ConfirmPasswordForm()
    context = {"user": current_user, "form": password_form}
    return render(request, "users/user_profile.html", context)


@login_required
def edit_profile(request):
    current_user = request.user
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            current_user = form.save(commit=False)
            current_user.save()
            return redirect("profile")
    else:
        form = UserForm(instance=current_user)

    return render(request, "users/edit_profile.html", {"form": form})


@login_required
def delete_account(request):
    current_user = request.user
    password_form = ConfirmPasswordForm(request.POST, instance=current_user)
    if request.method == "POST":
        if password_form.is_valid():
            current_user.delete()
            return redirect("home")
    else:
        password_form = ConfirmPasswordForm(instance=current_user)
    return render(request, "users/delete_account.html", {"form": password_form})


@login_required
def get_projects(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    projects = user.project_set.all()

    context = {
        "projects": projects,
    }
    return render(request, "users/user_projects.html", context)


@login_required
def get_donations(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    donations = user.project_donations.distinct()
    context = {
        "donations": donations,
    }
    return render(request, "users/user_donations.html", context)
