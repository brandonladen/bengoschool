from django.urls import path

from .views import *

urlpatterns = [
    # management
    path("staff/home/", staff_home, name='staff_home'),
    path("staff/apply/leave/", staff_apply_leave,
         name='staff_apply_leave'),
    path("staff/feedback/", staff_feedback, name='staff_feedback'),
    path("staff/view/profile/", staff_view_profile,
         name='staff_view_profile'),
    path("staff/attendance/take/", staff_take_attendance,
         name='staff_take_attendance'),
    path("staff/attendance/update/", staff_update_attendance,
         name='staff_update_attendance'),
    path("staff/get_students/", get_students, name='get_students'),
    path("staff/attendance/fetch/", get_student_attendance,
         name='get_student_attendance'),
    path("staff/attendance/save/",
         save_attendance, name='save_attendance'),
    path("staff/attendance/update/",
         update_attendance, name='update_attendance'),
    path("staff/fcmtoken/", staff_fcmtoken, name='staff_fcmtoken'),
    path("staff/view/notification/", staff_view_notification,
         name="staff_view_notification"),
]
