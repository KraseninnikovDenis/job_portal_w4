from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        from job_portal.models import Company, Specialty, Vacancy
        from job_portal.data import jobs, companies, specialties

        from datetime import datetime

        for specialty in specialties:
            Specialty.objects.create(
                code=specialty.get('code'),
                title=specialty.get('title'),
                )

        for company in companies:
            Company.objects.create(
                id=company.get('id'),
                name=company.get('title'),
                location=company.get('location'),
                description=company.get('description'),
                employee_count=company.get('employee_count'),
                )

        for job in jobs:
            Vacancy.objects.create(
                id=job.get('id'),
                title=job.get('title'),
                specialty=Specialty.objects.get(code=job.get('specialty')),
                company=Company.objects.get(id=int(job.get('company'))),
                skills=job.get('skills'),
                description=job.get('description'),
                salary_min=float(job.get('salary_from')),
                salary_max=float(job.get('salary_to')),
                published_at=datetime.strptime(job.get('posted'), '%Y-%m-%d'),
            )
