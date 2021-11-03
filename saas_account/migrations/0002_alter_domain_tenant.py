# Generated by Django 3.2.7 on 2021-10-06 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saas_account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='tenant',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='domains', to='saas_account.client'),
        ),
    ]