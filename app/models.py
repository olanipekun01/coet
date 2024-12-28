from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now

# Create your models here.
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # date_joined = models.DateTimeField(auto_now_add=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.username
        
    def set_password(self, raw_password):
        """Hash and set the password."""
        self.password = make_password(raw_password)
        self.save()
        
    def check_password(self, raw_password):
        """Check the password against the stored hashed password."""
        return check_password(raw_password, self.password)
    
class Session(models.Model):
    year = models.CharField(max_length=500)  # e.g., '2023/2024'
    is_current = models.BooleanField(default=False)  # Marks current active session

    def save(self, *args, **kwargs):
        if self.is_current:
            # Uncheck `is_current` for all other Semester objects
            Session.objects.filter(is_current=True).exclude(id=self.id).update(is_current=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.year
    
    

class College(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=True, null=True, max_length=500)

    def __str__(self):
        return self.name
    
class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=True, null=True, max_length=500)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Programme(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=True, null=True, max_length=500)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    duration = models.IntegerField(blank=True, null=True)
    degree = models.CharField(blank=True, null=True, max_length=50)

    def __str__(self):
        return self.name

class Application(models.Model):
    applicant = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='application')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved')], default='pending')
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True, default=None)
    
    def __str__(self):
        return f"Application - {self.applicant.username}"

class Instructor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    position = models.CharField(blank=True, null=True, max_length=500)
    departmental_email = models.CharField(blank=True, null=True, max_length=90)

    def __str__(self):
        return self.position

class PersonalDetails(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    DENOMINATION_CHOICES = [
        ('christian', 'Christian'),
        ('muslim', 'Muslim'),
        ('traditional', 'Traditional'),
    ]

    PROGRAM_CHOICES = [
        ('electricalElectronicsEngineering', 'B.Eng. Electrical & Electronics Engineering'),
        ('computerEngineering', 'B.Eng. Computer Engineering'),
        ('mechatronicsEngineering', 'B.Eng. Mechatronics Engineering'),
        ('mechanicalEngineering', 'B.Eng. Mechanical Engineering'),
        ('biomedicalEngineering', 'B.Eng. Biomedical Engineering'),
        ('civilEnvironmentalEngineering', 'B.Eng. Civil and Environmental Engineering'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    applicant = models.OneToOneField(Application, on_delete=models.CASCADE, related_name='personal_details', default=None)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=150, blank=True, null=True)
    state_of_origin = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=100,blank=True, null=True)
    local_government_area = models.CharField(max_length=100, blank=True, null=True)
    denomination = models.CharField(max_length=15, choices=DENOMINATION_CHOICES, blank=True, null=True)
    address = models.TextField( blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    desired_program = models.ForeignKey(Programme, on_delete=models.CASCADE, null=True, default=None)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

class ParentsGuardian(models.Model):
    # Father's Information
    father_surname = models.CharField(max_length=100, blank=True, null=True)
    father_first_name = models.CharField(max_length=100, blank=True, null=True)
    father_other_name = models.CharField(max_length=100, blank=True, null=True)
    father_occupation = models.CharField(max_length=200, blank=True, null=True)
    father_place_of_work = models.CharField(max_length=200, blank=True, null=True)
    father_telephone = models.CharField(max_length=15, blank=True, null=True)
    father_email = models.EmailField(blank=True, null=True)

    # Mother's Information
    mother_surname = models.CharField(max_length=100, blank=True, null=True)
    mother_first_name = models.CharField(max_length=100, blank=True, null=True)
    mother_other_name = models.CharField(max_length=100, blank=True, null=True)
    mother_occupation = models.CharField(max_length=200, blank=True, null=True)
    mother_place_of_work = models.CharField(max_length=200, blank=True, null=True)
    mother_telephone = models.CharField(max_length=15, blank=True, null=True)
    mother_email = models.EmailField(blank=True, null=True)

    # Guardian's Information
    guardian_surname = models.CharField(max_length=100, blank=True, null=True)
    guardian_first_name = models.CharField(max_length=100, blank=True, null=True)
    guardian_other_name = models.CharField(max_length=100, blank=True, null=True)
    guardian_occupation = models.CharField(max_length=200, blank=True, null=True)
    guardian_place_of_work = models.CharField(max_length=200, blank=True, null=True)
    guardian_telephone = models.CharField(max_length=15, blank=True, null=True)
    guardian_email = models.EmailField(blank=True, null=True)

    applicant = models.OneToOneField(Application, on_delete=models.CASCADE, related_name='parents_guardian', default=None)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True, default=None)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Parents/Guardian Info - ID {self.id}"

class Sponsor(models.Model):
    # Name of Sponsor
    surname = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    other_name = models.CharField(max_length=100, blank=True, null=True)

    # Occupation and Place of Work
    occupation = models.CharField(max_length=200, blank=True, null=True)
    place_of_work = models.CharField(max_length=200, blank=True, null=True)

    # Contact Information
    telephone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    applicant = models.OneToOneField(Application, on_delete=models.CASCADE, related_name='sponsor', default=None)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True, default=None)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.surname} {self.first_name}"

