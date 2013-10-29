/* Sample Code for Creating SQL Data Warehouse for Alexandria Community Indicators */

/* CREATE GEOGRAPHY TABLES */
/* Not all geographies necessary right now for Alexandria -- future-proofing */

/*REGION*/
Create table region_fips (
region_fips varchar(1) NOT NULL,
region_name varchar(9) NOT NULL,
Primary key (region_fips)
);

/*DIVISION*/
Create table divis_fips (
divis_fips varchar(1) NOT NULL,
divis_name varchar(18) NOT NULL,
region_fips varchar(1) NOT NULL,
Primary key (divis_fips),
foreign key (region_fips) references region_fips(region_fips)
);

/*STATE*/
Create table state_fips (
state_fips varchar(2) NOT NULL,
state_name varchar(20) NOT NULL,
state_abbrev varchar(2) NOT NULL,
Primary key (state_fips)
);

/*METRO*/
create table metro_fips (
metro_fips varchar(5) NOT NULL,
metro_name varchar(125) NOT NULL,
primary key (metro_fips)
);

/*METRO DIVISION*/
create table metdiv_fips (
metdiv_fips varchar(5) NOT NULL,
metdiv_name varchar(125) NOT NULL,
metro_fips varchar(5) NOT NULL,
primary key (metdiv_fips),
foreign key (metro_fips) references metro_fips(metro_fips)
);

/*COUNTY*/
create table county_fips (
county_fips varchar(5) NOT NULL,
county_name varchar(50) NOT NULL,
primary key (county_fips)
);

/*TRACT*/
create table tract_fips (
tract_fips varchar(11) NOT NULL,
county_fips varchar(5) NOT NULL,
primary key (tract_fips),
foreign key (county_fips) references county_fips(county_fips)
);

/*BLOCK GROUP*/
create table blkgrp_fips (
blkgrp_fips varchar(12) NOT NULL,
tract_fips varchar(11) NOT NULL,
primary key (blkgrp_fips),
foreign key (tract_fips) references tract_fips(tract_fips)
);

/*GEOGRAPHY LEVEL*/
create table geolevel (
geolevel integer NOT NULL,
geolevel_name varchar(30) NOT NULL,
primary key (geolevel)
);

/*Create geography table*/
Create table geography (
geo_id integer NOT NULL,
geo_name varchar(125) NOT NULL,
geolevel integer NOT NULL,
country varchar(2),
region_fips varchar(1),
divis_fips varchar(1),
state_fips varchar(2),
metro_fips varchar(5),
metdiv_fips varchar(5),
county_fips varchar(5),
tract_fips varchar(11),
blkgrp_fips varchar(12),
Primary key (geo_id),
foreign key (geolevel) references geolevel(geolevel),
foreign key (region_fips) references region_fips(region_fips),
foreign key (divis_fips) references divis_fips(divis_fips),
foreign key (state_fips) references state_fips(state_fips),
foreign key (metro_fips) references metro_fips(metro_fips),
foreign key (metdiv_fips) references metdiv_fips(metdiv_fips),
foreign key (county_fips) references county_fips(county_fips),
foreign key (tract_fips) references tract_fips(tract_fips),
foreign key (blkgrp_fips) references blkgrp_fips(blkgrp_fips)
);

/*Create theme table*/
create table theme (
theme_id integer NOT NULL,
theme_name varchar(32) NOT NULL,
theme_desc varchar(255) NOT NULL,
Primary key (theme_id)
);

/*Create time_period table*/
create table time_period (
time_id integer NOT NULL,
time_year integer NOT NULL,
time_quarter integer NOT NULL,
time_month integer NOT NULL,
Primary key (time_id)
);

/*Create data source table*/
create table data_source (
source_id integer NOT NULL,
source_name varchar(15) NOT NULL,
source_desc varchar(100) NOT NULL,
Primary key (source_id)
);

