"""
Created on May 2, 2012

@author: Tyler
"""
import unittest
import sys
sys.path.append("../src/crawler")
from crawler import DBManager

"""
This class runs our unit tests for DBManager.py.
"""
class Test(unittest.TestCase):

    """
    Tests get_country_list to ensure it returns all of the
    countries as intended.
    """
    def test_get_country_list(self):
        expected = ['Falkland Is.', 'French Guiana', 
                    'Guyana', 'Pitcairn Is.', 
                    'South Georgia & the South Sandwich Is.', 
                    'St. Helena', 'Suriname', 'Trinidad & Tobago', 
                    'Venezuela', 'American Samoa', 'Cook Is.', 
                    'French Polynesia', 'Jarvis I.', 'Niue', 
                    'Samoa', 'Tokelau', 'Tonga', 'Wallis & Futuna', 
                    'Argentina', 'Bolivia', 'Brazil', 'Chile', 
                    'Ecuador', 'Paraguay', 'Peru', 'Uruguay', 
                    'Anguilla', 'Antigua & Barbuda', 
                    'British Virgin Is.', 'Montserrat', 
                    'Puerto Rico', 'St. Kitts & Nevis', 'Virgin Is.', 
                    'Baker I.', 'Canada', 'Guatemala', 
                    'Howland I.', 'Johnston Atoll', 'Kiribati', 
                    'Mexico', 'Midway Is.', 'Barbados', 'Dominica', 
                    'Grenada', 'Guadeloupe', 'Martinique', 'St. Lucia', 
                    'St. Pierre & Miquelon', 'St. Vincent & the Grenadines', 
                    'Aruba', 'Bermuda', 'Dominican Republic', 'Haiti', 
                    'Jamaica', 'Netherlands Antilles', 'The Bahamas', 
                    'Turks & Caicos Is.', 'Belize', 'Cayman Is.', 
                    'Colombia', 'Costa Rica', 'Cuba', 'El Salvador', 
                    'Honduras', 'Nicaragua', 'Panama', 'Faroe Is.', 
                    'Greenland', 'Guernsey', 'Iceland', 'Ireland', 
                    'Isle of Man', 'Jan Mayen', 'Jersey', 'United Kingdom', 
                    'Cape Verde', "Cote d'Ivoire", 'Ghana', 'Gibraltar', 
                    'Liberia', 'Morocco', 'Portugal', 'Spain', 'Western Sahara', 
                    'Burkina Faso', 'Guinea', 'Guinea-Bissau', 'Mali', 
                    'Mauritania', 'Senegal', 'Sierra Leone', 'The Gambia', 
                    'Djibouti', 'Eritrea', 'Ethiopia', 'Sudan', 'Uganda', 
                    'Gaza Strip', 'Iraq', 'Israel', 'Jordan', 'Kazakhstan', 
                    'Norway', 'Russia', 'Sweden', 'West Bank', 'Algeria', 
                    'Andorra', 'Libya', 'Monaco', 'Tunisia', 'Benin', 
                    'Cameroon', 'Central African Republic', 'Chad', 
                    'Equatorial Guinea', 'Niger', 'Nigeria', 
                    'Sao Tome & Principe', 'Togo', 'Albania', 
                    'Bosnia & Herzegovina', 'Croatia', 'Italy', 
                    'Macedonia', 'Malta', 'San Marino', 'Vatican City', 
                    'Bulgaria', 'Cyprus', 'Egypt', 'Georgia', 
                    'Greece', 'Lebanon', 'Syria', 'Turkey', 'Austria', 
                    'Czech Republic', 'Denmark', 'Hungary', 'Poland', 
                    'Slovakia', 'Slovenia', 'Svalbard', 'Belgium', 'France', 
                    'Germany', 'Liechtenstein', 'Luxembourg', 'Switzerland', 
                    'United States', 'Belarus', 'Estonia', 'Finland', 'Latvia', 
                    'Lithuania', 'Moldova', 'Romania', 'Ukraine', 'India', 
                    'Maldives', 'Oman', 'Somalia', 'Sri Lanka', 'Turkmenistan', 
                    'Uzbekistan', 'Yemen', 'Armenia', 'Azerbaijan', 'Bahrain', 
                    'Iran', 'Kuwait', 'Qatar', 'Saudi Arabia', 'United Arab Emirates', 
                    'Afghanistan', 'Kyrgyzstan', 'Nepal', 'Pakistan', 'Tajikistan', 
                    'Bangladesh', 'Bhutan', 'Brunei', 'China', 'Mongolia', 'Palau', 
                    'Philippines', 'Cambodia', 'Laos', 'Malaysia', 'Burma/Myanmar', 
                    'North Korea', 'Singapore', 'South Korea', 'Thailand', 'Vietnam', 
                    'Guam', 'Japan', 'Marshall Is.', 'Micronesia', 'Northern Mariana Is.', 
                    'Wake I.', 'Botswana', 'Burundi', 'Kenya', 'Rwanda', 'Tanzania', 
                    'Zambia', 'Zimbabwe', 'Antarctica', 'Bouvet I.', 'Comoros', 
                    'French Southern & Antarctic Lands', 'Heard I. & McDonald Is.', 
                    'Juan De Nova I.', 'Malawi', 'Mozambique', 'Angola', 'Congo', 
                    'Congo, DRC', 'Gabon', 'Lesotho', 'Namibia', 'New Zealand', 
                    'South Africa', 'Swaziland', 'British Indian Ocean Territory', 
                    'Glorioso Is.', 'Madagascar', 'Mauritius', 'Mayotte', 'Reunion', 
                    'Seychelles', 'Australia', 'Christmas I.', 'Cocos Is.', 'Indonesia', 
                    'Timor-Leste', 'Fiji', 'Nauru', 'New Caledonia', 'Norfolk I.', 
                    'Papua New Guinea', 'Solomon Is.', 'Tuvalu', 'Vanuatu', 'Serbia', 
                    'Montenegro', 'Netherlands', 'Hong Kong', 'Taiwan']
        self.assertEqual(expected, DBManager.DBManager().get_country_list())

    """
    Tests add_article_info given an empty parameter.
    """
    def test_add_article_info_null(self):
        self.assertFalse(DBManager.DBManager().add_article_info(
                        "null", "desc", "words", "author", "google.com"))
    
    """
    Tests add_article_list given an empty parameter.
    """
    def test_add_article_list_null(self):
        self.assertFalse(DBManager.DBManager().add_article_list(
                        ["null", "desc", "words", "author", "article", "google.com"]))
    
    """
    Tests add_article_list given a list with less than the
    required number of items.
    """    
    def test_add_article_list_fewer_args(self):
        self.assertFalse(DBManager.DBManager().add_article_list(
                        ["null", "desc", "words", "author", "google.com"]))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_get_country_list']
    unittest.main()