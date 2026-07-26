from django.shortcuts import render, redirect, get_object_or_404
from .models import Fish
from .forms import FishForm


def home(request):
    return render(request, 'fishes/home.html')


def fish_list(request):
    fishes = Fish.objects.all()
    return render(request, 'fishes/fish_list.html', {'fishes': fishes})


def fish_create(request):
    if request.method == 'POST':
        form = FishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fish_list')
    else:
        form = FishForm()
    return render(request, 'fishes/fish_form.html', {'form': form, 'title': 'Add Fish'})


def fish_update(request, pk):
    fish = get_object_or_404(Fish, pk=pk)
    if request.method == 'POST':
        form = FishForm(request.POST, instance=fish)
        if form.is_valid():
            form.save()
            return redirect('fish_list')
    else:
        form = FishForm(instance=fish)
    return render(request, 'fishes/fish_form.html', {'form': form, 'title': 'Edit Fish'})


def fish_delete(request, pk):
    fish = get_object_or_404(Fish, pk=pk)
    fish.delete()
    return redirect('fish_list')