/*Create indicator type table*/
create table indicator_type (
indic_id integer NOT NULL,
indic_name varchar(32) NOT NULL,
indic_desc varchar(300) NOT NULL,
theme_id integer NOT NULL,
indic_avail varchar(14) NOT NULL,
indic_quality varchar(14) NOT NULL,
indic_spatial varchar(3) NOT NULL,
indic_freq varchar(20) NOT NULL,
indic_notes varchar(500) NULL,
Primary key (indic_id),
foreign key (theme_id) references theme(theme_id)
);

/*Create indicator value table*/
create table indicator_value (
indic_value decimal(38,5),
geo_id integer NOT NULL,
time_id integer NOT NULL,
indic_id integer NOT NULL,
primary key (geo_id,time_id,indic_id),
foreign key (geo_id) references geography(geo_id),
foreign key (time_id) references time_period(time_id),
foreign key (indic_id) references indicator_type(indic_id)
);

/* Code below should be replaced with code to import CSV files containing these data points */

/*insert records into REGION table*/
insert into region_fips values (1,'Northeast');
insert into region_fips values (2,'South');
insert into region_fips values (3,'Midwest');
insert into region_fips values (4,'West');

/*insert records into THEME table*/
insert into theme values (1,'Sense of community','An Alexandria where building a sense of community and helping one another are essential');
insert into theme values (2,'Basic needs','An Alexandria where meeting basic needs such as food, clothing, shelter, and affordable housing is a priority for each individual');
insert into theme values (3,'Diversity','An Alexandria that celebrates racial, ethnic, and gender diversity and supports people of all ages, abilities, and sexual orientation');
insert into theme values (4,'Access to health care','An Alexandria where all residents, regardless of their ability to pay, can access quality health care that focuses on prevention, treatment, and wellness');
insert into theme values (5,'Built environment','An Alexandria where everyone has access to transportation options, trails, parks, open space and recreation opportunities');
insert into theme values (6,'Crime and safety','An Alexandria where people are safe in their homes and walking in their neighborhoods, unafraid of crime, violence and domestic abuse');
insert into theme values (7,'Mental health','An Alexandria where safeguarding emotional and mental health is a priority and there is adequate provision of mental health services');
insert into theme values (8,'Substance abuse prevention','An Alexandria where its residents support and are engaged in efforts to prevent the abuse of alcohol, tobacco and other drugs and where treatment for substance use problems is readily available');
insert into theme values (9,'Food and nutrition','An Alexandria where all residents can access safe and healthy foods and are able to practice healthy eating habits');
insert into theme values (10,'Cleanliness and beautification','An Alexandria where our houses, streets, neighborhoods and parks are clean and well-kept, as well as free of garbage, environmental hazards, and pests so that everyone can fully enjoy our beautiful city');
insert into theme values (11,'Employment opportunities','An Alexandria where meaningful employment opportunities are available to all');

/*insert records into TIME_PERIOD table*/
insert into time_period values (1,2000,0,0);
insert into time_period values (2,2000,1,1);
insert into time_period values (3,2000,1,2);
insert into time_period values (4,2000,1,3);
insert into time_period values (5,2000,2,4);
insert into time_period values (6,2000,2,5);
insert into time_period values (7,2000,2,6);
insert into time_period values (8,2000,3,7);
insert into time_period values (9,2000,3,8);
insert into time_period values (10,2000,3,9);
insert into time_period values (11,2000,4,10);
insert into time_period values (12,2000,4,11);
insert into time_period values (13,2000,4,12);
insert into time_period values (14,2001,0,0);
insert into time_period values (15,2001,1,1);
insert into time_period values (16,2001,1,2);
insert into time_period values (17,2001,1,3);
insert into time_period values (18,2001,2,4);
insert into time_period values (19,2001,2,5);
insert into time_period values (20,2001,2,6);
insert into time_period values (21,2001,3,7);
insert into time_period values (22,2001,3,8);
insert into time_period values (23,2001,3,9);
insert into time_period values (24,2001,4,10);
insert into time_period values (25,2001,4,11);
insert into time_period values (26,2001,4,12);
insert into time_period values (27,2002,0,0);
insert into time_period values (28,2002,1,1);
insert into time_period values (29,2002,1,2);
insert into time_period values (30,2002,1,3);
insert into time_period values (31,2002,2,4);
insert into time_period values (32,2002,2,5);
insert into time_period values (33,2002,2,6);
insert into time_period values (34,2002,3,7);
insert into time_period values (35,2002,3,8);
insert into time_period values (36,2002,3,9);
insert into time_period values (37,2002,4,10);
insert into time_period values (38,2002,4,11);
insert into time_period values (39,2002,4,12);

