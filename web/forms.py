from __future__ import absolute_import
from __future__ import unicode_literals
# Copyright (c) 2015 Upper County Dolphins
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

.. moduleauthor:: Andrew Wang <wangandrewt@gmail.com>

"""

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UniqueEmailUser


class UniqueEmailUserCreationForm(UserCreationForm):
    """A form to create a UniqueEmailUser."""

    class Meta:
        model = UniqueEmailUser
        fields = ("email",)


class UniqueEmailUserChangeForm(UserChangeForm):
    """A form to update a UniqueEmailUser."""

    class Meta:
        model = UniqueEmailUser
        fields = ("email",)
