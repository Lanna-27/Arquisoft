from django.db import models

class Category(models.Model):

    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    description = models.TextField(max_length = 200)

    class Meta:
        app_label = 'swarch2024i_ms'
