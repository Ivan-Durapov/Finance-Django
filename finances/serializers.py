from rest_framework import serializers

from .models import Category, Table, Transaction


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"
        read_only_fields = ("user",)


class TransactionSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Category.objects.all()
    )

    class Meta:
        model = Transaction
        fields = ["id", "table", "categories", "amount", "currency", "date"]
