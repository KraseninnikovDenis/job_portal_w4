"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic.base import TemplateView

from accounts.views import RegisterView, AuthorizationView
from job_portal.views.custom_handler import custom_handler404, custom_handler500
from job_portal.views.my_company import MycompanyCreate, CompanyEdit, CompanyLetsstart, Success
from job_portal.views.my_company_vacancies import CompanyVacancies, CompanyVacanciesCreate, CompanyVacanciesEdit
from job_portal.views.public import main, vacancies, \
    category, companies, SelectedVacancy


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', main, name='main'),
    path('vacancies/', vacancies, name='vacancies'),
    path('vacancies/cat/<str:cat>', category, name='category'),
    path('companies/<int:companies_id>', companies, name='companies'),
    path('vacancies/<int:vacancy_id>', SelectedVacancy.as_view(), name='selected_vacancy'),
    path('vacancies/send/', TemplateView.as_view(template_name='job_portal/public/sent.html'), name='vacancies_send'),
    path(
        'vacancies/resending/',
        TemplateView.as_view(template_name='job_portal/public/resending.html'),
        name='vacancies_resending'),

    path('mycompany/', CompanyEdit.as_view(), name='mycompany'),
    path('mycompany/letsstart/', CompanyLetsstart.as_view(), name='company_letsstart'),
    path('mycompany/create/', MycompanyCreate.as_view(), name='company_create'),
    path('mycompany/create/success', Success.as_view(template_name='job_portal/create-or-update-success.html')),

    path('mycompany/vacancies/', CompanyVacancies.as_view(), name='company_vacancies'),
    path('mycompany/vacancies/create/', CompanyVacanciesCreate.as_view(), name='company_vacancies_create'),
    path('mycompany/vacancies/<int:vacancy_id>', CompanyVacanciesEdit.as_view(), name='company_vacancies_update'),
    path('mycompany/vacancies/create/success', Success.as_view(
        template_name='job_portal/create-or-update-success.html',
    )),

    path('login/', AuthorizationView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )

handler404 = custom_handler404
handler500 = custom_handler500
