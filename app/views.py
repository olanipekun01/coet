from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
# from .forms import UserSignupForm, StudentSignupForm, InstructorSignupForm
from .models import *
from django.db.models import Max, Q, F
import uuid
import random
import string
import json

import os

import fpdf
from fpdf import FPDF, HTMLMixin

from django.http import HttpResponse
from django.template.loader import render_to_string

# from weasyprint import HTML

# from io import BytesIO
# from django.template.loader import get_template
# from xhtml2pdf import pisa

from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin


from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict


from django.contrib import messages

# Create your views here.
def Index(request):
    return render(request, "index.html")

def About(request):
    return render(request, "aboutUs.html")

def PrincipalOfficers(request):
    return render(request, "principalofficers.html")

def Staff(request):
    return render(request, "staff.html")

def Contact(request):
    return render(request, "contact.html")

def Department(request):
    return render(request, "departments.html")

def EachDepartment(request, pk):
    return render(request, "eachdepartment.html")

def Amissions(request):
    return render(request, "admissions.html")

@login_required
# @user_passes_test(is_student, login_url="/404")
def ApplyStart(request):
    if request.user.is_authenticated:
        user = request.user
     # Fetch the current session (assuming Session has an 'is_current' field)
    current_session = Session.objects.filter(is_current=True).first()
    if not current_session:
        return render(request, "./apply/applystart.html", {
            'error_message': "No current session is available."
        })
    
    if request.method == "POST":  # Ensure the new application is only created on form submission
            new_application = Application.objects.create(applicant=user, session=current_session)
            return redirect('/apply/1')
    
    # Check if the user already has an application for the current session
    application = Application.objects.filter(applicant=user, session=current_session).first()

    if application:
        # Redirect to the continuation of the existing application
        app = True
    else:
        app = False

    print('app', app)

    return render(request, "./apply/applystart.html", {'current_session': current_session, 'application': app})

