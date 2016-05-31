# Copyright (c) 2014 Upper County Dolphins
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""Admin forms to input data.

.. moduleauthor:: Yang Yang <y4n9squared@gmail.com>
.. moduleauthor:: Andrew Wang <wangandrewt@gmail.com>

"""

from __future__ import absolute_import
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UniqueEmailUserCreationForm, UniqueEmailUserChangeForm
from .models import Coach, SwimRecord, Meet, UniqueEmailUser


class CoachAdmin(admin.ModelAdmin):
    """Set properties of Coach to display in admin interface."""

    list_display = ['name', 'email', 'title']
    list_filter = ['title']


class SwimRecordAdmin(admin.ModelAdmin):
    """Set properties of SwimRecord to display in admin interface."""

    list_filter = ['record_type']


class MeetAdmin(admin.ModelAdmin):
    """Set properties of Meet to display in admin interface."""

    list_filter = ['meet_type']
    list_display = ('name', 'meet_type', 'date')

admin.site.register(Coach, CoachAdmin)
admin.site.register(SwimRecord, SwimRecordAdmin)
admin.site.register(Meet, MeetAdmin)


class UniqueEmailUserAdmin(UserAdmin):
    """Set forms to add and change a UniqueEmailUser in admin interface."""

    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Metadata', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}),
    )
    form = UniqueEmailUserChangeForm
    add_form = UniqueEmailUserCreationForm
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

admin.site.register(UniqueEmailUser, UniqueEmailUserAdmin)
