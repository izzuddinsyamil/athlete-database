from django.contrib import admin
from .models import (Sport,
                     Achievement,
                     Athlete, Event,
                     AchievementList, AchievementMapping)

# pylint: disable=function-redefined
# Register your models here.


@admin.register(Athlete)
class AthleteAdmin(admin.ModelAdmin):
    fields = ('name', 'nik', 'photo', 'ktp', 'kk', 'birth_date', 'birth_place',
              'blood_type', 'phone_number', 'address', 'email',
              'sex', 'school', 'sports')


class AthleteAdmin(admin.ModelAdmin):
    exclude = ('age', 'BLOOD_TYPES',)


admin.site.register(Sport)
# admin.site.register(Achievement)
admin.site.register(Event)
admin.site.register(AchievementList)
admin.site.register(AchievementMapping)
