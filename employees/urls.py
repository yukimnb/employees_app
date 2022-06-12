from django.urls import path

from . import views


app_name = "employees"
urlpatterns = [
    path("", views.ListView.as_view(), name="list"),
    path("detail/<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("create/", views.CreateView.as_view(), name="create"),
    path("update/<int:pk>/", views.UpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", views.DeleteView.as_view(), name="delete"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]
