from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        from job_portal.models import Company, Specialty, Vacancy

        Company.objects.all().delete()
        Specialty.objects.all().delete()
        Vacancy.objects.all().delete()
