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

"""Module for views.

.. moduleauthor:: Yang Yang <y4n9squared@gmail.com>
.. moduleauthor:: Andrew Wang <wangandrewt@gmail.com>

"""

from __future__ import absolute_import
from __future__ import unicode_literals
from django import forms
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.generic import ListView

from .models import Coach, SwimRecord, Meet


def index(request):
    return render(request, 'web/index.html')


def team(request):
    return redirect(practices, permanent=True)


def practices(request):
    return render(request, 'web/practices.html')


def meets(request):
    results = Meet.objects.order_by('date')
    a_meets = [e for e in results if e.meet_type == Meet.MEET_TYPE_A and
               e.is_current_year_meet()]
    b_meets = [e for e in results if e.meet_type == Meet.MEET_TYPE_B and
               e.is_current_year_meet()]
    other_meets = [e for e in results
                   if e.meet_type == Meet.MEET_TYPE_OTHER and
                   e.is_current_year_meet()]
    archived_meets = [e for e in results if not e.is_current_year_meet()]
    return render(request, 'web/meets.html', {
        'a_meets': a_meets,
        'b_meets': b_meets,
        'other_meets': other_meets,
        'archived_meets': archived_meets,
    })


def volunteer(request):
    return render(request, 'web/volunteer.html')


def shop(request):
    return render(request, 'web/shop.html')


class CoachesList(ListView):
    context_object_name = 'coaches'
    queryset = Coach.objects.order_by('name')
    template_name = 'web/coaches.html'


def records(request):
    results = SwimRecord.objects.all()
    team_list = [e for e in results if
                 e.record_type == SwimRecord.RECORD_TYPE_TEAM]
    pool_list = [e for e in results if
                 e.record_type == SwimRecord.RECORD_TYPE_POOL]
    return render(request, 'web/records.html', {
        'team_list': sorted(team_list, key=lambda record: record.event_number),
        'pool_list': sorted(pool_list, key=lambda record: record.event_number)
    })


def handler404(request):
    return HttpResponseNotFound(render_to_string('web/404.html'))


def handler500(request):
    return HttpResponseNotFound(render_to_string('web/500.html'))
