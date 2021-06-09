
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
    
    path('', include('quiz.urls')),
    path('register', user_views.register, name='register'),
    path('admin/', admin.site.urls),
]
