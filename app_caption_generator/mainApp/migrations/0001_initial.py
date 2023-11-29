# Generated by Django 4.2.2 on 2023-11-28 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ImageData",
            fields=[
                (
                    "id_image",
                    models.AutoField(
                        default="nextval('\"ImageData_id_image_seq\"'::regclass)",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("create_time", models.DateField()),
                ("description", models.CharField(max_length=400)),
                ("file_path", models.CharField(max_length=255)),
            ],
            options={"db_table": "ImageData",},
        ),
    ]