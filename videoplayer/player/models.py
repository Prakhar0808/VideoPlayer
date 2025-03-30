from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

# forms.py (inside player app)
from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_file']

# views.py (inside player app)
from django.shortcuts import render, redirect
from .models import Video
from .forms import VideoForm

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'player/video_list.html', {'videos': videos})

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'player/upload_video.html', {'form': form})

# urls.py (inside player app)
from django.urls import path


urlpatterns = [
    path('', video_list, name='video_list'),
    path('upload/', upload_video, name='upload_video'),
]
