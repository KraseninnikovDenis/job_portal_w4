from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.utils.html import format_html

from job_portal.models import Company, Specialty, Vacancy


def create_context_main():
    specialty = Specialty.objects.annotate(vacancies_count=Count('vacancies'))
    company = Company.objects.annotate(vacancies_count=Count('vacancies'))

    return {
        'specialty': specialty,
        'company': company,
        }


def create_context_all_vacancy():
    vacancy = Vacancy.objects.annotate(count=Count('id'))

    return {
        'vacancy': vacancy,
        }


def context_vacancy_one_category_or_404(cat):
    try:
        specialty = Specialty.objects.get(code=cat)
    except ObjectDoesNotExist:
        raise Http404

    vacancy = Vacancy.objects.filter(specialty__code=cat).annotate(count=Count('id'))

    return {
        'vacancy': vacancy,
        'specialty': specialty.title,
        }


def context_one_companies_or_404(companies_id):
    try:
        company = Company.objects.get(id=companies_id)
    except ObjectDoesNotExist:
        raise Http404

    vacancy = Vacancy.objects.filter(company__id=companies_id).annotate(count=Count('id'))
    return {
        'vacancy': vacancy,
        'company': company,
        }


def context_one_vacancy_or_404(vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except ObjectDoesNotExist:
        raise Http404

    description = format_html(vacancy.description)

    return {
        'vacancy': vacancy,
        'description': description,
        }
