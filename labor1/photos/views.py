from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo
from .forms import CreatePhoto
from django.contrib.auth.decorators import login_required

def photo_list(request):
    sort_by = request.GET.get('sort', 'date')
    
    if sort_by == 'name':
        photos = Photo.objects.all().order_by('title')
    else:
        photos = Photo.objects.all().order_by('-date')

    return render(request, 'photos/photo_list.html', {'photos': photos})

def photo_page(request, slug):
    photo = Photo.objects.get(slug=slug)
    return render(request, 'photos/photo_page.html', {'photo': photo})

@login_required(login_url="/users/login/")
def new_photo(request):
    if request.method == 'POST':
        form = CreatePhoto(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('photos:list')
    else:
        form = CreatePhoto()
    return render(request, 'photos/new_photo.html', { 'form': form })

@login_required(login_url="/users/login/")
def photo_delete(request, slug):
    photo = get_object_or_404(Photo, slug=slug)
    
    if request.user != photo.author:
        return redirect('photos:list')

    if request.method == 'POST':
        photo.delete()
        return redirect('photos:list')
        
    return render(request, 'photos/photo_delete.html', {'photo': photo})