from django.db import models


# Create your models here.
class Player(models.Model):
    """ A model for player data """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    ret_code = models.CharField(max_length=8, unique=True)
    debut = models.DateField()
    # throws = models.CharField(max_length=1, blank=True)
    # bats = models.CharField(max_length=1, blank=True)
    # position = models.ManyToManyField("position", blank=True)
    # slug = models.SlugField(
    #     max_length=50,
    #     unique=True,
    #     help_text='A label for URL config')

    def __str__(self):
        return "{} {}".format(
            self.first_name,
            self.last_name)

    """ Ordering is not working (names like De la Rosa being
    sorted after z I believe it is an SQLite issue) """
    # class Meta:
    #     ordering = ['last_name', 'first_name']
