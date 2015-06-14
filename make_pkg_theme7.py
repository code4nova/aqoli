#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import urllib
import json
import pprint
import ckan_api
from make_pkg import make_pkg


ind7_3 = {
    "name" : "considered-suicide",
    "title" : "Percent of Adolescents Who Reported That They Have Seriously Considered Suicide",
    "groups" : [{"name" : "mental-health"}],
    "notes" : "Source: Alexandria City Public Schools Youth Risk Behavior Survey, 2008 Final Report http://www.acps.k12.va.us/mes/reports/",
}

ind7_4 = {
    "name" : "mentally-unhealthy-days",
    "title" : "Mentally Unhealthy Days",
    "groups" : [{"name" : "mental-health"}],
    "notes" : "Indicator: Mentally Unhealthy Days per Month (mean). Source: BRFSS",
}

make_pkg(ind7_3)
make_pkg(ind7_4)