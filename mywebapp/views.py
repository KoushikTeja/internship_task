from django.shortcuts import render
from django.http import HttpResponse
from .backend_gpt import identify_topics_with_gpt

def home(request):
    if request.method == 'POST':
        transcription_text = request.POST.get('text', '')
        summary = identify_topics_with_gpt(transcription_text)
        return render(request, 'home.html', {'summary': summary})

    return render(request, 'home.html')