class ModeOfEntry(models.Model):
    ENTRY_MODES = [
        ('UTME', 'UTME'),
        ('DIRECT ENTRY', 'Direct Entry'),
    ]

    # Basic Fields
    entry_mode = models.CharField(max_length=20, choices=ENTRY_MODES)
    jamb_reg_number = models.CharField(max_length=20, unique=True)
    
    # UTME Subjects and Scores
    subject1 = models.CharField(max_length=100, default="Use of English")
    score1 = models.IntegerField()
    subject2 = models.CharField(max_length=100, blank=True, null=True)
    score2 = models.IntegerField(blank=True, null=True)
    subject3 = models.CharField(max_length=100, blank=True, null=True)
    score3 = models.IntegerField(blank=True, null=True)
    subject4 = models.CharField(max_length=100, blank=True, null=True)
    score4 = models.IntegerField(blank=True, null=True)

    applicant = models.OneToOneField(Application, on_delete=models.CASCADE, related_name='modeOfEntry', default=None)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True, default=None)


    # Choices of Study
    first_choice = models.CharField(max_length=100)
    second_choice = models.CharField(max_length=100)



    def __str__(self):
        return f"{self.jamb_reg_number} - {self.entry_mode}"

class OLevelQualification(models.Model):
    SITTING_CHOICES = [
        (1, 'One Sitting'),
        (2, 'Two Sittings'),
    ]

    sitting = models.IntegerField(choices=SITTING_CHOICES)

    applicant = models.OneToOneField(Application, on_delete=models.CASCADE, related_name='olevelqualification', default=None)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True, blank=True)

    # First Sitting Details
    first_exam_type = models.CharField(max_length=50, blank=True, null=True)  # e.g., WASSCE, NECO
    first_exam_year = models.IntegerField(blank=True, null=True)  # e.g., 2023
    first_school_name = models.CharField(max_length=255, blank=True, null=True)  # Name of school
    first_school_address = models.TextField(blank=True, null=True)  # Address of school
    first_exam_centre = models.CharField(max_length=255, blank=True, null=True)  # Exam centre name
    first_exam_period_from = models.DateField(blank=True, null=True)  # Exam period start date
    first_exam_period_to = models.DateField(blank=True, null=True)  # Exam period end date
    first_subjects_grades = models.TextField(blank=True, null=True)  # Subjects and grades stored as a JSON dictionary

    # Second Sitting Details (optional)
    second_exam_type = models.CharField(max_length=50, null=True, blank=True)
    second_exam_year = models.IntegerField(null=True, blank=True)
    second_school_name = models.CharField(max_length=255, null=True, blank=True)
    second_school_address = models.TextField(null=True, blank=True)
    second_exam_centre = models.CharField(max_length=255, null=True, blank=True)
    second_exam_period_from = models.DateField(null=True, blank=True)
    second_exam_period_to = models.DateField(null=True, blank=True)
    second_subjects_grades = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"OLevel - Sitting {self.sitting} ({self.session})"


