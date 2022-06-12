from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Employee


class DateInput(forms.DateInput):
    input_type = "date"


class CreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = (
            "name",
            "sub_name",
            "post",
            "gender",
            "age",
            "birthday",
            "address",
            "phone",
            "assignment",
            "team",
            "license",
            "experience",
            "joined_date",
            "retired_date",
            "evaluation",
            "photo",
        )
        widgets = {
            "birthday": DateInput(),
            "joined_date": DateInput(),
            "retired_date": DateInput(),
        }
        help_texts = {
            "name": "Some useful help text",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Username"
        self.fields["password"].label = "Password"
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs["placeholder"] = field.label
