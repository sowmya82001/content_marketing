from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContentViewSet, home
from .views import blog_list, blog_detail
from .views import social_media_page
from .views import contact_view
from django.conf.urls.static import static
from django.conf import settings


router = DefaultRouter()
router.register(r'content', ContentViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('api/', include(router.urls)),
    path('blogs/', blog_list, name='blog_list'),
    path('blogs/<slug:slug>/', blog_detail, name='blog_detail'),
    path("social-media/", social_media_page, name="social_media"),
    path('contact/', contact_view, name='contact'),
]
if settings.DEBUG:  # Only serve media files in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
