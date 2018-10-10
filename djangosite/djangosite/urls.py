from django.contrib import admin
from django.urls import include, path
from nextbook.views import suggestion

urlpatterns = [
    path('', include('menu.urls')),
    path('menu/', include('menu.urls')),
    path('nextbook/', include('nextbook.urls')),
    path('newbook/', include('newbook.urls')),
    path(r'?actions=newbook', include('newbook.urls')),
    path('admin/', admin.site.urls),
]
