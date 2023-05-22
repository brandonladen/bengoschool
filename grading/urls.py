from django.urls import path

from .views import*

urlpatterns = [
    #################grading rules########################
    path("rules/list/", GradingListView.as_view(), name="grading-list"),
    path("rules/create/", GradingCreateView.as_view(), name="grading-create"),
    path("rules/<int:pk>/detail/", GradingDetailView.as_view(), name="grading-detail"),
    path("rules/<int:pk>/update/", GradingUpdateView.as_view(), name="grading-update"),
    path("rules/<int:pk>/delete/", GradingDeleteView.as_view(), name="grading-delete"),
     #################overall grading rules########################
    path("overal/list/", OverallGradingListView.as_view(), name="overallgrading-list"),
    path("overal/create/", OverallGradingCreateView.as_view(), name="overallgrading-create"),
    path("overal/<int:pk>/detail/", OverallGradingDetailView.as_view(), name="overallgrading-detail"),
    path("overal/<int:pk>/update/", OverallGradingUpdateView.as_view(), name="overallgrading-update"),
    path("overal/<int:pk>/delete/", OverallGradingDeleteView.as_view(), name="overallgrading-delete"),
    ###########grades#######################################
     path("grades/list/", GradesListView.as_view(), name="grades-list"),
    path("grades/create/", GradesCreateView.as_view(), name="grades-create"),
    path("grades/<int:pk>/update/", GradesUpdateView.as_view(), name="grades-update"),
    path("grades/<int:pk>/delete/", GradesDeleteView.as_view(), name="grades-delete"),
     ###########gradeing levels################################
     path("level/list/", GradingLevelListView.as_view(), name="gradinglevel-list"),
    path("level/create/", GradingLevelCreateView.as_view(), name="gradinglevel-create"),
    path("level/<int:pk>/update/", GradingLevelUpdateView.as_view(), name="gradinglevel-update"),
    path("level/<int:pk>/delete/", GradingLevelDeleteView.as_view(), name="gradinglevel-delete"),
     path(
        "current-level/", CurrentGradingLevelView.as_view(), name="current-level"
    ),
]
