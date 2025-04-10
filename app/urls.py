from django.urls import path
from . import views

urlpatterns = [
    path("", views.todos, name="todos"),
    path("add", views.todos_add, name="todosAdd"),
    path("delete/<int:id>", views.todos_delete, name="todosDelete"),
    path("check/<int:id>", views.todos_check, name="todosCheck"),
    path("uncheck/<int:id>", views.todos_uncheck, name="todosUncheck")
]