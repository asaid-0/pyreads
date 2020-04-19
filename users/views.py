from django.shortcuts import render
from .models import User
from .forms import UserForm
from django.shortcuts import get_object_or_404, redirect
# Create your views here.

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