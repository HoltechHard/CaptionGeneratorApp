from django.db import models

# Create your models here.

class ImageData(models.Model):
    id_image = models.AutoField(primary_key=True)
    create_time = models.DateField()
    description = models.CharField(max_length=400)
    file_path = models.CharField(max_length=255)

    class Meta:
        db_table = 'ImageData'
