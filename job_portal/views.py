
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from job_portal.models import Vacancy, Application
from django.utils.html import format_html
from django.views.generic.edit import CreateView
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404


from job_portal.service import \
    create_context_main, create_context_all_vacancy, context_vacancy_one_category_or_404, \
    context_one_companies_or_404, context_one_vacancy_or_404

from job_portal.forms import VacancyResponseForm


def main(request):

    return render(
        request,
        'job_portal/index.html',
        context=create_context_main(),
        )


def vacancies(request):

    return render(
        request,
        'job_portal/vacancies.html',
        context=create_context_all_vacancy(),
        )


def category(request, cat):

    return render(
        request,
        'job_portal/vacancies.html',
        context=context_vacancy_one_category_or_404(cat),
        )


def companies(request, companies_id):

    return render(
        request,
        'job_portal/company.html',
        context=context_one_companies_or_404(companies_id),
        )

    
class Selected_vacancy(CreateView):
    template_name = 'job_portal/vacancy.html'
    model = Application
    form_class = VacancyResponseForm
    success_url = ''


    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        try:
            vacancy = Vacancy.objects.get(id=self.kwargs['vacancy_id'])
        except ObjectDoesNotExist:
            raise Http404

        description = format_html(vacancy.description)

        context = {
            'vacancy': vacancy,
            'description': description
        }
        context['form'] = VacancyResponseForm
        return context

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print(request.user.id)
            Application.objects.create(
                written_username=request.POST.get('written_username'),
                written_phone=request.POST.get('written_phone'),
                written_cover_letter=request.POST.get('written_cover_letter'),
                vacancy=Vacancy.objects.get(id=self.kwargs['vacancy_id']),
                user_id=request.user.id,
            )
        return super().post(request, *args, **kwargs)


class Vacancies_send(DetailView):
    template_name = 'job_portal/sent.html'


class Company_letsstart(TemplateView):
    template_name = 'job_portal/company-create.html'


class Company_create(TemplateView):
    template_name = 'job_portal/company-edit.html'

class Mycompany(TemplateView):
    template_name = 'job_portal/company-edit.html'


class Company_vacancies(TemplateView):
    template_name = 'job_portal/vacancy-list.html'


class Company_vacancies_create(TemplateView):
    template_name = 'job_portal/vacancy-edit.html'


class Company_vacancies_edit(TemplateView):
    template_name = 'job_portal/vacancy-edit.html'    


def custom_handler404(request, exception):
    return HttpResponseNotFound('Страница не найдена')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера')
