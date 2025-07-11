# Generated by Django 5.1.6 on 2025-03-04 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_alter_patient_insurance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nextofkin',
            name='contacts',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='user_id',
        ),
        migrations.AddField(
            model_name='nextofkin',
            name='email_address',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='nextofkin',
            name='residence',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='nextofkin',
            name='tel_no',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.DeleteModel(
            name='ContactDetails',
        ),
    ]
