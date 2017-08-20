from django.db import models


# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    ret_code = models.CharField(max_length=8, unique=True)
    # slug = models.SlugField(
    #     max_length=50,
    #     unique=True,
    #     help_text='A label for URL config')

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        ordering = ['last_name']