@login_required
# @user_passes_test(is_student, login_url="/404")
def ApplyOne(request):
    if request.user.is_authenticated:
        user = request.user
        applicant = get_object_or_404(Application, applicant=user)
    # programmes = Programme.objects.all()
    current_session = Session.objects.filter(is_current=True).first()

    if current_session:

        application = Application.objects.filter(session=current_session).first()
        if not application:
            # If PersonalDetails is not completed, redirect to /apply/1
            messages.info(request, "Please start here first.")
            return redirect('/apply/start')


        personal_details = PersonalDetails.objects.filter(applicant=applicant, session=current_session).first()
        if personal_details:
            return redirect('/apply/2')

    # Fetch all available programmes for the form
    programmes = Programme.objects.all()

    if request.method == "POST":
        # Retrieve data from the POST request
        first_name = request.POST.get("firstName", "")
        last_name = request.POST.get("lastName", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        date_of_birth = request.POST.get("dateOfBirth", None)
        place_of_birth = request.POST.get("placeOfBirth", "")
        state_of_origin = request.POST.get("stateOfOrigin", "")
        nationality = request.POST.get("nationality", "")
        local_government_area = request.POST.get("localGovernmentArea", "")
        denomination = request.POST.get("denomination", "")
        address = request.POST.get("address", "")
        gender = request.POST.get("gender", "")
        desired_program_id = request.POST.get("desiredProgram", None)
        # session_id = request.POST.get("session", None)

        try:
        # Retrieve related Programme and Session instances
        # desired_program = Programme.objects.get(id=desired_program_id) if desired_program_id else None
        # session = Session.objects.get(id=session_id) if session_id else None

        # Create a new PersonalDetails instance
            personal_details = PersonalDetails.objects.create(
                applicant = applicant,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                date_of_birth=date_of_birth,
                place_of_birth=place_of_birth,
                state_of_origin=state_of_origin,
                nationality=nationality,
                local_government_area=local_government_area,
                denomination=denomination,
                address=address,
                gender=gender,
                desired_program=get_object_or_404(Programme, id=desired_program_id),
                session=get_object_or_404(Session, year=current_session.year)
            )

            # Save the instance to the database
            personal_details.save()

            # Redirect or respond with success
            return redirect('/apply/2')
        except Programme.DoesNotExist:
            messages.info(request, "Programme doesn't exist!")
            return redirect('/apply/1')
        except Session.DoesNotExist:
            messages.info(request, "Session doesn't exist!")
            return redirect('/apply/1')
        except Exception as e:
            messages.info(request, "Invalid request!")
            return redirect('/apply/1')


    return render(request, "./apply/apply1.html", {'programmes': programmes})

@login_required
# @user_passes_test(is_student, login_url="/404")
def ApplyTwo(request):
    if request.user.is_authenticated:
        user = request.user
        applicant = get_object_or_404(Application, applicant=user)
    # programmes = Programme.objects.all()
    current_session = Session.objects.filter(is_current=True).first()

    if current_session:

        personal_details = PersonalDetails.objects.filter(applicant=applicant, session=current_session).first()
        if not personal_details:
            # If PersonalDetails is not completed, redirect to /apply/1
            messages.info(request, "Please complete the Personal Details section first.")
            return redirect('/apply/1')


        parentsGuardian = ParentsGuardian.objects.filter(applicant=applicant, session=current_session).first()
        if parentsGuardian:
            return redirect('/apply/3')
    if request.method == "POST":
        try:
            # Extracting Father's Data
            father_surname = request.POST.get("father-surname")
            father_first_name = request.POST.get("father-firstName")
            father_other_name = request.POST.get("father-otherName")
            father_occupation = request.POST.get("father-occupation")
            father_place_of_work = request.POST.get("father-placeOfWork")
            father_telephone = request.POST.get("father-telephone")
            father_email = request.POST.get("father-email")
            
            # Extracting Mother's Data
            mother_surname = request.POST.get("mother-surname")
            mother_first_name = request.POST.get("mother-firstName")
            mother_other_name = request.POST.get("mother-otherName")
            mother_occupation = request.POST.get("mother-occupation")
            mother_place_of_work = request.POST.get("mother-placeOfWork")
            mother_telephone = request.POST.get("mother-telephone")
            mother_email = request.POST.get("mother-email")
            
            # Extracting Guardian's Data
            guardian_surname = request.POST.get("guardian-surname")
            guardian_first_name = request.POST.get("guardian-firstName")
            guardian_other_name = request.POST.get("guardian-otherName")
            guardian_occupation = request.POST.get("guardian-occupation")
            guardian_place_of_work = request.POST.get("guardian-placeOfWork")
            guardian_telephone = request.POST.get("guardian-telephone")
            guardian_email = request.POST.get("guardian-email")
            
            # Saving Data to the Model
            parent_guardian_data = ParentsGuardian.objects.create(
                father_surname=father_surname,
                father_first_name=father_first_name,
                father_other_name=father_other_name,
                father_occupation=father_occupation,
                father_place_of_work=father_place_of_work,
                father_telephone=father_telephone,
                father_email=father_email,
                
                mother_surname=mother_surname,
                mother_first_name=mother_first_name,
                mother_other_name=mother_other_name,
                mother_occupation=mother_occupation,
                mother_place_of_work=mother_place_of_work,
                mother_telephone=mother_telephone,
                mother_email=mother_email,
                
                guardian_surname=guardian_surname,
                guardian_first_name=guardian_first_name,
                guardian_other_name=guardian_other_name,
                guardian_occupation=guardian_occupation,
                guardian_place_of_work=guardian_place_of_work,
                guardian_telephone=guardian_telephone,
                guardian_email=guardian_email,

                applicant = applicant,
                session=get_object_or_404(Session, year=current_session.year),
            )
            
            return redirect('/apply/3')

        except ValidationError as e:
            messages.info(request, "Validation Error!")
            return redirect('/apply/2')
        except Session.DoesNotExist:
            messages.info(request, "Session doesn't exist!")
            return redirect('/apply/2')
        except Exception as e:
            messages.info(request, "Invalid request!")
            return redirect('/apply/2')

    # Render the form if GET request
    return render(request, "./apply/apply2.html")

@login_required
def ApplyThree(request):
    if request.user.is_authenticated:
        user = request.user
        applicant = get_object_or_404(Application, applicant=user)
    # programmes = Programme.objects.all()
    current_session = Session.objects.filter(is_current=True).first()

    if current_session:
        parentGuardian = ParentsGuardian.objects.filter(applicant=applicant, session=current_session).first()
        if not parentGuardian:
            # If PersonalDetails is not completed, redirect to /apply/1
            messages.info(request, "Please complete the Parent Guardian section first.")
            return redirect('/apply/2')
        
        sponsor = Sponsor.objects.filter(applicant=applicant, session=current_session).first()
        if sponsor:
            return redirect('/apply/4')

    if request.method == 'POST':
        surname = request.POST.get('surname')
        first_name = request.POST.get('first_name')
        other_name = request.POST.get('other_name')
        occupation = request.POST.get('occupation')
        place_of_work = request.POST.get('place_of_work')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')

        print('info', surname, first_name, occupation, place_of_work, telephone, email)

        # Validate required fields
        if not surname or not first_name or not occupation or not place_of_work or not telephone or not email:
            messages.error(request, 'Please fill in all required fields.')
            return redirect('/apply/3')  # Redirect back to the form

        try:
            # Save to database
            sponsor = Sponsor(
                surname=surname,
                first_name=first_name,
                other_name=other_name,
                occupation=occupation,
                place_of_work=place_of_work,
                telephone=telephone,
                email=email,
                applicant = applicant,
                session=get_object_or_404(Session, year=current_session.year),
            )
            sponsor.save()

            messages.success(request, 'Sponsor information has been saved successfully!')
            return redirect('/apply/4')  # Redirect to avoid duplicate submissions

        except ValidationError as e:
            messages.info(request, "Validation Error!")
            return redirect('/apply/3')
        except Session.DoesNotExist:
            messages.info(request, "Session doesn't exist!")
            return redirect('/apply/3')
        except Exception as e:
            messages.info(request, "Invalid request!")
            return redirect('/apply/3')

    return render(request, "./apply/apply3.html")

@login_required
def ApplyFour(request):
    if request.user.is_authenticated:
        user = request.user
        applicant = get_object_or_404(Application, applicant=user)
    # programmes = Programme.objects.all()
    current_session = Session.objects.filter(is_current=True).first()

    if current_session:

        sponsor = Sponsor.objects.filter(applicant=applicant, session=current_session).first()
        if not sponsor:
            # If PersonalDetails is not completed, redirect to /apply/1
            messages.info(request, "Please complete the Sponsor section first.")
            return redirect('/apply/3')

        modeOfEntry = ModeOfEntry.objects.filter(applicant=applicant, session=current_session).first()
        if modeOfEntry:
            return redirect('/apply/5')

    programmes = Programme.objects.all()
    if request.method == 'POST':
        # Retrieve form data
        entry_mode = request.POST.get('entryMode')
        jamb_reg_number = request.POST.get('jambRegNumber')
        score1 = request.POST.get('score1')
        subject2 = request.POST.get('subject2', '')
        score2 = request.POST.get('score2')
        score3 = request.POST.get('score3')
        subject3 = request.POST.get('subject3', '')
        score4 = request.POST.get('score4')
        subject4 = request.POST.get('subject4', '')
        score4 = request.POST.get('score4')

        first_choice = request.POST.get('firstChoice')
        second_choice = request.POST.get('secondChoice')

        print('info', entry_mode, jamb_reg_number, score1, first_choice)

        # Validate form data
        if not entry_mode or not jamb_reg_number or not score1 or not first_choice:
            messages.error(request, "Please fill out all required fields.")
            return redirect('/apply/4/')


        try:
            # Create a new Application instance
            application = ModeOfEntry(
                entry_mode=entry_mode,
                jamb_reg_number=jamb_reg_number,
                subject1="Use of English",
                score1=score1,
                subject2=subject2,
                score2=score2 if score2 else None,
                subject3=subject3,
                score3=score3 if score3 else None,
                subject4=subject4,
                score4=score4 if score4 else None,
                first_choice=first_choice,
                second_choice=second_choice,
                applicant = applicant,
                session=get_object_or_404(Session, year=current_session.year),
            )
            application.save()
            messages.success(request, "Application submitted successfully.")
            return redirect('/apply/5')  # Replace 'next_step' with the next URL name
        except Programme.DoesNotExist:
            messages.info(request, "Programme doesn't exist!")
            return redirect('/apply/4')
        except Exception as e:
            messages.error(request, f"Error saving application: {str(e)}")
            return redirect('/apply/4')

    return render(request, "./apply/apply4.html")

@login_required
def ApplyFive(request):
    if request.user.is_authenticated:
        user = request.user
        applicant = get_object_or_404(Application, applicant=user)
    # programmes = Programme.objects.all()
    current_session = Session.objects.filter(is_current=True).first()

    if current_session:

        modeOfEntry = ModeOfEntry.objects.filter(applicant=applicant, session=current_session).first()
        if not modeOfEntry:
            # If PersonalDetails is not completed, redirect to /apply/1
            messages.info(request, "Please complete the Mode Of Entry section first.")
            return redirect('/apply/4')

        oLevelQualification = OLevelQualification.objects.filter(applicant=applicant, session=current_session).first()
        if oLevelQualification:
            return redirect('/apply/6')

    programmes = Programme.objects.all()

    if request.method == 'POST':
        sitting = request.POST.get("sitting")
        oLevelSchool1 = request.POST.get("oLevelSchool1")
        oLevelAddress1 = request.POST.get("oLevelAddress1")
        oLevelCentre1 = request.POST.get("oLevelCentre1")
        oLevelFrom1 = request.POST.get("oLevelFrom1")
        oLevelTo1 = request.POST.get("oLevelTo1")

        subject1 = request.POST.getlist("subject1")
        grade1 = request.POST.getlist("grade1")
        subjects_and_grades1 = dict(zip(subject1, grade1))
        # print('olevel', subjects_and_grades1)

        # For second sitting, if applicable
        if sitting == "two":
            oLevelSchool2 = request.POST.get("oLevelSchool")
            oLevelAddress2 = request.POST.get("oLevelAddress")
            oLevelCentre2 = request.POST.get("oLevelCentre")
            oLevelFrom2 = request.POST.get("oLevelFrom")
            oLevelTo2 = request.POST.get("oLevelTo")
            subject2 = request.POST.getlist("subject")
            grade2 = request.POST.getlist("grade")
            subjects_and_grades2 = dict(zip(subject2, grade2))
        else:
            oLevelSchool2 = None
            oLevelAddress2 = None
            oLevelCentre2 = None
            oLevelFrom2 = None
            oLevelTo2 = None
            subjects_and_grades2 = None

        # Save to the model
        try:
            olevel_qualification = OLevelQualification(
                sitting=1 if sitting == "one" else 2,
                first_exam_type="WASSCE",  # Replace with dynamic data if needed
                first_exam_year=oLevelTo1.split("-")[0],  # Extract the year from the date
                first_school_name=oLevelSchool1,
                first_school_address=oLevelAddress1,
                first_exam_centre=oLevelCentre1,
                first_exam_period_from=oLevelFrom1,
                first_exam_period_to=oLevelTo1,
                first_subjects_grades=json.dumps(subjects_and_grades1),

                second_exam_type="WASSCE" if sitting == "two" else None,  # Replace dynamically
                second_exam_year=oLevelTo2.split("-")[0] if sitting == "two" else None,
                second_school_name=oLevelSchool2,
                second_school_address=oLevelAddress2,
                second_exam_centre=oLevelCentre2,
                second_exam_period_from=oLevelFrom2,
                second_exam_period_to=oLevelTo2,
                second_subjects_grades=json.dumps(subjects_and_grades2),
                applicant = applicant,
                session=current_session,
            )
            olevel_qualification.save()
        except OLevelQualification.DoesNotExist:
            messages.info(request, "OLevelQualification doesn't exist!")
            return redirect('/apply/5')
        except Exception as e:
            messages.error(request, f"Error saving application: {str(e)}")
            return redirect('/apply/5')

        # a level
        school_name = request.POST.get("school_name", "")
        school_address = request.POST.get("school_address", "")
        exam_centre = request.POST.get("exam_centre", "")
        exam_period_from = request.POST.get("exam_period_from", None)
        exam_period_to = request.POST.get("exam_period_to", None)
        agrades = request.POST.getlist("agrade1", "")
        asubjects = request.POST.getlist("asubject1", "")


        asubjects_and_grades = dict(zip(asubjects, agrades))
        print('alevel', asubjects_and_grades)

        
           

        # Save the A-Level qualification
        try:
            ALevel = ALevelQualification.objects.create(
                applicant = applicant,
                session=current_session,
                school_name=school_name,
                school_address=school_address,
                exam_centre=exam_centre,
                exam_period_from=exam_period_from,
                exam_period_to=exam_period_to,
                subjects_grades=json.dumps(asubjects_and_grades),
            )

            ALevel.save()
        except ALevelQualification.DoesNotExist:
            messages.info(request, "ALevelQualification doesn't exist!")
            return redirect('/apply/5')
        except Exception as e:
            messages.error(request, f"Error saving application: {str(e)}")
            return redirect('/apply/5')

        school_name = request.POST.get("school_name", "")
        address = request.POST.get("address", "")
        course_of_study = request.POST.get("course_of_study", "")
        certificate_issued = request.POST.get("certificate_issued", "")
        graduating_grade = request.POST.get("graduating_grade", "")
        from_date = request.POST.get("from_date", None)
        to_date = request.POST.get("to_date", None)

        try:
            AddQual  = AdditionalQualification.objects.create(
                school_name=school_name,
                address=address,
                course_of_study=course_of_study,
                certificate_issued=certificate_issued,
                graduating_grade=graduating_grade,
                from_date=from_date,
                to_date=to_date,
                applicant = applicant,
                session=current_session,
            )

            AddQual.save()
            return redirect('/apply/6')
        except AdditionalQualification.DoesNotExist:
            messages.info(request, "AdditionalQualification doesn't exist!")
            return redirect('/apply/5')
        except Exception as e:
            messages.error(request, f"Error saving application: {str(e)}")
            return redirect('/apply/5')



    return render(request, "./apply/apply5.html")

# @login_required
def ApplySix(request):
    if request.user.is_authenticated:
        user = request.user
        applicant = get_object_or_404(Application, applicant=user)
    # programmes = Programme.objects.all()
    current_session = Session.objects.filter(is_current=True).first()

    if current_session:

        oLevelQualification = OLevelQualification.objects.filter(applicant=applicant, session=current_session).first()
        if not oLevelQualification:
            # If PersonalDetails is not completed, redirect to /apply/1
            messages.info(request, "Please complete the OLevel Qualification section first.")
            return redirect('/apply/5')


        health_detail = HealthDetail.objects.filter(applicant=applicant, session=current_session).first()
        if health_detail:
            return redirect('/apply/7')

    if request.method == 'POST':
        has_ailment = request.POST.get('hasAilment')
        ailment_details = request.POST.get('ailmentDetails', '')

        # Ensure ailment details are only saved if has_ailment is 'yes'
        if has_ailment == 'no':
            ailment_details = ''

        try:
            # Save data to the database
            health_detail = HealthDetail.objects.create(
                has_ailment=has_ailment,
                ailment_details=ailment_details,
                applicant = applicant,
                session=current_session,
            )

            health_detail.save()

            return redirect('/apply/7')
        except HealthDetail.DoesNotExist:
            messages.info(request, "HealthDetail doesn't exist!")
            return redirect('/apply/6')
        except Exception as e:
            messages.error(request, f"Error saving application: {str(e)}")
            return redirect('/apply/6')

    return render(request, "./apply/apply6.html")

# @login_required
def ApplySeven(request):
    if request.user.is_authenticated:
        user = request.user
        applicant = get_object_or_404(Application, applicant=user)
    # programmes = Programme.objects.all()
    current_session = Session.objects.filter(is_current=True).first()

    if current_session:
        healthDetail = HealthDetail.objects.filter(applicant=applicant, session=current_session).first()
        if not healthDetail:
            # If PersonalDetails is not completed, redirect to /apply/1
            messages.info(request, "Please complete the Health Detail section first.")
            return redirect('/apply/6')

        declaration = Declaration.objects.filter(applicant=applicant, session=current_session).first()
        if declaration:
            return redirect('/apply/status')

    if request.method == "POST":
        # Extract data from POST request
        full_name = request.POST.get("fullName")
        consent = request.POST.get("consent") == "yes"  # Convert 'yes'/'no' to boolean
        bank_name = request.POST.get("bankName")
        amount = request.POST.get("amount")
        payment_date = request.POST.get("date")
        receipt_number = request.POST.get("receiptNumber")
        heard_from = request.POST.get("heardFrom")

        # # Validate required fields
        # if not all([full_name, bank_name, amount, payment_date, receipt_number, heard_from]):
        #     messages.error(request, "All fields are required")
        #     return redirect('/apply/7/')

        if not (consent):
            messages.error(request, "You must consent to the declaration to proceed.")
            return redirect('/apply/7/')
        try:
            # Save to database
            declaration = Declaration.objects.create(
                full_name=full_name,
                consent=consent,
                bank_name=bank_name,
                amount=amount,
                payment_date=payment_date,
                receipt_number=receipt_number,
                heard_from=heard_from,
                applicant = applicant,
                session=current_session,
            )

            declaration.save()

            # Success response (redirect to a success page or return JSON)
            messages.info(request, f"Request was succesfully1")
            return redirect('/apply/status/')
        except Declaration.DoesNotExist:
            messages.info(request, "Declaration doesn't exist!")
            return redirect('/apply/7')
        except Exception as e:
            messages.error(request, f"Error saving application: {str(e)}")
            return redirect('/apply/7')

    return render(request, "./apply/apply7.html")

@login_required
def ApplyStatus(request):
    if request.user.is_authenticated:
        user = request.user
        applicant = get_object_or_404(Application, applicant=user)
    # programmes = Programme.objects.all()
    current_session = Session.objects.filter(is_current=True).first()

    if current_session:

        declaration = Declaration.objects.filter(applicant=applicant, session=current_session).first()
        if not declaration:
            messages.info(request, "Please complete the Declaration section first.")
            return redirect('/apply/7')

    if request.method == "POST":
        payment_upload = request.FILES.get("payment-upload")
        jamb_upload = request.FILES.get("jamb-upload")
        waec_upload = request.FILES.get("waec-upload")

        credentials, created = UploadedCredentials.objects.get_or_create(applicant=applicant, session=current_session)
        # credentials = UploadedCredentials.objects.all()

        if payment_upload:
            credentials.payment_upload = payment_upload
        if jamb_upload:
            credentials.jamb_upload = jamb_upload
        if waec_upload:
            credentials.waec_upload = waec_upload

        credentials.session = current_session
        credentials.applicant = applicant

        credentials.save()
        messages.success(request, "Your files have been uploaded successfully.")
        return redirect("/apply/status")

    credentials = UploadedCredentials.objects.filter(applicant=applicant, session=current_session).first()
    # credentials = UploadedCredentials.objects.all()
    additional_files = AdditionalCredentials.objects.filter(applicant=applicant, session=current_session)
    # additional_files = AdditionalCredentials.objects.all()
    return render(request, "./apply/apply8.html", {
        "credentials": credentials,
        "additional_files": additional_files,
        "applicant": applicant,
    })


def upload_additional_file_view(request):
    if request.user.is_authenticated:
        user = request.user
        applicant = get_object_or_404(Application, applicant=user)
    # programmes = Programme.objects.all()
    current_session = Session.objects.filter(is_current=True).first()

    if current_session:
        declaration = Declaration.objects.filter(applicant=applicant, session=current_session).first()
        if not declaration:
            return redirect('/apply/7')

    if request.method == "POST":
        file_name = request.POST.get("file-name")
        additional_file = request.FILES.get("additional-upload")

        if not file_name or not additional_file:
            messages.error(request, "Please provide a valid file name and upload a file.")
            return redirect("/apply/status")

        AdditionalCredentials.objects.create(
            # user=request.user,
            name=file_name,
            file=additional_file,
            session=current_session,
            applicant=applicant,
        )
        messages.success(request, "Additional file uploaded successfully.")
        return redirect("/apply/status")
    return redirect("/apply/status")
    



def Signup(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        firstName = request.POST["firstName"]
        lastName = request.POST["lastName"]
        confirmPassword = request.POST["confirmPassword"]

        if password != confirmPassword:
            messages.info(request, "Password doesn't match!")
            redirect('/accounts/signup')
        
        # Validate form fields (you can add more complex validation if needed)
        if not (firstName and lastName and email and phone):
            messages.error(request, "Please fill out all required fields.")
            return redirect("/accounts/signup")  # Replace 'signup' with your signup view's URL name

        # Check for duplicate email
        if Application.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect("/accounts/signup")
    
    return render(request, "./authentication/signup.html")

def Login(request):
    if request.user.is_authenticated:
        user = request.user
        return redirect("/apply/start")
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            # user = auth.authenticate(username=email, password=password)
            user = authenticate(request, username=email, password=password)
            # user = User.objects.get(email=email)
            # if user.check_password(password):
            #     # Log the user in (assuming you're using Django's session framework)
            # login(request, user)
            #     return redirect('/')  # Redirect to the dashboard or homepage
            # else:
            #     error_message = "Invalid password."
            print('user', user)
            if user is not None:
                auth.login(request, user)
                return redirect("/apply/start")
                # 
                # if user.user_type == "student":
                #     return redirect("/")
                # elif user.user_type == "instructor":
                #     return redirect("/instructor/dashboard")
                # else:
                #     # Redirect user to a 404 page
                #     return redirect("/404")
            # elif user is not None and user.user_type == 'student':

            else:
                messages.error(request, "Invalid credentials!")
                return redirect('/accounts/login')
                # return render(request, "./authentication/login.html", {"error": error_message})
        except User.DoesNotExist:
            messages.error(request, "Invalid credentials!")
            return redirect('/accounts/login')
            # return render(request, "./authentication/login.html", {"error": error_message})

    return render(request, "./authentication/login.html")

@login_required
def logout(request):
    auth.logout(request)
    return redirect("/accounts/login")