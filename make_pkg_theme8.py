#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import urllib
import json
import pprint
import ckan_api
from make_pkg import make_pkg


ind8_1 = {
    "name" : "adult-smokers",
    "title" : "Adult Smokers",
    "groups" : [{"name" : "substance-abuse-prevention"}],
    "notes" : "Indicator: % of current adult smokers. Source: BRFSS",
}

ind8_2 = {
    "name" : "youth-smoking",
    "title" : "Youth Smoking",
    "groups" : [{"name" : "substance-abuse-prevention"}],
    "notes" : "Indicator: % of youth (grades 7-12) who have never smoked cigarettes in their lifetime. Source: ACPS (http://www.acps.k12.va.us/mes/reports/20070301_youthprofile_appendix.pdf)",
}

ind8_3 = {
    "name" : "youth-drinking",
    "title" : "Youth Drinking",
    "groups" : [{"name" : "substance-abuse-prevention"}],
    "notes" : "Indicator: % adolescents who report having used alcohol in past 30 days. Source: ACPS (http://www.acps.k12.va.us/mes/reports/20070301_youthprofile_appendix.pdf)",
}

make_pkg(ind8_1)
make_pkg(ind8_2)
make_pkg(ind8_3)