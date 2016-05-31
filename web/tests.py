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

"""Unit tests.

.. moduleauthor:: Yang Yang <y4n9squared@gmail.com>
.. moduleauthor:: Andrew Wang <wangandrewt@gmail.com>

"""

from __future__ import absolute_import
from __future__ import unicode_literals
import datetime
from django.test import TestCase
from django.utils import timezone

from .models import UniqueEmailUser, Meet


class UniqueEmailUserTestCase(TestCase):
    """Test functionality of UniqueEmailUser."""

    def setUp(self):
        UniqueEmailUser.objects.create_user(email="johndoe@example.com",
                                            first_name="John", last_name="Doe")
        UniqueEmailUser.objects.create_superuser(
            email="admin@example.com", first_name="Jane", last_name="Dear",
            password="pass1234")

    def test_email(self):
        user = UniqueEmailUser.objects.get(email="johndoe@example.com")
        self.assertEqual(user.email, "johndoe@example.com")

    def test_first_name(self):
        user = UniqueEmailUser.objects.get(email="johndoe@example.com")
        self.assertEqual(user.first_name, "John")

    def test_last_name(self):
        user = UniqueEmailUser.objects.get(email="johndoe@example.com")
        self.assertEqual(user.last_name, "Doe")

    def test_full_name_is_correct(self):
        user = UniqueEmailUser.objects.get(email="johndoe@example.com")
        self.assertEqual(user.get_full_name(), "John Doe")

    def test_short_name_is_correct(self):
        user = UniqueEmailUser.objects.get(email="johndoe@example.com")
        self.assertEqual(user.get_short_name(), "John")

    def test_does_not_have_perm(self):
        user = UniqueEmailUser.objects.get(email="johndoe@example.com")
        self.assertFalse(user.has_perm('web'))

    def test_does_not_have_module_perms(self):
        user = UniqueEmailUser.objects.get(email="johndoe@example.com")
        self.assertFalse(user.has_module_perms('web'))

    def test_is_not_staff(self):
        user = UniqueEmailUser.objects.get(email="johndoe@example.com")
        self.assertFalse(user.is_staff)

    def test_is_staff(self):
        user = UniqueEmailUser.objects.get(email="admin@example.com")
        self.assertTrue(user.is_staff)


class WebViewsTestCase(TestCase):

    def test_index(self):
        with self.assertTemplateUsed('web/index.html'):
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        with self.assertTemplateUsed('web/index.html'):
            response = self.client.get('/web/')
            self.assertEqual(response.status_code, 200)

    def test_team_info_page(self):
        response = self.client.get('/web/team/')
        self.assertRedirects(response, '/web/practices/', 301, 200)

    def test_practices_page(self):
        with self.assertTemplateUsed('web/practices.html'):
            response = self.client.get('/web/practices/')
            self.assertEqual(response.status_code, 200)

    def test_volunteer_page(self):
        with self.assertTemplateUsed('web/volunteer.html'):
            response = self.client.get('/web/volunteer/')
            self.assertEqual(response.status_code, 200)

    def test_shop_page(self):
        with self.assertTemplateUsed('web/shop.html'):
            response = self.client.get('/web/shop/')
            self.assertEqual(response.status_code, 200)

    def test_coaches_page(self):
        with self.assertTemplateUsed('web/coaches.html'):
            response = self.client.get('/web/coaches/')
            self.assertEqual(response.status_code, 200)

    def test_http404(self):
        with self.assertTemplateUsed('web/404.html'):
            response = self.client.get('/web/doesnotexist')
            self.assertEqual(response.status_code, 404)

    def test_records_page(self):
        with self.assertTemplateUsed('web/records.html'):
            response = self.client.get('/web/records/')
            self.assertEqual(response.status_code, 200)

    def test_meets_page(self):
        with self.assertTemplateUsed('web/meets.html'):
            response = self.client.get('/web/meets/')
            self.assertEqual(response.status_code, 200)


class MeetTestCase(TestCase):
    """Test functionality of Meet."""

    def test_was_program_date_updated_recently_with_old_doc(self):
        date = datetime.date.today() - datetime.timedelta(days=3)
        doc = Meet(program_date_updated=date)
        self.assertEqual(doc.was_program_date_updated_recently(), False)

    def test_was_program_date_updated_recently(self):
        date = datetime.date.today() - datetime.timedelta(days=1)
        doc = Meet(program_date_updated=date)
        self.assertEqual(doc.was_program_date_updated_recently(), True)

    def test_was_results_date_updated_recently_with_old_doc(self):
        date = datetime.date.today() - datetime.timedelta(days=3)
        doc = Meet(results_date_updated=date)
        self.assertEqual(doc.was_results_date_updated_recently(), False)

    def test_was_results_date_updated_recently(self):
        date = datetime.date.today() - datetime.timedelta(days=1)
        doc = Meet(results_date_updated=date)
        self.assertEqual(doc.was_results_date_updated_recently(), True)

    def test_is_current_year_meet_with_old_meet(self):
        date = datetime.date.today() - datetime.timedelta(weeks=53)
        meet = Meet(date=date)
        self.assertEqual(meet.is_current_year_meet(), False)

    def test_is_current_year_meet(self):
        date = datetime.date.today()
        meet = Meet(date=date)
        self.assertEqual(meet.is_current_year_meet(), True)
