# Generated by Django 4.2.3 on 2023-07-04 19:37

from django.db import migrations, models
import django_registries.registry.Registry


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Foo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "foo_type",
                    django_registries.registry.Registry.ChoicesField(max_length=100),
                ),
            ],
        ),
    ]