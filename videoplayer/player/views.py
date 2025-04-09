from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Video
from .forms import VideoForm

def video_list(request):
    search_query = request.GET.get('q', '')
    if search_query:
        videos = Video.objects.filter(title__icontains=search_query).order_by('-uploaded_at')
    else:
        videos = Video.objects.all().order_by('-uploaded_at')
    
    # Paginate videos (6 per page)
    paginator = Paginator(videos, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }
    return render(request, 'player/video_list.html', context)

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'player/upload_video.html', {'form': form})
# yaha par changes
