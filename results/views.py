from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, View
from students.models import *
from .forms import CreateResults, EditResults
from .models import Result
from.utils import *

@login_required
def create_result(request):
    students = Student.objects.all()
    if request.method == "POST":

        # after visiting the second page
        if "finish" in request.POST:
            form = CreateResults(request.POST)
            if form.is_valid():
                subjects = form.cleaned_data["subjects"]
                session = form.cleaned_data["session"]
                term = form.cleaned_data["term"]
                students = request.POST["students"]
                results = []
                for student in students.split(","):
                    stu = Student.objects.get(pk=student)
                    if stu.current_class:
                        for subject in subjects:
                            check = Result.objects.filter(
                                session=session,
                                term=term,
                                current_class=stu.current_class,
                                subject=subject,
                                student=stu,
                            ).first()
                            if not check:
                                results.append(
                                    Result(
                                        session=session,
                                        term=term,
                                        current_class=stu.current_class,
                                        subject=subject,
                                        student=stu,
                                    )
                                )

                Result.objects.bulk_create(results)
                return redirect("edit-results")

        # after choosing students
        id_list = request.POST.getlist("students")
        if id_list:
            form = CreateResults(
                initial={
                    "session": request.current_session,
                    "term": request.current_term,
                }
            )
            studentlist = ",".join(id_list)
            return render(
                request,
                "result/create_result_page2.html",
                {"students": studentlist, "form": form, "count": len(id_list)},
            )
        else:
            messages.warning(request, "You didnt select any student.")
    return render(request, "result/create_result.html", {"students": students})


@login_required
def edit_results(request):
    if request.method == "POST":
        form = EditResults(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Results successfully updated")
            return redirect("edit-results")
    else:
        results = Result.objects.filter(
            session=request.current_session, term=request.current_term
        )
        form = EditResults(queryset=results)
    return render(request, "result/edit_results.html", {"formset": form})


class ResultListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        results = Result.objects.filter(
            session=request.current_session, term=request.current_term
        ).order_by('subject__name')
        ##prev session results
        prevresults = Result.objects.filter(
            session__to_date__lte=request.current_session.from_date
        ).exclude(term=request.current_term).order_by('session__to_date').last()
        print(prevresults)
        bulk = {}
        allsubjects=Subject.objects.values("name").order_by("name")
        prevscores=[]
        if prevresults !=None:
            for result in results:
                test_total = 0
                exam_total = 0
                counter=0
                for subject in results:
                    if subject.student == result.student:
                        counter+=int(1)
                        test_total += subject.test_score
                        exam_total += subject.exam_score
            prevscores.append({'student':result.student.id,'score':(test_total + exam_total)/counter})

        ##current score
        for result in results:
            test_total = 0
            exam_total = 0
            subjects = []
            for subject in results:
                if subject.student == result.student:
                    subjects.append(subject)
                    test_total += subject.test_score
                    exam_total += subject.exam_score

            bulk[result.student.id] = {
                "student": result.student,
                "subjects": subjects,
                "allsubjects":allsubjects,
                "test_total": test_total,
                "exam_total": exam_total,
                "total_total": test_total + exam_total,
                "mean_total": (test_total + exam_total)/len(subjects),
                "mean_grade":mean_grade(test_total + exam_total),
                "deviation": (test_total + exam_total)/len(subjects)-prevscores['score'] if len(prevscores) >0 and prevscores['student']==result.student.id else 0
            }

        context = {"results": bulk}
        return render(request, "result/all_results.html", context)

def load_student_card(request):
    return render(request,'result/report-card.html')