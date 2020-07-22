from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import posts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', posts.views.index, name="index"),
    # post app
    # CREATE (new, create)
    path('posts/new', posts.views.new, name="new"),
    path('posts/create', posts.views.create, name="create"),
    # READ(detail)
    path('posts/<int:post_id>', posts.views.detail, name='detail'),

    path('accounts/', include('accounts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
