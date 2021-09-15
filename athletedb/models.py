from django.db import models
from dateutil.relativedelta import relativedelta
from datetime import datetime
from model_utils import Choices

# Create your models here.


class Sport(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Cabang Olahraga'
        verbose_name_plural = 'Cabang Olahraga'
        db_table = 'public.athletedb_sport'

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
    # year = models.CharField(max_length=255)
    organizer = models.CharField(max_length=255)
    date = models.DateField(default=None, blank=True, null=True)
    # date = models.CharField(max_length=0)
    location = models.CharField(
        max_length=255, default=None, blank=True, null=True)

    class Meta:
        verbose_name = 'Olimpiade'
        verbose_name_plural = 'Olimpiade'
        db_table = 'public.athletedb_event'

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

    class Meta:
        verbose_name = 'Perolehan Medali'
        verbose_name_plural = 'Perolehan Medali'
        db_table = 'public.athletedb_achievementlist'

    @property
    def get_name_titled(self):
        return self.name.title()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.get_name_titled
        super(AchievementList, self).save(*args, **kwargs)


class Athlete(models.Model):
    name = models.CharField(max_length=200, verbose_name='nama')
    nik = models.CharField(
        max_length=255, default=None, blank=True, null=True, unique=True)
    photo = models.ImageField(upload_to='images/pasfoto/',
                              default='images/pasfoto/default_photo.jpg',
                              blank=True, null=True,
                              verbose_name='Pasfoto')
    ktp = models.ImageField(upload_to='images/ktp/',
                            default=None, blank=True, null=True, verbose_name='Foto Ktp')
    kk = models.ImageField(upload_to='images/kartu-keluarga/',
                           default=None, blank=True, null=True,
                           verbose_name='Foto Kartu Keluarga')
    email = models.EmailField(default=None, blank=True, null=True)
    birth_date = models.DateField(
        default=None, blank=True, null=True, verbose_name='tanggal lahir')
    birth_place = models.CharField(
        max_length=255, default=None, blank=True, null=True,
        verbose_name='tempat lahir')
    age = models.IntegerField(default=None, blank=True,
                              null=True, verbose_name='umur')
    BLOOD_TYPES = Choices('A', 'B', 'AB', 'O')
    blood_type = models.CharField(
        choices=BLOOD_TYPES, default=BLOOD_TYPES.A,
        max_length=2, blank=True, null=True, verbose_name='golongan darah')
    phone_number = models.CharField(
        max_length=50, default=None, blank=True, null=True, verbose_name='nomor telepon')
    address = models.CharField(
        max_length=255, default=None, blank=True, null=True, verbose_name='alamat')
    school = models.CharField(
        max_length=255, default=None, blank=True, null=True, verbose_name='sekolah')

    SEXES = Choices('Laki - laki', 'Perempuan')
    sex = models.CharField(
        choices=SEXES, max_length=20,
        blank=True, null=True, verbose_name='Jenis Kelamin'
    )
    sports = models.ManyToManyField(Sport, verbose_name='Cabang Olahraga')

    class Meta:
        verbose_name = 'Atlet'
        verbose_name_plural = 'Atlet'
        db_table = 'public.athletedb_athlete'

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


class Achievement(models.Model):
    # description = models.CharField(
    #     max_length=255, verbose_name='Deskripsi',
    #     default=None, blank=True, null=True)
    description = models.TextField(
        verbose_name='Deskripsi',
        default=None, blank=True, null=True
    )

    RESULTS = Choices('Juara 1', 'Juara 2', 'Juara 3', 'Peserta')
    result = models.CharField(
        choices=RESULTS, max_length=10, verbose_name='Hasil',
        default=None, blank=True, null=True)

    LEVELS = Choices('Tingkat Kota (Porkot)', 'Tingkat Daerah (Porda)',
                     'Tingkat Provinsi (Porprov)', 'Tingkat Nasional (PON)',
                     'Tingkat Dunia (Kejurda)')
    level = models.CharField(
        choices=LEVELS, max_length=255, verbose_name='Tingkat kejuaraan',
        default=None, blank=True, null=True)
    certificate_file = models.ImageField(
        upload_to='images/sertifikat/', blank=True,
        null=True, verbose_name='File sertifikat')
    athlete = models.ForeignKey(
        Athlete, on_delete=models.CASCADE,
        related_name='achievements',
        default=None, blank=True, null=True
    )

    class Meta:
        verbose_name = 'Prestasi'
        verbose_name_plural = 'Prestasi'
        db_table = 'public.athletedb_achievement'

    def __str__(self):
        return "{result}, {level}".format(result=self.result, level=self.level)


class AchievementMapping(models.Model):
    athlete = models.ForeignKey(
        Athlete, related_name='athletes_achievementmapping', on_delete=models.CASCADE)
    event = models.ForeignKey(
        Event, related_name='events_achievementmapping', on_delete=models.CASCADE)
    achievement = models.ForeignKey(
        AchievementList, related_name='achievementlist_achievementmapping',
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Medali Prestasi'
        verbose_name_plural = 'Medali Prestasi'
        db_table = 'public.athletedb_achievementmapping'

    def __str__(self):
        return self.athlete.name


class AthleteSports(models.Model):
    athlete = models.ForeignKey(
        Athlete, related_name='athletes_athletesports', on_delete=models.CASCADE)
    sport = models.ForeignKey(
        Sport, related_name='sports_athletesports', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Olahraga atlit'
        verbose_name_plural = 'Olahraga atlit'
        db_table = 'public.athletedb_athletesports'

    def __str__(self):
        return self.sport.name
