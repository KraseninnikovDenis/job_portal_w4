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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from job_portal.views import \
    main, vacancies, category, companies, \
    Selected_vacancy, custom_handler404, custom_handler500, \
    Vacancies_send, Company_letsstart, Company_create, Mycompany, \
    Company_vacancies, Company_vacancies_create, Company_vacancies_edit
from accounts.views import RegisterView, AuthorizationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('vacancies/', vacancies, name='vacancies'),
    path('vacancies/cat/<str:cat>', category, name='category'),
    path('companies/<int:id>', companies, name='companies'),
    path('vacancies/<int:vacancy_id>', Selected_vacancy.as_view(), name='selected_vacancy'),
    path('vacancies/<int:pk>/send/', Vacancies_send.as_view(), name='vacancies_send'),
    path('mycompany/letsstart/', Company_letsstart.as_view(), name='company_letsstart'),
    path('mycompany/create/', Company_create.as_view(), name='company_create'),
    path('mycompany/', Mycompany.as_view(), name='mycompany'),
    path('mycompany/vacancies/', Company_vacancies.as_view(), name='company_vacancies'),
    path('mycompany/vacancies/create/', Company_vacancies_create.as_view(), name='company_vacancies_create'),
    path('mycompany/vacancies/<int:id>', Company_vacancies_edit.as_view(), name='one_company_vacancy'),
    path('login/', AuthorizationView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)

handler404 = custom_handler404
handler500 = custom_handler500
