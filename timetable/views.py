from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from authman.forms import *
from django.contrib import messages
from .forms import tableForm
from staff.models import *

# Create your views here.
def my_home_view(request):  
    return render(request, 'timetable/home.html')
def my_classList_view(request):
    classes=StudentClass.objects.all()
    data=[]
    for cl in classes:
        data.append({"class_id":cl.id,"class_name":cl.name,"streams":cl.sections.all()})
    print(data)
    context = {
        'classes': data
    }
    return render(request, 'timetable/timetable_list.html', context)
def my_timetable_view(request,class_id=0,stream=0):
    if stream != 0:
        classes = StudentClass.objects.filter(id=class_id,sections__id=stream).first()
        selected_section = ClassSection.objects.get(id=stream)
    context = {
        'classes': classes,
        'selected_section': selected_section
    }
    return render(request, 'timetable/real_timetable.html', context)
def my_staff_list(request, selected_class=0, selected_section=0):
    allStaff=None
    user_type=request.user.user_type
    if int(user_type) == 1:
       allStaff = Staff.objects.all()
    elif int(user_type) == 2:
        allStaff= Staff.objects.filter(admin=request.user.id).first()
    context = {
        'allStaff': allStaff,
        'page_title': 'Manage Staff',
        'selected_class': selected_class,
        'selected_section': selected_section 
    }
    return render(request, "timetable/timetable_staff_list.html", context)
def subject_action(request, subject, staff_id,selected_class, selected_section):
    context = {
        'subject' : subject,
        'staff_id': staff_id,
        'selected_class': selected_class,
        'selected_section': selected_section
    }
    return render(request, 'timetable/subject_action.html', context)

def create(request, subject, staff_id, selected_class, selected_section):
    # added these
    if request.method == "POST":
         form = tableForm(request.POST)
         if form.is_valid():
            lesson = form.save()
            messages.success(request, "Lession added successfully!")
            return redirect(reverse("timetable_staff_list",args=(selected_class, selected_section)))
    else:
         print(subject)
         form = tableForm()
    context = {
        'form': form,
        'subject': subject,
        'staff_id':staff_id,
        'selected_class': selected_class,
        'selected_section': selected_section
    }
    return render(request, 'timetable/form.html', context)
"""
def delete_staff(request, subject, staff_id):
    staff = get_object_or_404(CustomUser, staff__id=staff_id)
    staff.delete()
    messages.success(request, "Staff deleted successfully!")
    return redirect(reverse('timetable_staff_list'))
"""

def delete_lession(request, subject, staff_id, selected_class, selected_section):
    staff = get_object_or_404(Staff, id=staff_id)
    
    if request.method == "POST":
        # Delete subjects and time associated with the staff
        staff.creattable_set.filter(subject=subject).delete()
        messages.success(request, "Lession deleted successfully!")
        return redirect(reverse("timetable_staff_list",args=(selected_class, selected_section)))

    
    return redirect(reverse("timetable_staff_list", {'selected_class':selected_class, 'selected_section': selected_section}))

def edit_lession(request, subject, staff_id, selected_class, selected_section):
    # get the lesson object by id or raise 404 if not found
    staff = get_object_or_404(Staff, id=staff_id)
    #lesson = get_object_or_404(CreatTable, subject=subject, staff=staff)
    
    if request.method == "POST":
        # initialize the form with the request data and the lesson object
        form = tableForm(request.POST, instance=staff)
        if form.is_valid():
            # save the updated lesson object
            form.save()
            messages.success(request, "Lesson updated successfully!")
            return redirect(reverse("timetable_staff_list",args=(selected_class, selected_section)))
        else:
            messages.error(request, "Failed to update lesson. Please check the form data.")
    else:
        # initialize the form with the lesson object
        form = tableForm(instance=staff)       
    
    context = {
        'form': form,
        'subject': subject,
        'staff': staff,
        'selected_class' : selected_class,
        'selected_section': selected_section
    }
    return render(request, 'timetable/form.html', context)