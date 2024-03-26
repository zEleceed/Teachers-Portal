from django.urls import path
from .views import ClassroomListView, ClassroomDetailView, ClassroomCreateView


urlpatterns = [
    path("classroom/new/", ClassroomCreateView.as_view(), name="classroom_new"),
    path("classroom/<int:pk>/", ClassroomDetailView.as_view(), name="post_detail"),
    path("", ClassroomListView.as_view(), name="home"),

]