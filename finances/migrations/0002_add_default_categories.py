from django.db import migrations


def create_default_categories(apps, schema_editor):
    Category = apps.get_model("finances", "Category")
    default_categories = ["Продукти", "Авто", "Одяг"]

    for category_name in default_categories:
        Category.objects.get_or_create(name=category_name)


class Migration(migrations.Migration):

    dependencies = [
        ("finances", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_default_categories),
    ]
