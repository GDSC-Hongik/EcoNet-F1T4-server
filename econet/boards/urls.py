from django.urls import path
from .views import gathering_list_create, gathering_detail_update_delete, create_comment

urlpatterns = [
    path('', gathering_list_create, name='gathering-list-create'),
    path('gatherings/<int:gatheringpost_id>/', gathering_detail_update_delete, name='gathering-detail-update-delete'),
    path('<int:gatheringpost_id>/comments/', create_comment, name='create-comment'),
]
