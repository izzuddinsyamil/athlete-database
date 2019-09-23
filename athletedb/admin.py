from django.contrib import admin
from .models import Sex, Sport, Achievement, Athlete

# pylint: disable=function-redefined
# Register your models here.
@admin.register(Athlete)
class AthleteAdmin(admin.ModelAdmin):
    fields = ('name', 'birth_date', 'phone_number',
              'address', 'sex', 'sports', 'achievements', 'school', 'nik', 'email')


class AthleteAdmin(admin.ModelAdmin):
    exclude = ('age',)


admin.site.register(Sex)
admin.site.register(Sport)
admin.site.register(Achievement)
