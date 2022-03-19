from django.forms import ModelForm
from job_portal.models import Application, Company, Vacancy


class VacancyResponseForm(ModelForm):

    class Meta:
        model = Application
        fields = ('written_username', 'written_phone', 'written_cover_letter')


class CompanyUpdateOrCreateForm(ModelForm):

    class Meta:
        model = Company
        fields = ('name', 'location', 'description', 'employee_count', 'logo','owner')


class VacancyUpdateForm(ModelForm):

    class Meta:
        model = Vacancy
        fields = ('title', 'specialty', 'skills', 'description', 'salary_min','salary_max')