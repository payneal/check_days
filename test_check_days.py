import unittest
import json
from check_days import Check_days

class Test_Check_Days(unittest.TestCase):
    
    def setUp(self):
        self.check_days = Check_days()
        self.january_2015 = {
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

    def tearDown(self):
        pass

    def test_get_days_in_week_that_is_valid(self):
        jan_info = self.check_days.days_in_month(2015, 1)
        expected = self.january_2015
        self.assertDictEqual(jan_info, expected)
    
    def test_get_months_in_year(self):
        year_info = self.check_days.months_in_year(2015)
        self.assertEqual(year_info[1][27]["dow"], "Tuesday")
        self.assertEqual(year_info[2][15]["dow"], "Sunday")
        self.assertEqual(year_info[3][16]["dow"], "Monday")
        self.assertEqual(year_info[4][30]["dow"], "Thursday")
        self.assertEqual(year_info[5][5]["dow"], "Tuesday")
        self.assertEqual(year_info[6][18]["dow"], "Thursday")
        self.assertEqual(year_info[7][4]["dow"], "Saturday")
        self.assertEqual(year_info[8][12]["dow"], "Wednesday")
        self.assertEqual(year_info[9][15]["dow"], "Tuesday")
        self.assertEqual(year_info[10][10]["dow"], "Saturday")
        self.assertEqual(year_info[11][30]["dow"], "Monday")
        self.assertEqual(year_info[12][31]["dow"], "Thursday")
       
    def test_get_years_bad(self):
        years = self.check_days.add_years(2018, 2015)
        self.assertEqual(years, "invalid")

    def test_get_years(self):
        self.check_days.add_years(2015, 2018)
        self.assertEqual(self.check_days.results[2015][1][27]["dow"], "Tuesday")
        self.assertEqual(self.check_days.results[2016][1][27]["dow"], "Wednesday")
        self.assertEqual(self.check_days.results[2017][1][27]["dow"], "Friday")
        self.assertEqual(self.check_days.results[2018][1][27]["dow"], "Saturday")


    def test_adding_data_to_calendar(self):
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
        self.check_days.add_years(2015, 2018)
        self.check_days.add_data("cim_account_h", insert['cim_account_h'])
        
        self.assertEqual(
            self.check_days.results[2017][1][2]['data']['cim_account_h'], 'recieved')
        self.assertEqual(
            self.check_days.results[2018][2][2]['data']['cim_account_h'], 'recieved')
        

        self.check_days.add_data("another_test", insert['another_test'])
        self.assertEqual(
            self.check_days.results[2017][10][2]['data']['another_test'], 'recieved')
        self.assertEqual(
            self.check_days.results[2018][12][2]['data']['another_test'], 'recieved')
    
        self.assertEqual(
            ['cim_account_h', "another_test"], self.check_days.tables_used) 


    def test_checking_which_dates_missing(self):
        insert = {
            "cim_account_h": [
                {"month": 1, "day": 2, "year": 2015},
                {"month": 2, "day": 2, "year": 2015}
            ]
        }
        self.check_days.add_years(2015, 2016)
        self.check_days.add_data("cim_account_h", insert['cim_account_h'])
        expected = {"cim_account_h": ["2015-1-2", "2015-2-2"]}
        day_recieved, not_recieved= self.check_days.get_days_data_recieved()
        
        self.assertDictEqual(expected, day_recieved)    
        self.assertListEqual(expected["cim_account_h"], day_recieved["cim_account_h"])

if __name__ == "__main__":
    unittest.main()