insert into time_period values (40,2003,0,0);
insert into time_period values (41,2003,1,1);
insert into time_period values (42,2003,1,2);
insert into time_period values (43,2003,1,3);
insert into time_period values (44,2003,2,4);
insert into time_period values (45,2003,2,5);
insert into time_period values (46,2003,2,6);
insert into time_period values (47,2003,3,7);
insert into time_period values (48,2003,3,8);
insert into time_period values (49,2003,3,9);
insert into time_period values (50,2003,4,10);
insert into time_period values (51,2003,4,11);
insert into time_period values (52,2003,4,12);

insert into time_period values (53,2004,0,0);
insert into time_period values (54,2004,1,1);
insert into time_period values (55,2004,1,2);
insert into time_period values (56,2004,1,3);
insert into time_period values (57,2004,2,4);
insert into time_period values (58,2004,2,5);
insert into time_period values (59,2004,2,6);
insert into time_period values (60,2004,3,7);
insert into time_period values (61,2004,3,8);
insert into time_period values (62,2004,3,9);
insert into time_period values (63,2004,4,10);
insert into time_period values (64,2004,4,11);
insert into time_period values (65,2004,4,12);

insert into time_period values (66,2005,0,0);
insert into time_period values (67,2005,1,1);
insert into time_period values (68,2005,1,2);
insert into time_period values (69,2005,1,3);
insert into time_period values (70,2005,2,4);
insert into time_period values (71,2005,2,5);
insert into time_period values (72,2005,2,6);
insert into time_period values (73,2005,3,7);
insert into time_period values (74,2005,3,8);
insert into time_period values (75,2005,3,9);
insert into time_period values (76,2005,4,10);
insert into time_period values (77,2005,4,11);
insert into time_period values (78,2005,4,12);

insert into time_period values (79,2006,0,0);
insert into time_period values (80,2006,1,1);
insert into time_period values (81,2006,1,2);
insert into time_period values (82,2006,1,3);
insert into time_period values (83,2006,2,4);
insert into time_period values (84,2006,2,5);
insert into time_period values (85,2006,2,6);
insert into time_period values (86,2006,3,7);
insert into time_period values (87,2006,3,8);
insert into time_period values (88,2006,3,9);
insert into time_period values (89,2006,4,10);
insert into time_period values (90,2006,4,11);
insert into time_period values (91,2006,4,12);

insert into time_period values (92,2007,0,0);
insert into time_period values (93,2007,1,1);
insert into time_period values (94,2007,1,2);
insert into time_period values (95,2007,1,3);
insert into time_period values (96,2007,2,4);
insert into time_period values (97,2007,2,5);
insert into time_period values (98,2007,2,6);
insert into time_period values (99,2007,3,7);
insert into time_period values (100,2007,3,8);
insert into time_period values (101,2007,3,9);
insert into time_period values (102,2007,4,10);
insert into time_period values (103,2007,4,11);
insert into time_period values (104,2007,4,12);

insert into time_period values (105,2008,0,0);
insert into time_period values (106,2008,1,1);
insert into time_period values (107,2008,1,2);
insert into time_period values (108,2008,1,3);
insert into time_period values (109,2008,2,4);
insert into time_period values (110,2008,2,5);
insert into time_period values (111,2008,2,6);
insert into time_period values (112,2008,3,7);
insert into time_period values (113,2008,3,8);
insert into time_period values (114,2008,3,9);
insert into time_period values (115,2008,4,10);
insert into time_period values (116,2008,4,11);
insert into time_period values (117,2008,4,12);

