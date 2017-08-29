from django.db import models


# Create your models here.
class Player(models.Model):
    """ A model for player data """
    ret_code = models.CharField(max_length=8, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
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


class Park(models.Model):
    """ Model for location data """
    ret_code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=100)
    aka = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    start = models.DateField(auto_now=False, auto_now_add=False)
    end = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return "{} in {}, {}".format(
            self.name,
            self.city,
            self.state
        )
