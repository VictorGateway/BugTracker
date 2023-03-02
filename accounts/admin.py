
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomChangeForm, CustomCreationForm
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    class Meta(UserAdmin):
        form = CustomChangeForm
        add_form=CustomCreationForm
        model=CustomUser
        
    fieldsets = (
        (_("Main Field"), {'fields': ('email', 'password', 'company', 'position')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'company', 'position'),
         }),
    )
    list_display= (
            "email",
            "company",
            "position",
            "is_staff",
    )
    search_fields=("email", "first_name", "last_name", "company","position")
    ordering = ("email",)
admin.site.register(CustomUser, CustomUserAdmin)