insert into time_period values (118,2009,0,0);
insert into time_period values (119,2009,1,1);
insert into time_period values (120,2009,1,2);
insert into time_period values (121,2009,1,3);
insert into time_period values (122,2009,2,4);
insert into time_period values (123,2009,2,5);
insert into time_period values (124,2009,2,6);
insert into time_period values (125,2009,3,7);
insert into time_period values (126,2009,3,8);
insert into time_period values (127,2009,3,9);
insert into time_period values (128,2009,4,10);
insert into time_period values (129,2009,4,11);
insert into time_period values (130,2009,4,12);

insert into time_period values (131,2010,0,0);
insert into time_period values (132,2010,1,1);
insert into time_period values (133,2010,1,2);
insert into time_period values (134,2010,1,3);
insert into time_period values (135,2010,2,4);
insert into time_period values (136,2010,2,5);
insert into time_period values (137,2010,2,6);
insert into time_period values (138,2010,3,7);
insert into time_period values (139,2010,3,8);
insert into time_period values (140,2010,3,9);
insert into time_period values (141,2010,4,10);
insert into time_period values (142,2010,4,11);
insert into time_period values (143,2010,4,12);

/*new rows added 11-23-2012*/
insert into time_period values (144,2011,0,0);
insert into time_period values (145,2011,1,1);
insert into time_period values (146,2011,1,2);
insert into time_period values (147,2011,1,3);
insert into time_period values (148,2011,2,4);
insert into time_period values (149,2011,2,5);
insert into time_period values (150,2011,2,6);
insert into time_period values (151,2011,3,7);
insert into time_period values (152,2011,3,8);
insert into time_period values (153,2011,3,9);
insert into time_period values (154,2011,4,10);
insert into time_period values (155,2011,4,11);
insert into time_period values (156,2011,4,12);
insert into time_period values (157,2012,0,0);
insert into time_period values (158,2012,1,1);
insert into time_period values (159,2012,1,2);
insert into time_period values (160,2012,1,3);
insert into time_period values (161,2012,2,4);
insert into time_period values (162,2012,2,5);
insert into time_period values (163,2012,2,6);
insert into time_period values (164,2012,3,7);
insert into time_period values (165,2012,3,8);
insert into time_period values (166,2012,3,9);
insert into time_period values (167,2012,4,10);
insert into time_period values (168,2012,4,11);
insert into time_period values (169,2012,4,12);
insert into time_period values (170,2013,0,0);
insert into time_period values (171,2013,1,1);
insert into time_period values (172,2013,1,2);
insert into time_period values (173,2013,1,3);
insert into time_period values (174,2013,2,4);
insert into time_period values (175,2013,2,5);
insert into time_period values (176,2013,2,6);
insert into time_period values (177,2013,3,7);
insert into time_period values (178,2013,3,8);
insert into time_period values (179,2013,3,9);
insert into time_period values (180,2013,4,10);
insert into time_period values (181,2013,4,11);
insert into time_period values (182,2013,4,12);




