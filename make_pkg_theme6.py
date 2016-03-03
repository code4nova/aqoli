#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import urllib
import json
import pprint
import ckan_api
from make_pkg import make_pkg


ind6_1 = {
    "name" : "child-abuse",
    "title" : "Child Abuse Rate",
    "groups" : [{"name" : "crime-and-safety"}],
    "notes" : "Indicator: Rate of substantiated cases of child abuse and neglect per 1,000 Alexandria children. Source: Alexandria Department of Community and Human Services (ADCHS), Center for Children and Families, Child Welfare Services",
}

ind6_3 = {
    "name" : "violent-property-crimes",
    "title" : "Violent and Property Crimes (Part 1)",
    "groups" : [{"name" : "crime-and-safety"}],
    "notes" : "Source: Alexandria Police Department",
}

ind6_4 = {
    "name" : "nuisance-crimes",
    "title" : "Nuisance Crimes",
    "groups" : [{"name" : "crime-and-safety"}],
    "notes" : "Source: Alexandria Police Department",
}

ind6_5 = {
    "name" : "fire-response",
    "title" : "Fire Response Time",
    "groups" : [{"name" : "crime-and-safety"}],
    "notes" : "Indicator: Percentage of residential fires confined to room of origin. Source: Alexandria Fire/EMS",
}

make_pkg(ind6_1)
make_pkg(ind6_3)
make_pkg(ind6_4)
make_pkg(ind6_5)