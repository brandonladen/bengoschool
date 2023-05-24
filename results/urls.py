from django.urls import path

from .views import *

urlpatterns = [
    path("create/", create_result, name="create-result"),
    path("edit-results/", edit_results, name="edit-results"),
    path("view/all", ResultListView.as_view(), name="view-results"),
    path("view/all<int:id>/", ResultListView.as_view(), name="view-results"),
    path('result/reportcard/all/',load_student_card,name='load-all-cards')
]
