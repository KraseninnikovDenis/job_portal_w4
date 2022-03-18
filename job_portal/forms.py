from django.forms import ModelForm
from job_portal.models import Application, Company


class VacancyResponseForm(ModelForm):

    class Meta:
        model = Application
        fields = ('written_username', 'written_phone', 'written_cover_letter')


class CompanyUpdateOrCreateForm(ModelForm):

    class Meta:
        model = Company
        fields = ('name', 'location', 'description', 'employee_count', 'logo','owner')

