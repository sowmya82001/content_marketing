from rest_framework import viewsets
from .models import Content
from .serializers import ContentSerializer
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Blog
from .models import SocialMedia
from .forms import ContactForm

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

def home(request):
    return render(request, 'content_marketing/base.html')

def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'content_marketing/blog_list.html', {'blogs': blogs})

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'content_marketing/blog_detail.html', {'blog': blog})

def social_media_page(request):
    """Fetch all social media details from the database and display them."""
    social_media_profiles = SocialMedia.objects.all()
    return render(request, "content_marketing/social_media.html", {"social_media_profiles": social_media_profiles})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save form data to database
            return redirect('contact')  # Redirect after submission
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})