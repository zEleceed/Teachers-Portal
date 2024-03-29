from django.db import models
from django.urls import reverse


# Database Information

class Classroom(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("classroom_detail", kwargs={"pk": self.pk})


class Student(models.Model):
    name = models.CharField(max_length=255)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]  # presents students in alphabetical order

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("classroom_detail", kwargs={"pk": self.classroom.pk})


class Comment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    comment = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("student_detail")
