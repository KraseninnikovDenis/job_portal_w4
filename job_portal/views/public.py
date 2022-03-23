from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.utils.html import format_html
from django.shortcuts import redirect

from job_portal.forms import VacancyResponseForm
from job_portal.models import Vacancy, Application
from job_portal.service import \
    create_context_main, create_context_all_vacancy, context_vacancy_one_category_or_404, \
    context_one_companies_or_404


def main(request):

    return render(
        request,
        'job_portal/public/index.html',
        context=create_context_main(),
        )


def vacancies(request):

    return render(
        request,
        'job_portal/public/vacancies.html',
        context=create_context_all_vacancy(),
        )


def category(request, cat):

    return render(
        request,
        'job_portal/public/vacancies.html',
        context=context_vacancy_one_category_or_404(cat),
        )


def companies(request, companies_id):

    return render(
        request,
        'job_portal/public/company.html',
        context=context_one_companies_or_404(companies_id),
        )


class SelectedVacancy(CreateView):
    template_name = 'job_portal/public/vacancy.html'
    form_class = VacancyResponseForm
    success_url = 'send/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            vacancy = Vacancy.objects.get(id=self.kwargs['vacancy_id'])
        except ObjectDoesNotExist:
            raise Http404

        description = format_html(vacancy.description)
        context = {
            'vacancy': vacancy,
            'description': description,
        }
        context['form'] = VacancyResponseForm
        return context

    def post(self, request, *args, **kwargs):
        if not Application.objects.filter(user_id=self.request.user.id).exists():
            return super().post(request, *args, **kwargs)
        else:
            return redirect('vacancies_resending')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.vacancy = Vacancy.objects.get(id=self.kwargs['vacancy_id'])
        return super().form_valid(form)
