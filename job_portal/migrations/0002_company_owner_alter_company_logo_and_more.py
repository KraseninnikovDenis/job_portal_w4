# Generated by Django 4.0.3 on 2022-03-13 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job_portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, upload_to='speciality_images'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='code',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='picture',
            field=models.ImageField(blank=True, upload_to='speciality_images'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='title',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='published_at',
            field=models.DateField(),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('written_username', models.CharField(max_length=15)),
                ('written_phone', models.CharField(max_length=11)),
                ('written_cover_letter', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL)),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='job_portal.vacancy')),
            ],
        ),
    ]
