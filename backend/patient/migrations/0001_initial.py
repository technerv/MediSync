# Generated by Django 5.1.6 on 2025-03-01 11:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel_no', models.IntegerField()),
                ('email_address', models.EmailField(max_length=254)),
                ('residence', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
                ('second_name', models.CharField(max_length=40)),
                ('date_of_birth', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True)),
                ('insurance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.insurancecompany')),
                ('user_id', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NextOfKin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('second_name', models.CharField(max_length=40)),
                ('relationship', models.CharField(max_length=40)),
                ('contacts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.contactdetails')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('complaint', models.TextField(blank=True, null=True)),
                ('fee', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('disposition', models.CharField(choices=[('admitted', 'Admitted'), ('referred', 'Referred'), ('discharged', 'Discharged'), ('lab', 'Lab')], default='', max_length=10)),
                ('doctor_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date_time', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='pending', max_length=10)),
                ('reason', models.TextField(max_length=300, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
                ('fee', models.CharField(default='0', max_length=40)),
                ('assigned_doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('item_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.item')),
                ('order_bill_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.orderbill')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('dispensed', 'Dispensed')], default='pending', max_length=10)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_doctor_prescriptions', to=settings.AUTH_USER_MODEL)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_presciptions', to='patient.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('service', models.CharField(choices=[('general', 'General'), ('dentist', 'Dentist'), ('cardiologist', 'Cardiologist'), ('neurologist', 'Neurologist'), ('orthopedist', 'Orthopedist'), ('psychiatrist', 'Psychiatrist'), ('surgeon', 'Surgeon'), ('physiotherapist', 'Physiotherapist')], default='general', max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
                ('referred_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PublicAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
                ('second_name', models.CharField(max_length=40)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=10)),
                ('appointment_date_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='pending', max_length=10)),
                ('reason', models.TextField(max_length=300)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.service')),
            ],
        ),
        migrations.CreateModel(
            name='Triage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=45)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('weight', models.IntegerField()),
                ('pulse', models.PositiveIntegerField()),
                ('fee', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('notes', models.CharField(blank=True, max_length=300)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
        migrations.CreateModel(
            name='PrescribedDrug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dosage', models.CharField(max_length=45)),
                ('frequency', models.CharField(max_length=45)),
                ('duration', models.CharField(max_length=45)),
                ('note', models.TextField(blank=True, null=True)),
                ('item_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.item')),
                ('order_bill_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.orderbill')),
                ('prescription_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.prescription')),
            ],
            options={
                'unique_together': {('prescription_id', 'item_ID')},
            },
        ),
    ]