/*insert records into DATA_SOURCE table*/
insert into data_source values (1,'ACS','American Community Survey');
insert into data_source values (2,'Census','Decennial Census');
insert into data_source values (3,'HSCC','Homeless Services Coordinating Committee');
insert into data_source values (4,'MCOG','Metropolitan Washington Council of Governments');
insert into data_source values (5,'ADH','Alexandria Department of Housing');
insert into data_source values (6,'ADF','Alexandria Department of Finance');
insert into data_source values (7,'VDSS','Virginia Department of Social Services');
insert into data_source values (8,'ACPS','Alexandria City Public Schools');
insert into data_source values (9,'VDE','Virginia Department of Education');
insert into data_source values (10,'FNS','US Department of Agriculture, Food and Nutrition Service');
/*new rows added 11-23-2012*/
insert into data_source values (11,'DAS','Developmental Assets Survey, Alexandria City Public Schools');
insert into data_source values (12,'OHR','Office of Human Rights, City of Alexandria');
insert into data_source values (13,'BRFSS','Virginia Behavioral Risk Factor Surveillance System');
insert into data_source values (14,'VDH','Virginia Department of Health');
insert into data_source values (15,'VDMAS','Virginia Department of Medical Assistance Services');
insert into data_source values (16,'VDHS','Virginia Department of Health Statistics');
insert into data_source values (17,'GIS','GIS Division, Department of Planning and Zoning, City of Alexandria');
insert into data_source values (18,'DTES','Department of Transportation and Environmental Services, City of Alexandria');
insert into data_source values (19,'DRPCA','Department of Recreation, Parks, and Cultural Activities, City of Alexandria');
insert into data_source values (20,'ADCHS','Alexandria Department of Community and Human Services');
insert into data_source values (21,'CCFCWS','Center for Children and Families, Child Welfare Services');
insert into data_source values (22,'APD','Alexandria Police Department');
insert into data_source values (23,'YRBSS','Youth Risk Behavior Surveillance System, Alexandria City Public Schools');
insert into data_source values (24,'CDC','Centers for Disease Control and Prevention');
insert into data_source values (25,'SAMHSA','Substance Abuse and Mental Health Services Administration');
insert into data_source values (26,'ADHEHD','Alexandria Department of Health, Environmental Health Division');
insert into data_source values (27,'AOEQ','Alexandria Office of Environmental Quality');
insert into data_source values (28,'VAWC','Virginia American Water Company');
insert into data_source values (29,'ODW','Office of Drinking Water, Virginia Department of Health');
insert into data_source values (30,'VEC','Virginia Employment Commission');
insert into data_source values (31,'CAFR','City of Alexandria Financial Report');
insert into data_source values (32,'BLS','US Department of Labor, Bureau of Labor Statistics');
insert into data_source values (33,'AEDP','Alexandria Economic Development Partnership');

/*insert records into INDICATOR_TYPE table*/
insert into indicator_type values (101,'Pct_Res_StrongCommunity','Percentage of residents who report a strong sense of community',1,'2','5','0','3','');
insert into indicator_type values (102,'Pct_Res_Volunteer','Percentage of residents who report volunteering in the last 12 months',1,'2','5','0','3','');
insert into indicator_type values (201,'Pct_Inc_HsgCost','Percentage of income paid toward housing',2,'1','4','1','1','');
insert into indicator_type values (202,'Num_HomelessPersons','Number of homeless persons',2,'1','4','0','1','');
insert into indicator_type values (203,'Num_HsgUnits_50PctMedian','Number of housing units available for households earning below 50% of median income',2,'1','4','1','1','');
insert into indicator_type values (204,'Median_GrossRent','Median gross rent',2,'1','4','1','1','');
insert into indicator_type values (205,'Num_RealEstate_Foreclosures','Number of Real Estate foreclosures',2,'1','4','1','1','');
insert into indicator_type values (206,'Num_Res_FoodStamps','Number of Food Stamp recipients',2,'1','4','0','1','');
insert into indicator_type values (207,'Pct_Stud_FreeRedCostMeals','Percentage of ACPS children eligible to receive free and reduced cost meals at school',2,'1','4','1','1','');
insert into indicator_type values (301,'Pct_Youth_Encouraged','Percentage of youth who feel encouraged by adults',3,'1','2','0','2','');
insert into indicator_type values (302,'Pct_Commissions_Reflect_Demog','City commissions that reflect demographic makeup of Alexandria',3,'3','2','0','3','');
insert into indicator_type values (303,'Tolerance_Index','Tolerance index',3,'2','2','0','3','');

