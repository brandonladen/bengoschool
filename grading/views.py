from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect,render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import *
from .forms import *

###########################Grading##############################
class GradingListView(LoginRequiredMixin, ListView):
    model = GradingRules


class GradingCreateView(LoginRequiredMixin, CreateView):
    model = GradingLevel
    fields = "__all__"
    success_url = "/grading/rules/list"

    def get_context_data(self, **kwargs):
        context = super(GradingCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["items"] = GradingItemFormset(
                self.request.POST, prefix="gradingitem_set"
            )
        else:
            context["items"] = GradingItemFormset(prefix="gradingitem_set")
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context["items"]
        print(form)
        self.object = form.save()
        if self.object.id != None:
            if form.is_valid() and formset.is_valid():
                formset.instance = self.object
                formset.save()
        return super().form_valid(form)

class GradingDetailView(LoginRequiredMixin, DetailView):
    model = GradingLevel
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super(GradingDetailView, self).get_context_data(**kwargs)
        context["items"] = GradingRules.objects.filter(grading_level=self.object)
        return context


class GradingUpdateView(LoginRequiredMixin, UpdateView):
    model = GradingLevel
    fields = fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super(GradingUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["items"] = GradingItemFormset(
                self.request.POST, instance=self.object
            )
        else:
            context["items"] = GradingItemFormset(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        itemsformset = context["items"]
        if form.is_valid() and itemsformset.is_valid():
            form.save()
            itemsformset.save()
        return super().form_valid(form)


class GradingDeleteView(LoginRequiredMixin, DeleteView):
    model = GradingLevel
    success_url = reverse_lazy("grading-list")

###########################Overall Grading##############################
class OverallGradingListView(LoginRequiredMixin, ListView):
    model = OveralGradingItem


class OverallGradingCreateView(LoginRequiredMixin, CreateView):
    model = OverallGrading
    fields = "__all__"
    success_url = "/grading/overal/list"

    def get_context_data(self, **kwargs):
        context = super(OverallGradingCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["items"] = OverallGradingFormSet(
                self.request.POST, prefix="overalgradingitem_set"
            )
        else:
            context["items"] = OverallGradingFormSet(prefix="overalgradingitem_set")
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context["items"]
        print(form)
        self.object = form.save()
        if self.object.id != None:
            if form.is_valid() and formset.is_valid():
                formset.instance = self.object
                formset.save()
        return super().form_valid(form)

class OverallGradingDetailView(LoginRequiredMixin, DetailView):
    model = OverallGrading
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super(OverallGradingDetailView, self).get_context_data(**kwargs)
        context["items"] = OveralGradingItem.objects.filter(overall_grading=self.object)
        return context


class OverallGradingUpdateView(LoginRequiredMixin, UpdateView):
    model = OverallGrading
    fields = fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super(OverallGradingUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["items"] = OverallGradingFormSet(
                self.request.POST, instance=self.object
            )
        else:
            context["items"] = OverallGradingFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        itemsformset = context["items"]
        if form.is_valid() and itemsformset.is_valid():
            form.save()
            itemsformset.save()
        return super().form_valid(form)


class OverallGradingDeleteView(LoginRequiredMixin, DeleteView):
    model = OverallGrading
    success_url = reverse_lazy("overallgrading-list")

##########################Grades################################################

class GradesListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Grades
    template_name = "grading/grades_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = GradesForm()
        return context


class GradesCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Grades
    form_class = GradesForm
    template_name = "grading/mgt_form.html"
    success_url = reverse_lazy("grades-list")
    success_message = "New Grades successfully added"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add new Grades"
        return context


class GradesUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Grades
    form_class = GradesForm
    success_url = reverse_lazy("grades-list")
    success_message = "Grades successfully updated."
    template_name = "grading/mgt_form.html"

    def form_valid(self, form):
        return super().form_valid(form)


class GradesDeleteView(LoginRequiredMixin, DeleteView):
    model = Grades
    success_url = reverse_lazy("grades-list")
    template_name = "grading/core_confirm_delete.html"
    success_message = "The Grades {} has been deleted with all its attached content"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message.format(obj.name))
        return super(GradesDeleteView, self).delete(request, *args, **kwargs)

#############################Grading LEvel###########################################
class GradingLevelListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = GradingLevel
    template_name = "grading/gradinglevel_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = GradingLevelForm()
        return context


class GradingLevelCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = GradingLevel
    form_class = GradingLevelForm
    template_name = "grading/mgt_form.html"
    success_url = reverse_lazy("gradinglevel-list")
    success_message = "New GradingLevel successfully added"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add new GradingLevel"
        return context


class GradingLevelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = GradingLevel
    form_class = GradingLevelForm
    success_url = reverse_lazy("gradinglevel-list")
    success_message = "GradingLevel successfully updated."
    template_name = "grading/mgt_form.html"

    def form_valid(self, form):
        obj = self.object
        if obj.current == False:
            terms = (
                GradingLevel.objects.filter(current=True)
                .exclude(name=obj.name)
                .exists()
            )
            if not terms:
                messages.warning(
                    self.request, "You must set a GradingLevel to current.")
                return redirect("gradinglevel-list")
        return super().form_valid(form)


class GradingLevelDeleteView(LoginRequiredMixin, DeleteView):
    model = GradingLevel
    success_url = reverse_lazy("gradinglevel-list")
    template_name = "grading/core_confirm_delete.html"
    success_message = "The GradingLevel {} has been deleted with all its attached content"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.current == True:
            messages.warning(
                request, "Cannot delete GradingLevel as it is set to current")
            return redirect("gradinglevel-list")
        messages.success(self.request, self.success_message.format(obj.name))
        return super(GradingLevelDeleteView, self).delete(request, *args, **kwargs)

class CurrentGradingLevelView(LoginRequiredMixin, View):
    """Current SEssion and Term"""
    form_class = CurrentLevelForm
    template_name = "grading/current_level.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(
            initial={
                "current_level": GradingLevel.objects.get(current=True),
            }
        )
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_Class(request.POST)
        if form.is_valid():
            level = form.cleaned_data["current_level"]
            GradingLevel.objects.filter(name=level).update(current=True)
            GradingLevel.objects.exclude(name=level).update(current=False)
        return render(request, self.template_name, {"form": form})