from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('djangoadmin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('admin/', include('app.urls')),
    path('', include('app.frontend.urls')),
]
