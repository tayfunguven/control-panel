from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('momentomedya.urls')),
    path('m-panel/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('print', include('Document.urls', namespace='Document'),),
]
