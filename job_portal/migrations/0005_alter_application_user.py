# Generated by Django 4.0.3 on 2022-03-22 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job_portal', '0004_alter_company_logo_alter_specialty_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='user',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='applications',
                to=settings.AUTH_USER_MODEL),
        ),
    ]
