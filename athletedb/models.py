from django.db import models
from dateutil.relativedelta import relativedelta
from datetime import datetime

# Create your models here.


class Sex(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Sport(models.Model):
    name = models.CharField(max_length=255)

    @property
    def get_name_titled(self):
        return self.name.title()

    def save(self, *args, **kwargs):
        self.name = self.get_name_titled
        super(Sport, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField(default=None, blank=True, null=True)
    organizer = models.CharField(max_length=255)
    date = models.DateField(default=None, blank=True, null=True)
    location = models.CharField(
        max_length=255, default=None, blank=True, null=True)

    @property
    def get_name_titled(self):
        return self.name.title()

    @property
    def get_organizer_titled(self):
        return self.organizer.title()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.get_name_titled
        self.organizer = self.get_organizer_titled
        super(Event, self).save(*args, **kwargs)


class AchievementList(models.Model):
    name = models.CharField(max_length=255)

    @property
    def get_name_titled(self):
        return self.name.title()

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.name = self.get_name_titled
        super(AchievementList, self).save(*args, **kwargs)


class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    position = models.CharField(max_length=10)
    event = models.ForeignKey(
        Event, related_name='achievements_event',
        on_delete=models.CASCADE, default=None,
        blank=True, null=True)

    @property
    def get_titled_title(self):
        return self.title.title()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.get_titled_title
        super(Achievement, self).save(*args, **kwargs)


class Athlete(models.Model):
    name = models.CharField(max_length=200)
    nik = models.CharField(
        max_length=255, default=None, blank=True, null=True, unique=True)
    email = models.EmailField(default=None, blank=True, null=True)
    birth_date = models.DateField(
        default=None, blank=True, null=True)
    birth_place = models.CharField(
        max_length=255, default='-', blank=True, null=True)
    age = models.IntegerField(default=None, blank=True, null=True)
    phone_number = models.CharField(
        max_length=50, default='-', blank=True, null=True)
    address = models.CharField(
        max_length=255, default='-', blank=True, null=True)
    school = models.CharField(
        max_length=255, default='-', blank=True, null=True)
    sex = models.ForeignKey(
        Sex, related_name='athletes_sex', on_delete=models.CASCADE)
    sports = models.ManyToManyField(Sport)

    def __str__(self):
        return self.name

    @property
    def get_age(self):
        return relativedelta(datetime.today(), self.birth_date).years

    @property
    def get_name_titled(self):
        return self.name.title()

    def save(self, *args, **kwargs):
        self.age = self.get_age
        self.name = self.get_name_titled
        super(Athlete, self).save(*args, **kwargs)


class AchievementMapping(models.Model):
    athlete = models.ForeignKey(
        Athlete, related_name='athletes', on_delete=models.CASCADE)
    event = models.ForeignKey(
        Event, related_name='events', on_delete=models.CASCADE)
    achievement = models.ForeignKey(
        AchievementList, related_name='achievements', on_delete=models.CASCADE)

    def __str__(self):
        return self.athlete.name