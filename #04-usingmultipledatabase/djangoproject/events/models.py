from django.db import models

# Create your models here.


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code', max_length=15)
    phone = models.CharField('Contact Phone', max_length=13)
    web = models.URLField('Website Address')
    email_address = models.EmailField('Email Address')

    def __str__(self):
        return self.name


class MyClubUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return "{}. {}-{}".format(self.id, self.first_name, self.last_name)


class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    # will be foreign key in another table (One to Many)
    venue = models.ForeignKey(
        Venue, blank=True, null=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    manager = models.CharField(max_length=160)
    # will be many to many relation with MyClubUser tabel
    attendees = models.ManyToManyField(MyClubUser, blank=True, )

    def __str__(self):
        return "{}. {}".format(self.id, self.name)
