
from django.contrib import admin
from django.urls import path, include
from apps.quiz.views import index
from apps.quiz.views import error
from apps.accounts.views import signup
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', include('apps.home.urls'), name='home'),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('error/', error, name='error'),
    path('signup/', signup, name="signup"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

