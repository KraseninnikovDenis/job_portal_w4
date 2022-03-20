from django.forms import ModelForm
from job_portal.models import Application, Company, Vacancy
from django.core.exceptions import ValidationError


class VacancyResponseForm(ModelForm):

    class Meta:
        model = Application
        fields = ('written_username', 'written_phone', 'written_cover_letter')
        labels = {
            'written_username': 'Вас зовут',
            'written_phone': 'Ваш телефон',
            'written_cover_letter': 'Сопроводительное письмо',
        }


class CompanyForm(ModelForm):

    class Meta:
        model = Company
        fields = ('name', 'location', 'description', 'employee_count', 'logo')
        labels = {
            'name': 'Название компании',
            'location': 'География',
            'description': 'Информация о компании',
            'employee_count': 'Количество человек в компании',
            'logo': 'логотип',
        }


class VacancyForm(ModelForm):
    fields = ('title', 'specialty', 'skills', 'description', 'salary_min', 'salary_max')

    class Meta:
        model = Vacancy
        fields = ('title', 'specialty', 'skills', 'description', 'salary_min', 'salary_max')
        labels = {
            'title': 'Название вакансии',
            'specialty': 'Специализация',
            'skills': 'Требуемые навыки',
            'description': 'Описание вакансии',
            'salary_min': 'Зарплата от',
            'salary_max': 'Зарплата до',
        }

    def clean(self):
        vacansy = self.cleaned_data
        if vacansy['salary_min'] > vacansy['salary_max']:
            raise ValidationError('минимальная зарплата не может быть больше максимальной')
