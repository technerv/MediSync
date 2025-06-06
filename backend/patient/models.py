from datetime import datetime
from django.db import models
from authentication.models import CustomUser
from inventory.models import Item, OrderBill

# class ContactDetails(models.Model):
#     tel_no = models.IntegerField()
#     email_address = models.EmailField()
#     residence = models.CharField(max_length=30)

#     def __str__(self):
#         return f"{self.tel_no} - {self.email_address}"

class Patient(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    first_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    second_name = models.CharField(max_length=40)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    insurance = models.ForeignKey("insurance.InsuranceCompany", on_delete=models.SET_NULL, null=True)
    # user_id = models.OneToManyField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name}-{self.second_name}"
    
    @property
    def age(self):
        if self.date_of_birth:
            patient_age:int = (datetime.now().year - self.date_of_birth.year)
            return patient_age
        return None


class NextOfKin(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40)
    second_name = models.CharField(max_length=40)
    relationship = models.CharField(max_length=40)   
    tel_no = models.CharField(max_length=30, null=True, blank=True)
    email_address = models.EmailField(unique=True, null=True, blank=True)
    residence = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f"{self.tel_no} - {self.email_address}"


class Service(models.Model):
    name = models.TextField(max_length=300)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    class Meta:
        ordering = ("-date_created",)

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )
    appointment_date_time = models.DateTimeField(null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    # assigned_doctor = models.ForeignKey("doctor.Doctor", on_delete=models.SET_NULL, null=True, blank=True, related_name='doctor_appointments')
    assigned_doctor = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='pending')
    reason = models.TextField(max_length=300, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    fee = models.CharField(max_length=40, default="0")
    order_bill_ID = models.ForeignKey(
        OrderBill, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Appointment #{self.patient.first_name}"


class PublicAppointment(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    second_name = models.CharField(max_length=40)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,)
    appointment_date_time = models.DateTimeField()
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='pending')
    reason = models.TextField(max_length=300,)
    date_created = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment #{self.first_name}"
    
    @property
    def age(self):
        if self.date_of_birth:
            patient_age:int = (datetime.now().year - self.date_of_birth.year)
            return patient_age
        return None


class Triage(models.Model):
    created_by = models.CharField(max_length=45)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.IntegerField()
    pulse = models.PositiveIntegerField()
    fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.CharField(max_length=300, blank=True)


class Consultation(models.Model):
    DISPOSITION_CHOICES = (
        ('admitted', 'Admitted'),
        ('referred', 'Referred'),
        ('discharged', 'Discharged'),
        ('lab', 'Lab'),
    )
    doctor_ID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    note = models.TextField(null=True, blank=True)
    complaint = models.TextField(null=True, blank=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    disposition = models.CharField(
        max_length=10, choices=DISPOSITION_CHOICES, default="")
    
    def __str__(self):
        return self.note


class Prescription(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('dispensed', 'Dispensed'),
    )
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient_presciptions')
    date_created = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='patient_doctor_prescriptions')
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Prescription #{self.patient_id.pk}"


class PrescribedDrug(models.Model):
    class Meta:
        unique_together = ("prescription_id", "item_ID")

    prescription_id = models.ForeignKey(Prescription, on_delete=models.CASCADE, null=True)
    dosage = models.CharField(max_length=45)
    frequency = models.CharField(max_length=45)
    duration = models.CharField(max_length=45)
    note = models.TextField(null=True, blank=True)
    order_bill_ID = models.ForeignKey(OrderBill, on_delete=models.CASCADE, null=True)
    item_ID = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return f"Prescribed Drug #{self.item_ID}"    
        

class Referral(models.Model):
    SERVICE = (
        ('general', 'General'),
        ('dentist', 'Dentist'),
        ('cardiologist', 'Cardiologist'),
        ('neurologist', 'Neurologist'),
        ('orthopedist', 'Orthopedist'),
        ('psychiatrist', 'Psychiatrist'),
        ('surgeon', 'Surgeon'),
        ('physiotherapist', 'Physiotherapist'),
    )
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    note = models.TextField(null=True, blank=True)
    referred_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    service = models.CharField(max_length=50, choices=SERVICE, default='general')
    email = models.EmailField()

    def __str__(self):
        return f"Referral #{self.patient_id}"
    
    def set_referred_by(self, CustomUser):
        self.referred_by = CustomUser

    def save(self, *args, **kwargs):
        if not self.pk:
            if not self.referred_by:
                raise ValueError("You must set the 'referred_by' user before saving.")
        super().save(*args, **kwargs)