/*new rows added 11-23-2012*/
insert into indicator_type values (401,'Pct_Adults_with_Healthcare','Percentage of adults who currently report having any kind of health care coverage',4,'1','2','0','2','');
insert into indicator_type values (402,'Num_Child_SCHIP','Number of children participating in the State Childrens Health Insurance Program (SCHIP)',4,'1','4','2','1','');
insert into indicator_type values (403,'Pct_Res_NoDoctor_Due_to_Cost','Percentage of people indicating they needed to see a doctor in the past year and could not due to cost',4,'1','2','0','2','');
insert into indicator_type values (404,'Pct_Prenatal_1stTrimester','Percentage of women who received prenatal care in the first trimester of pregnancy',4,'1','4','0','1','');
insert into indicator_type values (405,'Rate_NewHIVCases_100000','Number of newly diagnosed cases of HIV per 100,000 population',4,'1','4','2','1','');
insert into indicator_type values (406,'Pct_Adults_Health_GoodExcellent','Percentage of adults who rated their health good to excellent',4,'1','4','2','1','');
insert into indicator_type values (407,'Pct_Adults_Got_FluVaccine','Percentage of adults who received seasonal influenza vaccine',4,'1','4','0','2','');
insert into indicator_type values (408,'Pct_Adults_OverweightObese','Percentage of adults overweight or obese',4,'1','3','0','2','');
insert into indicator_type values (409,'Rate_HeartDiseaseMortal_100000','Heart disease mortality rate per 100,000 population',4,'1','3','0','2','');
insert into indicator_type values (410,'Rate_CancerMortality_100000','Cancer mortality rate per 100,000',4,'1','4','0','1','');
insert into indicator_type values (411,'Rate_InfantMortality_1000','Infant mortality per 1000 live births',4,'1','4','0','1','');
insert into indicator_type values (412,'Pct_Women_Prenatal_1stTri','Percentage of women who received prenatal care in the first trimester of pregnancy',4,'1','3','0','1','');
insert into indicator_type values (413,'Rate_TeenPregnancy_1000','Teen pregnancy rate',4,'1','3','0','1','');
insert into indicator_type values (5011,'Pct_Res_WalktoWork','Percentage of Alexandria residents walking to work',5,'1','3','1','1','');
insert into indicator_type values (5012,'Pct_Res_BiketoWork','Percentage of Alexandria residents who bike to work',5,'1','3','1','1','');
insert into indicator_type values (502,'Pct_TreeCanopyCoverage','Percentage of tree canopy coverage',5,'1','3','1','2','');
insert into indicator_type values (503,'Pct_Res_LiveNearPublicTransit','Percentage of residents who live within a walkable quarter mile of a public transportation point',5,'1','4','1','1','');
insert into indicator_type values (504,'Miles_SharedUsePaths','Miles of designated shared-use paths and bike lanes relative to street miles',5,'1','3','0','2','');
insert into indicator_type values (505,'Rate_OpenSpaceAcres_1000','Open space acres per 1000 residents',5,'3','3','0','2','');
insert into indicator_type values (506,'Pct_Res_TakePublicTransit_Work','Percentage of residents who take public transportation to work',5,'1','4','1','1','');
insert into indicator_type values (601,'Num_ChildAbuseInvestigations','Child abuse and neglect investigations with a founded disposition',6,'1','3','2','1','');
insert into indicator_type values (602,'Num_Perceive_PhysicalSafety','Perception of physical safety in the community',6,'2','5','2','3','');
insert into indicator_type values (603,'Num_MajorCrimes_Total','Number of major crimes',6,'1','4','1','1','Can break down into 7 categories');
insert into indicator_type values (604,'Num_NuisanceCrimes','Number of nuisance crimes',6,'1','4','1','1','');
insert into indicator_type values (605,'Avg_ResponseTime_StructureFires','Average response time in minutes to Alexandria structure fires',6,'1','3','0','1','');
insert into indicator_type values (606,'Pct_DisasterSupplyKit_Prepared','Percentage of population reporting a Disaster Supply Kit with emergency supplies such as water, food, and medicine has been prepared in home',6,'2','5','0','3','');
insert into indicator_type values (701,'Pct_Adults_Depress_Get_Care','Percentage of adults with recognized depression who receive treatment',7,'2','5','0','3','');
insert into indicator_type values (702,'Pct_Adults_Got_MentalHealthCare','Percentage of adults needing mental health care who stated that they did obtain professional help for emotional or mental health issues in the past year',7,'2','5','0','3','');
insert into indicator_type values (703,'Pct_Stud_Considered_Suicide','Percentage of adolescents who reported that they have seriously considered suicide',7,'1','2','0','2','');
insert into indicator_type values (704,'Num_MentallyUnhealthyDays_Last30','Mentally unhealthy days during the last 30 days',7,'1','2','0','2','');
insert into indicator_type values (801,'Pct_Adults_Smoke','Percentage of adults who smoke cigarettes',8,'1','3','0','2','');
insert into indicator_type values (802,'Pct_Youth_NeverSmoked','Percentage of youth who never smoked cigarettes',8,'1','2','0','2','');
insert into indicator_type values (803,'Pct_Youth_Used_Alcohol_Last30','Percentage of adolescents who report having used alcohol in the past 30 days',8,'1','2','0','2','Broken out by grade, 7-12');
insert into indicator_type values (804,'Pct_Youth_Used_IllicitRx','Percentage of youth who report illicitly using prescription drugs',8,'3','2','0','3','');
insert into indicator_type values (805,'Pct_Res_SpecTrtmnt_SubAbuse','Percentage of residents who received specialty treatment for substance abuse or dependence',8,'3','2','0','3','');
insert into indicator_type values (901,'Pct_Adults_Eat_5Plus_FruitsVeg','Percentage of adults eating 5 or more fruits or vegetables a day',9,'1','2','0','2','');
insert into indicator_type values (902,'Pct_Tracts_HealthierFoodRetail','Percentage of Alexandria Census tracts that have healthier daily food retailers located within the tract or within one-half mile of tract boundaries',9,'1','3','1','3','');
insert into indicator_type values (903,'Pct_Res_Participate_WIC','Percentage of residents participating in the WIC program',9,'1','4','0','1','');
insert into indicator_type values (904,'Avg_Num_FoodSafety_Violations','Average number of critical violations per food establishment inspection in Alexandria',9,'1','3','0','1','');
insert into indicator_type values (1001,'Num_AirQualityActionDays','Number of air quality action days',10,'1','4','0','1','');
insert into indicator_type values (1002,'Num_Hazard_Pest_Complaints','Number of environmental hazards and pests complaints',10,'1','3','0','1','');
insert into indicator_type values (1003,'Pct_SolidWaste_Recycled','Percentage of solid waste recycled',10,'1','3','0','2','');
insert into indicator_type values (1004,'Num_WaterQuality_Violations','Number of water quality violations',10,'1','4','0','1','');
insert into indicator_type values (1101,'Median_Household_Income','Median household income',11,'1','4','1','1','');
insert into indicator_type values (1102,'Pct_Age16_64_In_Workforce','Percentage of population ages 16-64 in the workforce',11,'1','4','1','1','');
insert into indicator_type values (1103,'Pct_Res_BelowPoverty','Percentage of population below the poverty level',11,'1','4','1','1','');
insert into indicator_type values (1104,'Rate_OnTimeGraduation','ACPS On-Time Graduation Rate',11,'1','2','0','1','');
insert into indicator_type values (1105,'Pct_Res_Unemployed','Prevalence of local unemployment',11,'1','4','0','1','');
insert into indicator_type values (1106,'Pct_Adults_Diploma_or_GED','Percentage of adults with at least a high school diploma or general education diploma',11,'1','4','1','1','');
insert into indicator_type values (1107,'Pct_Retail_Occupancy','Percentage retail occupancy',11,'3','1','0','1','');
