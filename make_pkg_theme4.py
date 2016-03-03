#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import urllib
import json
import pprint
import ckan_api
from make_pkg import make_pkg


ind4_1 = {
    "name" : "pct-adults-w-healthcare",
    "title" : "Percent of Adults with Health Coverage",
    "groups" : [{"name" : "access-to-health-care"}],
    "notes" : "Indicator: % of adults ages 18-64 who currently report having any kind of health care coverage. Source: BRFSS. Question: Do you have any kind of health care coverage, including health insurance, prepaid plans such as HMOs or government plans such as Medicare?",
}

ind4_2 = {
    "name" : "num-schip-participants",
    "title" : "Number SCHIP Participants",
    "groups" : [{"name" : "access-to-health-care"}],
    "notes" : "Indicator: # Alexandria's children participating in the federal State Children’s Health Insurance Program (SCHIP). Source: Virginia Department of Health, Division of Health Statistics",
}

ind4_3 = {
    "name" : "pct-deferred-care",
    "title" : "Percent People Deferring Health Care",
    "groups" : [{"name" : "access-to-health-care"}],
    "notes" : "Indicator: % of people indicating they needed to see a doctor in the past year and could not due to cost. Source: BRFSS",
}

ind4_4 = {
    "name" : "pct-prenatal-care",
    "title" : "Percent Women Receiving Prenatal Care",
    "groups" : [{"name" : "access-to-health-care"}],
    "notes" : "Indicator: % of women who received prenatal care in the first trimester of pregnancy. Source: Virginia Department of Health, Division of Health Statistics. http://www.vdh.state.va.us/epidemiology/DiseasePrevention/DAta/Quarterly/2nd%20Quarter%202011/Table6HIV_Q2.pdf",
}

ind4_5 = {
    "name" : "rate-new-hiv",
    "title" : "Rate of New HIV Diagnoses",
    "groups" : [{"name" : "access-to-health-care"}],
    "notes" : "Indicator: The total annual number of newly diagnosed cases of HIV per 100,000 people in the population. Source: Virginia Department of Health, Division of Health Statistics, http://www.vdh.state.va.us/epidemiology/DiseasePrevention/DAta/Quarterly/2nd%20Quarter%202011/Table6HIV_Q2.pdf",
}

ind4_6 = {
    "name" : "good-health",
    "title" : "Adults Reporting Good to Excellent Health",
    "groups" : [{"name" : "access-to-health-care"}],
    "notes" : "Indicator: % of adults who rated their health good to excellent. Source: BRFSS",
}

ind4_7 = {
    "name" : "flu-shot",
    "title" : "Percent Adults Receiving Flu Shot",
    "groups" : [{"name" : "access-to-health-care"}],
    "notes" : "Indicator: % adults who received seasonal influenza vaccine in past 12 months. Source: BRFSS",
}

ind4_8 = {
    "name" : "overweight",
    "title" : "Percent Adults Overweight or Obese",
    "groups" : [{"name" : "access-to-health-care"}],
    "notes" : "Indicator: % of adults overweight or obese in the population. Source: BRFSS",
}

ind4_10 = {
    "name" : "heart-mortality",
    "title" : "Rate of Heart Disease Mortality",
    "groups" : [{"name" : "access-to-health-care"}],
    "notes" : "Indicator: Heart Disease Mortality Rate. Source: Virginia Department of Health, Health Profile, Alexandria City, 2000-2009",
}

ind4_11 = {
    "name" : "cancer-mortality",
    "title" : "Rate of Cancer Mortality",
    "groups" : [{"name" : "access-to-health-care"}],
    "notes" : "Indicator: Cancer Mortality Rate. Source: Virginia Department of Health, Division of Health Statistics",
}

ind4_12 = {
    "name" : "infant-mortality",
    "title" : "Rate of Infant Mortality",
    "groups" : [{"name" : "access-to-health-care"}],
    "notes" : "Indicator: Infant mortality rate per 1,000 live births. Source: Virginia Department of Health, Health Profile, Alexandria City, 2000-2009",
}

ind4_13 = {
    "name" : "teen-pregnancy",
    "title" : "Rate of Teen Pregnancy",
    "groups" : [{"name" : "access-to-health-care"}],
    "notes" : "Indicator: Teen Pregnancy Rate (per 1000 girls). Source: Virginia Department of Health, Health Profile, Alexandria City, 2000-2009",
}

make_pkg(ind4_1)
make_pkg(ind4_2)
make_pkg(ind4_3)
make_pkg(ind4_4)
make_pkg(ind4_5)
make_pkg(ind4_6)
make_pkg(ind4_7)
make_pkg(ind4_8)
make_pkg(ind4_10)
make_pkg(ind4_11)
make_pkg(ind4_12)
make_pkg(ind4_13)
