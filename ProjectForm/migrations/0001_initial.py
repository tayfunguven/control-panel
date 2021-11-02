# Generated by Django 3.1.7 on 2021-08-18 12:19

import ProjectForm.models
import datetime
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('dealer_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Bayi ID')),
                ('dealer_name', models.CharField(max_length=200, verbose_name='Bayi')),
            ],
            options={
                'verbose_name': 'Bayi',
                'verbose_name_plural': 'Bayiler',
            },
        ),
        migrations.CreateModel(
            name='RegisterDeal',
            fields=[
                ('deal_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Anlaşma ID')),
                ('project_name', models.CharField(max_length=250, verbose_name='Proje Adı')),
                ('project_date', models.DateField(default=datetime.date(2021, 8, 18), validators=[ProjectForm.models.RegisterDeal.validate_initial_date], verbose_name='Anlaşma Tarihi')),
                ('estimated_date', models.DateField(default=datetime.date(2021, 8, 18), validators=[ProjectForm.models.RegisterDeal.validate_date], verbose_name='Tahmini Teslim Tarihi')),
                ('project_time', models.IntegerField(verbose_name='Proje Süresi')),
                ('user', models.CharField(default=django.contrib.auth.models.User, max_length=100, verbose_name='Düzenleyen')),
                ('project_status', models.CharField(choices=[('takipte', 'Takipte'), ('tamamlandi', 'Tamamlandı'), ('takipsiz', 'Takipsiz')], default='takipte', max_length=150, verbose_name='İlerleme Durumu')),
                ('project_description', models.TextField(verbose_name='Açıklama')),
                ('company', models.CharField(max_length=150, verbose_name='Kurum Adı')),
                ('company_address', models.TextField(verbose_name='Kurum Adresi')),
                ('contact_name', models.CharField(max_length=150, verbose_name='Ad')),
                ('contact_surname', models.CharField(max_length=150, verbose_name='Soyad')),
                ('contact_phone', models.CharField(max_length=15, verbose_name='Telefon')),
                ('contact_email', models.CharField(max_length=150, verbose_name='E-posta')),
            ],
            options={
                'verbose_name': 'Anlaşma Kaydı',
                'verbose_name_plural': 'Anlaşma Kayıtları',
            },
        ),
        migrations.CreateModel(
            name='DealerUser',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Bayi ID')),
                ('user', models.CharField(default=django.contrib.auth.models.User, max_length=200, verbose_name='Kullanıcı')),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dealers', to='ProjectForm.dealer', verbose_name='Bayi')),
            ],
            options={
                'verbose_name': 'Bayi Kullanıcısı',
                'verbose_name_plural': 'Bayi Kullanıcıları',
            },
        ),
    ]