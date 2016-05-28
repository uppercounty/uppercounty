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

"""URL conf file for website.

.. moduleauthor:: Yang Yang <y4n9squared@gmail.com>
.. moduleauthor:: Andrew Wang <wangandrewt@gmail.com>

"""

from django.conf.urls import patterns, url
from web import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^practices/$', views.practices, name='practices'),
    url(r'^team/$', views.team, name='team'),
    url(r'^meets/$', views.meets, name='meets'),
    url(r'^volunteer/', views.volunteer, name='volunteer'),
    url(r'^shop/', views.shop, name='shop'),
    url(r'^coaches/', views.CoachesList.as_view(), name='coaches'),
    url(r'^records/', views.records, name='records'),
]