class ALevelQualification(models.Model):
    applicant = models.OneToOneField(Application, on_delete=models.CASCADE, related_name='alevelqualification', default=None)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True, blank=True)
    school_name = models.CharField(max_length=255, blank=True, null=True)  # Name of school
    school_address = models.TextField(blank=True, null=True)  # Address of school
    exam_centre = models.CharField(max_length=255, blank=True, null=True)  # Exam centre name
    exam_period_from = models.DateField(blank=True, null=True)  # Exam period start date
    exam_period_to = models.DateField(blank=True, null=True)  # Exam period end date
    subjects_grades = models.TextField(blank=True, null=True)  # Subjects and grades stored as a JSON dictionary

    def __str__(self):
        return f"ALevel - {self.school_name} ({self.session})"

class AdditionalQualification(models.Model):
    applicant = models.OneToOneField(Application, on_delete=models.CASCADE, related_name='additionalqualification', default=None)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True, default=None)
    school_name = models.CharField(max_length=255,blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    course_of_study = models.CharField(max_length=255, blank=True, null=True)
    certificate_issued = models.CharField(max_length=255, blank=True, null=True)
    graduating_grade = models.CharField(max_length=50, blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.school_name

class HealthDetail(models.Model):
    AILMENT_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    
    has_ailment = models.CharField(
        max_length=3, 
        choices=AILMENT_CHOICES, 
        default='no', 
        verbose_name="Requires Special Medical Attention",
        blank=True, null=True
    )
    ailment_details = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Ailment Details"
    )

    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True, default=None)
    applicant = models.OneToOneField(Application, on_delete=models.CASCADE, related_name='health_detail', default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ailment: {self.get_has_ailment_display()}"

    def save(self, *args, **kwargs):
        # Ensure ailment_details is cleared if has_ailment is "no"
        if self.has_ailment == 'no':
            self.ailment_details = ""
        super().save(*args, **kwargs)

class Declaration(models.Model):
    # Declaration details
    applicant = models.OneToOneField(Application, on_delete=models.CASCADE, related_name='declaration', default=None)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True, default=None)
    full_name = models.CharField(max_length=255, blank=True, null=True)  # Full name of the applicant
    consent = models.BooleanField(blank=True, null=True)  # Yes/No consent to the declaration

    # Payment evidence details
    bank_name = models.CharField(max_length=255, blank=True, null=True)  # Bank name for payment
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Payment amount
    payment_date = models.DateField(blank=True, null=True)  # Payment date
    receipt_number = models.CharField(max_length=255, blank=True, null=True)  # Receipt/Teller number

    # Referral details
    heard_from = models.CharField(
        max_length=50,
        choices=[
            ('Social Media', 'Social Media'),
            ('Radio Advert', 'Radio Advert'),
            ('Newspaper Advert', 'Newspaper Advert'),
            ('Other', 'Other'),
        ],
        blank=True, null=True
    )

    # Timestamps for tracking creation and modification
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Declaration by {self.full_name}"



class UploadedCredentials(models.Model):
    payment_upload = models.FileField(upload_to='applications/payment_evidence/', blank=True, null=True, verbose_name="Payment Evidence")
    jamb_upload = models.FileField(upload_to='applications/jamb_results/', blank=True, null=True, verbose_name="JAMB Result")
    waec_upload = models.FileField(upload_to='applications/waec_results/', blank=True, null=True, verbose_name="WAEC Result")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    applicant = models.OneToOneField(Application, on_delete=models.CASCADE, related_name='uploadedcredentials', default=None)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True, default=None)

class AdditionalCredentials(models.Model):
    name = models.CharField(max_length=255)  # e.g., "WAEC Result", "JAMB Result"
    file = models.FileField(upload_to='applications/additionalcredentials/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    applicant = models.OneToOneField(Application, on_delete=models.CASCADE, related_name='additionalcredentials', default=None)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True, default=None)