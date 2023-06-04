from django.urls import path
from . import views

urlpatterns = [
    path('timetable/', views.my_home_view, name='timetable_home'),
    path('list/', views.my_classList_view, name='classesT'),
    path('real_timetable/<int:class_id>/<int:stream>/', views.my_timetable_view, name='r_timetable'), #add id to help filter
    path('staff_list/<int:selected_class>/<int:selected_section>/', views.my_staff_list, name='timetable_staff_list'),
    path('timetable/subject_action/<str:subject>/<int:staff_id>/<str:selected_class>/<str:selected_section>/', views.subject_action, name='sub_action'),
    path('timetable/create/<str:subject>/<int:staff_id>/<str:selected_class>/<str:selected_section>/', views.create, name='create'),
    path("timetable/delete/<str:subject>/<int:staff_id>/<str:selected_class>/<str:selected_section>/",views.delete_lession, name='delete_lession'),
    path("timetable/edit/<str:subject>/<int:staff_id>/<str:selected_class>/<str:selected_section>/", views.edit_lession, name='edit_lession')               
]   
    