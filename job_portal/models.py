from django.db import models
from django.contrib.auth.models import User

from conf.settings import MEDIA_COMPANY_IMAGE_DIR, MEDIA_SPECIALITY_IMAGE_DIR


class Company (models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    logo = models.ImageField(upload_to=MEDIA_SPECIALITY_IMAGE_DIR, blank=True)
    description = models.TextField()
    employee_count = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="company", blank=True, null=True)

    def __str__(self):
        return self.name


class Specialty(models.Model):
    code = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    picture = models.ImageField(upload_to=MEDIA_SPECIALITY_IMAGE_DIR, blank=True)

    def __str__(self):
        return self.title


class Vacancy(models.Model):
    title = models.CharField(max_length=30)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(max_length=100)
    description = models.TextField()
    salary_min = models.FloatField()
    salary_max = models.FloatField()
    published_at = models.DateField()


class Application(models.Model):
    written_username = models.CharField(max_length=15)
    written_phone = models.CharField(max_length=11)
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="applications")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")
