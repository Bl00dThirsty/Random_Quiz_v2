
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.home.urls')),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('signup/', signup, name="signup"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

