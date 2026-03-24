from django.shortcuts import render
from .models import Event, Coordinator, Gallery, SiteSetting

def index(request):
    events = Event.objects.all().order_by('start_time')
    faculty_coordinators = Coordinator.objects.filter(role='Faculty')
    student_coordinators = Coordinator.objects.filter(role='Student')
    gallery_images = Gallery.objects.all().order_by('heading', '-uploaded_at')
    
    # Fetch the active Google Form link
    settings = SiteSetting.objects.filter(is_active=True).first()
    reg_link = settings.registration_link if settings else "#"

    context = {
        'events': events,
        'faculty_coordinators': faculty_coordinators,
        'student_coordinators': student_coordinators,
        'gallery_images': gallery_images,
        'reg_link': reg_link,
    }
    return render(request, 'index.html', context)