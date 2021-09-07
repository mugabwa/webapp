from users.models import NewUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
# Change the admin view interface
class UserAdminConfig(UserAdmin):
    search_fields = ('email','username','full_name')
    list_filter = ('email','username','full_name','postal_code','description','is_lead')
    ordering = ('-start_date',) # Display order
    list_display = ('email','username','full_name','postal_code','description','is_lead')
    fieldsets = (('Personal Info', {'fields':('email','full_name','username')}),
    ('Detailed Info',{'fields':('postal_code','description')}),
    ('Status',{'fields':('is_lead',)}),)
# make the model changes visible
admin.site.register(NewUser, UserAdminConfig)