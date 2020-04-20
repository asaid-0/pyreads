from django.shortcuts import render
from django.http import HttpResponse
from .models import User , Category
from .forms import UserForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import get_user_model

# Create your views here.

def home(request):
    categories = Category.objects.all()



    context = {'categories': categories}
    return render(request, 'users/home.html', context )

def show_profile(request, id):
    user = User.objects.get(id = id)
    context = {'user': user}
    return render(request, 'users/user_profile.html', context)

def edit_profile(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST' :
        form = UserForm(request.POST, instance=user)
        if form.is_valid:
            user = form.save(commit=False)
            user.save()
            return redirect('profile', id=user.id)
    else:
        form = UserForm(instance=user)

    return render(request, 'users/edit_profile.html', {'form': form})

def get_projects(request, id):
    user = User.objects.get(id = id)
    projects =  user.project_set.all()
    
    context = {'projects': projects}
    return render(request, 'users/user_projects.html', context)

def get_donations(request, id):
    user = User.objects.get(id = id)
    donations =  user.project_donations.all()
    context = {'donations': donations}
    return render(request, 'users/user_donations.html', context)

def get_category_projects(request , id):
    category = Category.objects.get(id = id)
    projects = category.project_set.all()
    context = {'projects': projects , 'category': category}
    return render(request, 'users/category_projects.html', context )
