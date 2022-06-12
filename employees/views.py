from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy

from .models import Employee
from .forms import CreateForm, LoginForm

import logging

logger = logging.getLogger(__name__)


class LoginView(LoginView):
    template_name = "login.html"
    form_class = LoginForm


class LogoutView(LogoutView):
    template_name = "login.html"


class ListView(LoginRequiredMixin, generic.ListView):
    model = Employee
    template_name = "list.html"
    login_url = "/login/"

    def get_queryset(self):
        return Employee.objects.order_by("-created_at")


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Employee
    template_name = "detail.html"


class CreateView(LoginRequiredMixin, generic.CreateView):
    model = Employee
    template_name = "create.html"
    form_class = CreateForm
    success_url = reverse_lazy("employees:list")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "プロフィールを作成しました。")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "プロフィールの作成に失敗しました。")
        return super().form_invalid(form)


class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Employee
    template_name = "update.html"
    form_class = CreateForm

    def get_success_url(self):
        return reverse_lazy("employees:detail", kwargs={"pk": self.kwargs["pk"]})

    def form_valid(self, form):
        messages.success(self.request, "プロフィールを更新しました。")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "プロフィールの更新に失敗しました。")
        return super().form_invalid(form)


class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Employee
    template_name = "delete.html"
    success_url = reverse_lazy("employees:list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "プロフィールを削除しました。")
        return super().delete(request, *args, **kwargs)
