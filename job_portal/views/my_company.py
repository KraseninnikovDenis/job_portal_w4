
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from job_portal.forms import CompanyForm
from job_portal.models import Company


class MycompanyCreate(LoginRequiredMixin, CreateView):
    template_name = 'job_portal/my_company/company-edit.html'
    form_class = CompanyForm
    success_url = '/mycompany/create/success'

    def get(self, request, *args, **kwargs):
        try:
            Company.objects.get(owner_id=request.user.id)
            return redirect('/mycompany/')
        except ObjectDoesNotExist:
            return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CompanyEdit(LoginRequiredMixin, UpdateView):
    template_name = 'job_portal/my_company/company-edit.html'
    success_url = '/mycompany/create/success'
    form_class = CompanyForm

    def get(self, request, *args, **kwargs):
        try:
            Company.objects.get(owner_id=request.user.id)
        except ObjectDoesNotExist:
            return redirect('letsstart/')
        return super().get(request, *args, **kwargs)

    def get_object(self):
        company = Company.objects.get(owner_id=self.request.user.id)
        return company

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CompanyLetsstart(LoginRequiredMixin, TemplateView):
    template_name = 'job_portal/my_company/company-create.html'


class Success(LoginRequiredMixin, TemplateView):
    pass
