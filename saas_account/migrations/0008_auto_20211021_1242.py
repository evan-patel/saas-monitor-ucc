# Generated by Django 3.2.7 on 2021-10-21 12:42

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('saas_account', '0007_alter_slack_active_incidents'),
    ]

    operations = [
        migrations.CreateModel(
            name='Miro',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name=uuid.uuid4)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('indicator', models.CharField(choices=[('major', 'major'), ('minor', 'minor'), ('none', 'none'), ('critical', 'critical')], max_length=20)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('miro_updated_at', models.DateTimeField(null=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='slack',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zoom',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
