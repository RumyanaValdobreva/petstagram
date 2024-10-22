from django.urls import path, include
from petstagram.photos import views


urlpatterns = [
    path('photos/', views.add_photo_page, name='add-photo'),
    path('<int:pk>/', include([
        path('', views.photo_details_page, name='photo-details'),
        path('edit/', views.photo_edit_page, name='photo_edit'),
        path('delete/', views.photo_delete, name='photo_delete'),
    ])),
]