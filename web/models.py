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
.. moduleauthor:: Andrew Wang <wangandrewt@gmail.com>

"""

from __future__ import absolute_import
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import datetime
import os
from django.contrib.auth.models import(AbstractBaseUser, BaseUserManager,
                                       PermissionsMixin)
from django.db import models
from django.utils import timezone


class UniqueEmailUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        """Create and saves a user with the given info.

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
        user.is_superuser = False
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, password):
        """Create and save a superuser with the given info.

        :param email: unique email address
        :param first_name: first name
        :param last_name: last name
        :param password: password

        """
        user = self.create_user(email, first_name, last_name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class UniqueEmailUser(AbstractBaseUser, PermissionsMixin):
    """A custom user model for authentication.

    Use emails instead of usernames
    """

    email = models.EmailField(verbose_name='email address', max_length=255,
                              unique=True, db_index=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UniqueEmailUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        """Return the full name of the user."""
        return (self.first_name + " " + self.last_name).title()

    def get_short_name(self):
        """Return the first name of the user."""
        return self.first_name.title()

    class Meta:
        verbose_name = "User"


@python_2_unicode_compatible
class Coach(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=25)
    bio = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    image_file = models.ImageField(upload_to='coach-images', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "coaches"


@python_2_unicode_compatible
class SwimRecord(models.Model):
    RECORD_TYPE_POOL = 1
    RECORD_TYPE_TEAM = 2
    RECORD_TYPE_CHOICES = (
        (RECORD_TYPE_POOL, 'Pool'),
        (RECORD_TYPE_TEAM, 'Team'),
    )
    TEAM_CHOICES = (
        ('A', 'Ashton'),
        ('B', 'Bannockburn'),
        ('BE', 'Bethesda'),
        ('C', 'Cedarbrook'),
        ('CA', 'Calverton'),
        ('CB', 'Connecticut Belair'),
        ('CCR', 'Chevy Chase Recreation Association'),
        ('CG', 'Country Glen'),
        ('CLK', 'Clarksburg Village'),
        ('CLM', 'Clopper Mill Kingsview'),
        ('CS', 'Carderock Springs'),
        ('CTC', 'Clarksburg Town Center'),
        ('D', 'Daleview'),
        ('DA', 'Damascus'),
        ('DF', 'Diamond Farm'),
        ('DT', 'Darnestown'),
        ('EG', 'East Gate'),
        ('EW', 'Eldwick'),
        ('FH', 'Flower Hill'),
        ('FM', 'Fallsmead'),
        ('FO', 'Forest Knolls'),
        ('FR', 'Franklin Knolls'),
        ('FV', 'Flower Valley'),
        ('G', 'Glenwood'),
        ('GER', 'Germantown'),
        ('GM', 'Glenmont'),
        ('GP', 'Garrett Park'),
        ('H', 'Hillandale'),
        ('HA', 'Hallowell'),
        ('IF', 'Inverness Recreation Club'),
        ('JC', 'James Creek'),
        ('K', 'Kenmont'),
        ('KFM', 'King Farm'),
        ('KL', 'Kentlands'),
        ('KM', 'Kemp Mill'),
        ('LB', 'Long Branch'),
        ('LF', 'Little Falls'),
        ('LLD', 'Lakelands'),
        ('LM', 'Lake Marion'),
        ('MB', 'Middlebridge'),
        ('MCF', 'Manchester Farm'),
        ('MCT', 'Mill Creek Towne'),
        ('MM', 'Merrimack Park'),
        ('MO', 'Mohican'),
        ('MS', 'Montgomery Square'),
        ('MW', 'Manor Woods'),
        ('NCC', 'North Chevy Chase'),
        ('NGV', 'Norbeck Grove'),
        ('NH', 'Norbeck Hills'),
        ('NMC', 'New Mark Commons'),
        ('NO', 'North Creek'),
        ('NWB', 'Northwest Branch'),
        ('OF', 'Old Farm'),
        ('OG', 'Old Georgetown'),
        ('OM', 'Olney Mill'),
        ('P', 'Parkland'),
        ('PA', 'Palisades'),
        ('PGL', 'Potomac Glen'),
        ('PL', 'Poolesville'),
        ('PLT', 'Plantations'),
        ('PO', 'Potomac'),
        ('PW', 'Potomac Woods'),
        ('QO', 'Quince Orchard'),
        ('QV', 'Quail Valley'),
        ('RC', 'Rock Creek'),
        ('RE', 'Regency Estates'),
        ('RF', 'River Falls'),
        ('RH', 'Robin Hood'),
        ('RS', 'Rockshire'),
        ('RV', 'Rockville'),
        ('SB', 'Stonebridge'),
        ('SG', 'Stonegate'),
        ('SL', 'Seven Locks'),
        ('SO', 'Somerset'),
        ('TA', 'Tanterra'),
        ('TB', 'Twinbrook'),
        ('TF', 'Twin Farms'),
        ('TH', 'Tallyho'),
        ('TN', 'Tanglewood'),
        ('TW', 'Tilden Woods'),
        ('UC', 'Upper County'),
        ('W', 'Whetstone'),
        ('WCF', 'Woodcliffe'),
        ('WG', 'Woodley Gardens'),
        ('WHI', 'West Hillandale'),
        ('WL', 'Westleigh'),
        ('WLP', 'Willows Of Potomac'),
        ('WM', 'Wildwood Manor'),
        ('WTL', 'Waters Landing'),
        ('WW', 'Wheaton Woods'),
        ('WWD', 'Washingtonian Woods'),
    )

    record_type = models.PositiveSmallIntegerField(choices=RECORD_TYPE_CHOICES)
    event_number = models.PositiveSmallIntegerField()
    event_name = models.CharField(max_length=100)
    swimmer_name = models.CharField(max_length=400)
    swimmer_team = models.CharField(blank=True, max_length=4,
                                    choices=TEAM_CHOICES)
    time = models.CharField(max_length=9)
    date = models.DateField(blank=True, null=True)
    pool = models.CharField(blank=True, max_length=4, choices=TEAM_CHOICES)

    def __str__(self):
        result = dict(self.RECORD_TYPE_CHOICES).get(self.record_type) + \
            " Record for Swimmers=[" + self.swimmer_name + \
            "] of team=[" + self.swimmer_team + "] Event=[#" + \
            str(self.event_number) + " " + self.event_name + "] on"
        if self.date:
            result += " " + self.date.strftime('%Y-%m-%d')
        result += " at pool=[" + self.pool + "] with time " + self.time
        return result


@python_2_unicode_compatible
class Meet(models.Model):
    MEET_TYPE_A = 1
    MEET_TYPE_B = 2
    MEET_TYPE_OTHER = 3
    MEET_TYPE_CHOICES = (
        (MEET_TYPE_A, 'A'),
        (MEET_TYPE_B, 'B'),
        (MEET_TYPE_OTHER, 'Other'),
    )

    meet_type = models.PositiveSmallIntegerField(choices=MEET_TYPE_CHOICES)
    name = models.CharField(max_length=200)
    date = models.DateField()
    program_file = models.FileField(upload_to='meet-documents', blank=True)
    program_date_updated = models.DateField(blank=True, null=True)
    results_file = models.FileField(upload_to='meet-documents', blank=True)
    results_date_updated = models.DateField(blank=True, null=True)

    def was_program_date_updated_recently(self):
        if not self.program_date_updated:
            return False
        return self.program_date_updated >= \
            datetime.date.today() - datetime.timedelta(days=2)
    was_program_date_updated_recently.boolean = True

    def was_results_date_updated_recently(self):
        if not self.results_date_updated:
            return False
        return self.results_date_updated >= \
            datetime.date.today() - datetime.timedelta(days=2)
    was_results_date_updated_recently.boolean = True

    def is_current_year_meet(self):
        return self.date.year >= datetime.date.today().year
    is_current_year_meet.boolean = True

    def __str__(self):
        return self.name + " "
        + dict(self.MEET_TYPE_CHOICES).get(self.meet_type)
        + " Meet on " + self.date.strftime('%Y-%m-%d')
