# Generated by Django 3.2.7 on 2021-10-08 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saas_account', '0002_alter_domain_tenant'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='site_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
