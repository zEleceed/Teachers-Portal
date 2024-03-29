from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import SingleObjectMixin
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .forms import CommentForm
from .models import Classroom, Student, Comment


# Classroom Views.
class ClassroomListView(LoginRequiredMixin, ListView):
    model = Classroom
    template_name = "home.html"


class ClassroomDetailView(LoginRequiredMixin, DetailView):
    model = Classroom
    template_name = "classroom_detail.html"


class ClassroomCreateView(LoginRequiredMixin, CreateView):
    model = Classroom
    template_name = "classroom_new.html"
    fields = ("title", "body")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ClassroomDeleteView(LoginRequiredMixin, DeleteView):
    model = Classroom
    template_name = "classroom_delete.html"
    success_url = reverse_lazy("home")


################################## Student Views Start ########################################
class StudentDetail(DetailView):
    # Student View is going to handle both POST and GET request to allow comments in
    model = Student
    template_name = "student_detail.html"

    # Get Request Method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = self.get_object()
        context["form"] = CommentForm()
        context['classroom'] = student.classroom
        return context

    # Post Reques Method
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.student = self.object
            comment.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            context = self.get_context_data(form=form)
            return self.render_to_response(context)

    def get_success_url(self):
        return reverse("student_detail", kwargs={"pk": self.object.pk})


class StudentCreateView(CreateView):
    model = Student
    template_name = "student_new.html"
    fields = ("name", "classroom",)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentPost(SingleObjectMixin, FormView):
    model = Student
    form_class = CommentForm
    template_name = "student_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.student = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        student = self.object
        return reverse("student_detail", kwargs={"pk": student.pk})
