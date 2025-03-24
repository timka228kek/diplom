from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Course, UserProgress


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {'courses': courses})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})


from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    progress = UserProgress.objects.filter(user=request.user)
    return render(request, 'auth/profile.html', {'progress': progress})