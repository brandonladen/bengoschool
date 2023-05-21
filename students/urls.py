from django.urls import path

from .views import *

urlpatterns = [
    path("list", StudentListView.as_view(), name="student-list"),
    path("<int:pk>/", StudentDetailView.as_view(), name="student-detail"),
    path("create/", StudentCreateView.as_view(), name="student-create"),
    path("<int:pk>/update/", StudentUpdateView.as_view(), name="student-update"),
    path("delete/<int:pk>/", StudentDeleteView.as_view(), name="student-delete"),
    path("upload/", StudentBulkUploadView.as_view(), name="student-upload"),
    path("download-csv/", DownloadCSVViewdownloadcsv.as_view(), name="download-csv"),
    # management
    path("student/home/", student_home, name='student_home'),
    path("student/view/attendance/", student_view_attendance,
         name='student_view_attendance'),
    path("student/apply/leave/", student_apply_leave,
         name='student_apply_leave'),
    path("student/feedback/", student_feedback,
         name='student_feedback'),
    path("student/view/profile/", student_view_profile,
         name='student_view_profile'),
    path("student/fcmtoken/", student_fcmtoken,
         name='student_fcmtoken'),
    path("student/view/notification/", student_view_notification,
         name="student_view_notification"),
    path('student/view/result/', student_view_result,
         name='student_view_result'),
]
