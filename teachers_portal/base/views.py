from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
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
    model = Student
    template_name = "student_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = self.get_object()
        context['classroom'] = student.classroom
        return context


class StudentCreateView(CreateView):
    model = Student
    template_name = "student_new.html"
    fields = ("name", "classroom",)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentCreateView(CreateView):
    model = Comment
    pass
