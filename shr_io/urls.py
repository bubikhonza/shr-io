from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_shareplace/', views.create_shareplace, name='create_shareplace'),
    path('display_shareplace/<str:code>', views.display_shareplace, name="display_shareplace"),
    path('remove_shareplace/<str:code>', views.remove_shareplace, name="remove_shareplace"),
    path('remove_item/<int:id>', views.remove_item, name="remove_item"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)