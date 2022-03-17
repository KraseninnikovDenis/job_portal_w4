from django.forms import ModelForm
from job_portal.models import Application


class VacancyResponseForm(ModelForm):

    class Meta:
        model = Application
        fields = ('written_username', 'written_phone', 'written_cover_letter')