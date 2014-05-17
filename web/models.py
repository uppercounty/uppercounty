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

"""Django models.

.. moduleauthor:: Yang Yang <y4n9squared@gmail.com>

"""

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UniqueEmailUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        """Creates and saves a user with the given email, first name, and last
        name.

        :param email: unique email address
        :param first_name: first name
        :param last_name: last name
        :param password: password

        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email),
                          first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, password):
        """Creates and saves a superuser with the given email, first name, and
        last name.

        :param email: unique email address
        :param first_name: first name
        :param last_name: last name
        :param password: password

        """

        user = self.create_user(email, first_name, last_name, password)
        user.is_admin = True
        user.save()
        return user


class UniqueEmailUser(AbstractBaseUser):
    """Custom user model for authentication using emails instead of
    usernames"""
    email = models.EmailField(verbose_name='email address', max_length=255,
                              unique=True, db_index=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UniqueEmailUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        """Returns the full name of the user"""
        return (self.first_name + " " + self.last_name).title()

    def get_short_name(self):
        """Returns the first name of the user"""
        return self.first_name.title()

    def has_perm(self, perm, obj=None):
        """Returns permissions of user"""
        return True

    def has_module_perms(self, app_label):
        """Returns permission of user to view `app_label`"""
        return True

    @property
    def is_staff(self):
        return self.is_admin
