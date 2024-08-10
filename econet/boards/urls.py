from django.urls import path
from .views import gathering_list_create, gathering_detail_update_delete, create_comment, like_gathering

urlpatterns = [
    path('', gathering_list_create, name='gathering-list-create'),
    path('<int:gatheringpost_id>/', gathering_detail_update_delete, name='gathering-detail-update-delete'),
    path('<int:gatheringpost_id>/comments/', create_comment, name='create-comment'),
    path('<int:gathering_id>/like/', like_gathering, name='like-gathering'),
]
