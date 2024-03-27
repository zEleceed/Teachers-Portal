from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Classroom, Student


# Create your views here.

class ClassroomListView(LoginRequiredMixin, ListView):
    model = Classroom
    template_name = "home.html"


class ClassroomDetailView(LoginRequiredMixin, DetailView):
    model = Classroom
    template_name = "post_detail.html"


class ClassroomCreateView(LoginRequiredMixin, CreateView):
    model = Classroom
    template_name = "classroom_new.html"
    fields = ("title", "body")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class StudentDetail(DetailView):
    model = Student
    template_name = "student_detail.html"


class StudentCreateView(CreateView):
    model = Student
    template_name = "student_new.html"
    fields = ("name","classroom",)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
