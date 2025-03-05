from django import forms

from .models import Category, Table, Transaction


class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ["name", "currency"]
        label = {
            "name": "Назва",
            "currency": "Валюта",
        }


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["amount", "currency", "categories", "description", "table"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields["table"].queryset = Table.objects.filter(user=user)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields["user"].initial = user
