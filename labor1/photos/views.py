from django.shortcuts import redirect, render
from .models import Photo
from .forms import CreatePhoto
from django.contrib.auth.decorators import login_required

def photo_list(request):
    photos = Photo.objects.all().order_by('-date')
    return render(request, 'photos/photo_list.html', {'photos': photos})

def photo_page(request, slug):
    photo = Photo.objects.get(slug=slug)
    return render(request, 'photos/photo_page.html', {'photo': photo})

@login_required(login_url="/users/login/")
def post_new(request):
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