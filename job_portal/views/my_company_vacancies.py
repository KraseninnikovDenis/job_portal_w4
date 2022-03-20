from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import Http404
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from job_portal.forms import VacancyForm
from job_portal.models import Company, Vacancy, Application


class CompanyVacancies(LoginRequiredMixin, ListView):
    model = Vacancy
    template_name = 'job_portal/my_company_vacansies/vacancy-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacancy'] = Vacancy.objects.filter(company__owner=self.request.user.id)
        return context


class CompanyVacanciesCreate(LoginRequiredMixin, CreateView):
    template_name = 'job_portal/my_company_vacansies/vacancy-edit.html'
    form_class = VacancyForm
    success_url = '/mycompany/vacancies/create/success'

    def form_valid(self, form):
        form.instance.company = Company.objects.get(owner_id=self.request.user.id)
        return super().form_valid(form)


class CompanyVacanciesEdit(LoginRequiredMixin, UpdateView):
    template_name = 'job_portal/my_company_vacansies/vacancy-edit.html'
    form_class = VacancyForm
    success_url = '/mycompany/vacancies/create/success'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['application'] = Application.objects.filter(
            vacancy__id=self.kwargs['vacancy_id']).annotate(count=Count('id'))
        return context

    def get_object(self):
        try:
            vacancy = Vacancy.objects.filter(company__owner=self.request.user).get(id=self.kwargs['vacancy_id'])
        except ObjectDoesNotExist:
            raise Http404
        return vacancy
