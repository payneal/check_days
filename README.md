# check_days
* calendar where you can pass in list  to tell which days data is missing

# how to use check days
```python
 
from check_days import  Check_days
 
check_days = Check_days()
 
# get a json object of any month
january = check_days.days_in_month(2015, 1)
 
print january
/*
{
            1: {
                "dow": "Thursday", 
                "data": {} }, 
            2:{
                "dow": "Friday",
                "data": {} },
            3:{
                "dow": "Saturday",
                "data": {} },
            4: {
                "dow": "Sunday", 
                "data": {} }, 
            5:{
                "dow": "Monday",
                "data": {} },
            6:{
                "dow": "Tuesday",
                "data": {} },
            7:{
                "dow": "Wednesday",
                "data": {} },
            8:{
                "dow": "Thursday",
                "data": {} },
            9:{
                "dow": "Friday",
                "data": {} },
            10:{
                "dow": "Saturday",
                "data": {} },
            11: {
                "dow": "Sunday", 
                "data": {} }, 
            12:{
                "dow": "Monday",
                "data": {} },
            13:{
                "dow": "Tuesday",
                "data": {} },
            14:{
                "dow": "Wednesday",
                "data": {} },
            15:{
                "dow": "Thursday",
                "data": {} },
            16:{
                "dow": "Friday",
                "data": {} },
            17:{
                "dow": "Saturday",
                "data": {} },
            18: {
                "dow": "Sunday", 
                "data": {} }, 
            19:{
                "dow": "Monday",
                "data": {} },
            20:{
                "dow": "Tuesday",
                "data": {} },
            21:{
                "dow": "Wednesday",
                "data": {} },
            22:{
                "dow": "Thursday",
                "data": {} },
            23:{
                "dow": "Friday",
                "data": {} },
            24:{
                "dow": "Saturday",
                "data": {}},
            25: {
                "dow": "Sunday", 
                "data": {}}, 
            26:{
                "dow": "Monday",
                "data": {} },
            27:{
                "dow": "Tuesday",
                "data": {} },
            28:{
                "dow": "Wednesday",
                "data": {} },
            29:{
                "dow": "Thursday",
                "data": {} },
            30:{
                "dow": "Friday",
                "data": {}},
            31:{
                "dow": "Saturday",
                "data": {} }
        }
*/
###########################################################################
# get json object  of year
check_days.add_years(2015, 2016)

print check_days.results
# json of year same as above but all 12months wrapped in year can do for multiple years
 
# add data  to calendar (list)
# ex
insert = {
  "cim_account_h": [
    {"month": 1, "day": 2, "year": 2017},
    {"month": 2, "day": 2, "year": 2018}
  ],
  "another_test": [
    {"month": 10, "day": 2, "year": 2017},
    {"month": 12, "day": 2, "year": 2018}
  ]
}

check_days.add_years(2015, 2018)
check_days.add_data("cim_account_h", insert['cim_account_h'])


print check_days.results[2017][1][2]['data']['cim_account_h']
# will print recieved

print check_days.results[2017][1][2]['data']['another_test']
# will print recieved

###########################################################################

# showing data recieved, or data removed

insert = {
  "cim_account_h": [
    {"month": 1, "day": 2, "year": 2015},
    {"month": 2, "day": 2, "year": 2015}
  ]
}
self.check_days.add_years(2015, 2016)
day_recieved, not_recieved= self.check_days.get_days_data_recieved()

print day_recieved
# { "cim_account_h": ["2015-1-2", "2015-2-2"]}

```
