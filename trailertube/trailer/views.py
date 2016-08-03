from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from .forms import VideoForm
from .models import Trailer

def Video(request):
    video = Trailer.objects.order_by("-id")
    query = request.GET.get('q')
    if query:
        video = video.filter(Q(title__icontains=query)|
                             Q(category__icontains=query)|
                             Q(release__icontains=query))
    # pagination
    paginator = Paginator(video, 16) # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        video = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        video = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        video = paginator.page(paginator.num_pages)

    context= {
        "video": video,
    }
    return render(request, 'index.html', context)

def add_video(request):
    form = VideoForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect("/")
    context={
        "form": form,
        "title": "Upload",
    }
    return render(request, 'forms.html', context)

def like_update(request, id=None):
    new = Trailer.objects.order_by('-id')
    like_count = get_object_or_404(Trailer, id=id)
    like_count.like+=1
    like_count.save()
    context = {
        'tr': new,
    }
    return render(request,'index.html',context)