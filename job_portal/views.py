
from urllib import request
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from job_portal.models import Company, Vacancy, Application
from django.utils.html import format_html
from django.views.generic.edit import CreateView, UpdateView
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin


from job_portal.service import \
    create_context_main, create_context_all_vacancy, context_vacancy_one_category_or_404, \
    context_one_companies_or_404, context_one_vacancy_or_404

from job_portal.forms import VacancyResponseForm, CompanyUpdateOrCreateForm


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
    success_url = 'send/'


    def get_context_data(self, **kwargs) :
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

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.vacancy = Vacancy.objects.get(id=self.kwargs['vacancy_id'])
        return super().form_valid(form)


class Company_edit(LoginRequiredMixin, UpdateView):
    template_name = 'job_portal/company-edit.html'
    success_url = '/mycompany/create/success'
    class_form = CompanyUpdateOrCreateForm
    model = Company
    fields = ('name', 'location', 'description', 'employee_count', 'logo')

    def get_object(self):
        try:
            company = Company.objects.get(owner_id=self.request.user.id)
            return company
        except ObjectDoesNotExist:
            return
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


def mycompany(request):
    try:
        Company.objects.get(owner_id=request.user.id)
        return redirect('create/')
    except ObjectDoesNotExist:
        return redirect('letsstart/')


def company_vacancies(request):
    vacancies_in_company_user = Vacancy.objects.filter(company__owner=request.user.id)
    if vacancies_in_company_user:
        return redirect(str(vacancies_in_company_user.id))
    else:
        return redirect('create/')


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
