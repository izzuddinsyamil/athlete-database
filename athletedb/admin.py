from django.contrib import admin
from .models import (Sport,
                     Achievement,
                     Athlete, Event,
                     AchievementList, AchievementMapping)

# pylint: disable=function-redefined
# Register your models here.

class AchievementInline(admin.StackedInline):
    model = Achievement
    extra = 1

@admin.register(Athlete)
class AthleteAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Data Diri', {'fields': ['name', 'nik', 'birth_date', 'birth_place',
              'blood_type', 'phone_number', 'address', 'email',
              'sex', 'school']}),
        ('Cabang Olahraga', {'fields': ['sports']}),
        ('Dokumen', {'fields': ['kk', 'photo', 'ktp']})
    ]
    inlines = [AchievementInline]


class AthleteAdmin(admin.ModelAdmin):
    exclude = ('age', 'BLOOD_TYPES',)


admin.site.register(Sport)