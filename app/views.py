from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
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


def ApplyStart(request):
    return render(request, "./apply/applystart.html")

def ApplyOne(request):
    return render(request, "./apply/apply1.html")

def ApplyTwo(request):
    return render(request, "./apply/apply2.html")

def ApplyThree(request):
    return render(request, "./apply/apply3.html")

def ApplyFour(request):
    return render(request, "./apply/apply4.html")

def ApplyFive(request):
    return render(request, "./apply/apply5.html")



def Signup(request):
    return render(request, "./authentication/signup.html")

def Login(request):
    return render(request, "./authentication/login.html")

@login_required
def logout(request):
    auth.logout(request)
    return redirect("/")