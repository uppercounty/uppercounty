# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniqueEmailUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'email address', db_index=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meet_type', models.PositiveSmallIntegerField(choices=[(1, b'A'), (2, b'B'), (3, b'Other')])),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('program_file', models.FileField(upload_to=b'meet-documents', blank=True)),
                ('program_date_updated', models.DateField(null=True, blank=True)),
                ('results_file', models.FileField(upload_to=b'meet-documents', blank=True)),
                ('results_date_updated', models.DateField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SwimRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('record_type', models.PositiveSmallIntegerField(choices=[(1, b'Pool'), (2, b'Team')])),
                ('event_number', models.PositiveSmallIntegerField()),
                ('event_name', models.CharField(max_length=100)),
                ('swimmer_name', models.CharField(max_length=400)),
                ('swimmer_team', models.CharField(blank=True, max_length=4, choices=[(b'A', b'Ashton'), (b'B', b'Bannockburn'), (b'BE', b'Bethesda'), (b'C', b'Cedarbrook'), (b'CA', b'Calverton'), (b'CB', b'Connecticut Belair'), (b'CCR', b'Chevy Chase Recreation Association'), (b'CG', b'Country Glen'), (b'CLK', b'Clarksburg Village'), (b'CLM', b'Clopper Mill Kingsview'), (b'CS', b'Carderock Springs'), (b'CTC', b'Clarksburg Town Center'), (b'D', b'Daleview'), (b'DA', b'Damascus'), (b'DF', b'Diamond Farm'), (b'DT', b'Darnestown'), (b'EG', b'East Gate'), (b'EW', b'Eldwick'), (b'FH', b'Flower Hill'), (b'FM', b'Fallsmead'), (b'FO', b'Forest Knolls'), (b'FR', b'Franklin Knolls'), (b'FV', b'Flower Valley'), (b'G', b'Glenwood'), (b'GER', b'Germantown'), (b'GM', b'Glenmont'), (b'GP', b'Garrett Park'), (b'H', b'Hillandale'), (b'HA', b'Hallowell'), (b'IF', b'Inverness Recreation Club'), (b'JC', b'James Creek'), (b'K', b'Kenmont'), (b'KFM', b'King Farm'), (b'KL', b'Kentlands'), (b'KM', b'Kemp Mill'), (b'LB', b'Long Branch'), (b'LF', b'Little Falls'), (b'LLD', b'Lakelands'), (b'LM', b'Lake Marion'), (b'MB', b'Middlebridge'), (b'MCF', b'Manchester Farm'), (b'MCT', b'Mill Creek Towne'), (b'MM', b'Merrimack Park'), (b'MO', b'Mohican'), (b'MS', b'Montgomery Square'), (b'MW', b'Manor Woods'), (b'NCC', b'North Chevy Chase'), (b'NGV', b'Norbeck Grove'), (b'NH', b'Norbeck Hills'), (b'NMC', b'New Mark Commons'), (b'NO', b'North Creek'), (b'NWB', b'Northwest Branch'), (b'OF', b'Old Farm'), (b'OG', b'Old Georgetown'), (b'OM', b'Olney Mill'), (b'P', b'Parkland'), (b'PA', b'Palisades'), (b'PGL', b'Potomac Glen'), (b'PL', b'Poolesville'), (b'PLT', b'Plantations'), (b'PO', b'Potomac'), (b'PW', b'Potomac Woods'), (b'QO', b'Quince Orchard'), (b'QV', b'Quail Valley'), (b'RC', b'Rock Creek'), (b'RE', b'Regency Estates'), (b'RF', b'River Falls'), (b'RH', b'Robin Hood'), (b'RS', b'Rockshire'), (b'RV', b'Rockville'), (b'SB', b'Stonebridge'), (b'SG', b'Stonegate'), (b'SL', b'Seven Locks'), (b'SO', b'Somerset'), (b'TA', b'Tanterra'), (b'TB', b'Twinbrook'), (b'TF', b'Twin Farms'), (b'TH', b'Tallyho'), (b'TN', b'Tanglewood'), (b'TW', b'Tilden Woods'), (b'UC', b'Upper County'), (b'W', b'Whetstone'), (b'WCF', b'Woodcliffe'), (b'WG', b'Woodley Gardens'), (b'WHI', b'West Hillandale'), (b'WL', b'Westleigh'), (b'WLP', b'Willows Of Potomac'), (b'WM', b'Wildwood Manor'), (b'WTL', b'Waters Landing'), (b'WW', b'Wheaton Woods'), (b'WWD', b'Washingtonian Woods')])),
                ('time', models.CharField(max_length=9)),
                ('date', models.DateField(null=True, blank=True)),
                ('pool', models.CharField(blank=True, max_length=4, choices=[(b'A', b'Ashton'), (b'B', b'Bannockburn'), (b'BE', b'Bethesda'), (b'C', b'Cedarbrook'), (b'CA', b'Calverton'), (b'CB', b'Connecticut Belair'), (b'CCR', b'Chevy Chase Recreation Association'), (b'CG', b'Country Glen'), (b'CLK', b'Clarksburg Village'), (b'CLM', b'Clopper Mill Kingsview'), (b'CS', b'Carderock Springs'), (b'CTC', b'Clarksburg Town Center'), (b'D', b'Daleview'), (b'DA', b'Damascus'), (b'DF', b'Diamond Farm'), (b'DT', b'Darnestown'), (b'EG', b'East Gate'), (b'EW', b'Eldwick'), (b'FH', b'Flower Hill'), (b'FM', b'Fallsmead'), (b'FO', b'Forest Knolls'), (b'FR', b'Franklin Knolls'), (b'FV', b'Flower Valley'), (b'G', b'Glenwood'), (b'GER', b'Germantown'), (b'GM', b'Glenmont'), (b'GP', b'Garrett Park'), (b'H', b'Hillandale'), (b'HA', b'Hallowell'), (b'IF', b'Inverness Recreation Club'), (b'JC', b'James Creek'), (b'K', b'Kenmont'), (b'KFM', b'King Farm'), (b'KL', b'Kentlands'), (b'KM', b'Kemp Mill'), (b'LB', b'Long Branch'), (b'LF', b'Little Falls'), (b'LLD', b'Lakelands'), (b'LM', b'Lake Marion'), (b'MB', b'Middlebridge'), (b'MCF', b'Manchester Farm'), (b'MCT', b'Mill Creek Towne'), (b'MM', b'Merrimack Park'), (b'MO', b'Mohican'), (b'MS', b'Montgomery Square'), (b'MW', b'Manor Woods'), (b'NCC', b'North Chevy Chase'), (b'NGV', b'Norbeck Grove'), (b'NH', b'Norbeck Hills'), (b'NMC', b'New Mark Commons'), (b'NO', b'North Creek'), (b'NWB', b'Northwest Branch'), (b'OF', b'Old Farm'), (b'OG', b'Old Georgetown'), (b'OM', b'Olney Mill'), (b'P', b'Parkland'), (b'PA', b'Palisades'), (b'PGL', b'Potomac Glen'), (b'PL', b'Poolesville'), (b'PLT', b'Plantations'), (b'PO', b'Potomac'), (b'PW', b'Potomac Woods'), (b'QO', b'Quince Orchard'), (b'QV', b'Quail Valley'), (b'RC', b'Rock Creek'), (b'RE', b'Regency Estates'), (b'RF', b'River Falls'), (b'RH', b'Robin Hood'), (b'RS', b'Rockshire'), (b'RV', b'Rockville'), (b'SB', b'Stonebridge'), (b'SG', b'Stonegate'), (b'SL', b'Seven Locks'), (b'SO', b'Somerset'), (b'TA', b'Tanterra'), (b'TB', b'Twinbrook'), (b'TF', b'Twin Farms'), (b'TH', b'Tallyho'), (b'TN', b'Tanglewood'), (b'TW', b'Tilden Woods'), (b'UC', b'Upper County'), (b'W', b'Whetstone'), (b'WCF', b'Woodcliffe'), (b'WG', b'Woodley Gardens'), (b'WHI', b'West Hillandale'), (b'WL', b'Westleigh'), (b'WLP', b'Willows Of Potomac'), (b'WM', b'Wildwood Manor'), (b'WTL', b'Waters Landing'), (b'WW', b'Wheaton Woods'), (b'WWD', b'Washingtonian Woods')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
