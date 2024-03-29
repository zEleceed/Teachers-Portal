from django.urls import path
from .views import ClassroomListView, ClassroomDetailView, ClassroomCreateView, StudentDetail, StudentCreateView, ClassroomDeleteView, CommentPost


urlpatterns = [
    path("classroom/new/", ClassroomCreateView.as_view(), name="classroom_new"),
    path("classroom/<int:pk>/", ClassroomDetailView.as_view(), name="classroom_detail"),
    path("classroom/<int:pk>/delete/", ClassroomDeleteView.as_view(), name="classroom_delete"),
    path("classroom/student/<int:pk>/", StudentDetail.as_view(), name="student_detail"),
    path("classroom/student/new/", StudentCreateView.as_view(), name="student_new"),
    path("", ClassroomListView.as_view(), name="home"),

]