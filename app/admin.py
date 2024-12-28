from django.contrib import admin
from .models import *
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User role',
            {
                'fields': (
                    'user_type',
                )
            }
        )
    )
    
# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(PersonalDetails)
admin.site.register(ParentsGuardian)
admin.site.register(Sponsor)
admin.site.register(OLevelQualification)
admin.site.register(ALevelQualification)
admin.site.register(AdditionalQualification)
admin.site.register(HealthDetail)
admin.site.register(Declaration)
admin.site.register(UploadedCredentials)
admin.site.register(AdditionalCredentials)
admin.site.register(Application)
@admin.register(ModeOfEntry)
class ModeOfEntryAdmin(admin.ModelAdmin):
    list_display = ('jamb_reg_number', 'entry_mode', 'first_choice', 'second_choice')
    search_fields = ('jamb_reg_number', 'first_choice', 'second_choice')
admin.site.register(College)
admin.site.register(Department)
admin.site.register(Session)
admin.site.register(Programme)