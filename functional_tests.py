import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys

MAX_WAIT = 10


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000/cv')
        self.assertIn('Gustavo\'s CV', self.browser.title)
        header_text = self.browser.find_element_by_id('tddh2').text
        self.assertIn('Test-Driven Development'.upper(), header_text)
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter an item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        # self.fail('Finish the test!')


class NewCVTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://localhost:8000/cv')
        self.assertIn('Gustavo\'s CV', self.browser.title)
        header_text = self.browser.find_element_by_id('tddh2').text
        self.assertIn('Test-Driven Development'.upper(), header_text)

    def tearDown(self):
        self.browser.quit()

    def test_create_experience(self):
        inputbox = self.browser.find_element_by_id('id_new_role')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a role')
        # Role #
        inputbox.send_keys('Web Developer')
        inputbox = self.browser.find_element_by_id('id_new_company')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a company')
        # Company #
        inputbox.send_keys('Legendary People + Ideas')
        inputbox = self.browser.find_element_by_id('id_new_duration')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a duration')
        # Duration #
        inputbox.send_keys('May 2017 - June 2017')
        inputbox = self.browser.find_element_by_id('id_new_item1')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter item 1')
        # Item 1 #
        inputbox.send_keys('Frontend and backend development')
        inputbox = self.browser.find_element_by_id('id_new_item2')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter item 2')
        # Item 2 #
        inputbox.send_keys(
            'Developed websites using the Bootstrap grid, HTML5, CSS, and JavaScript and then transferred them to '
            'Wordpress to be editable in back-office')
        inputbox = self.browser.find_element_by_id('id_new_item3')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter item 3')
        # Item 3 #
        inputbox.send_keys(
            'Produced a PHP script that, by using cURL and working with an API that uses RESTful guidelines and '
            'OAuth2 Framework, exports data from one website to another')
        self.browser.find_element_by_tag_name('form').submit()

    def test_create_education(self):
        inputbox = self.browser.find_element_by_id('id_new_degree')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a degree')
        # Degree #
        inputbox.send_keys('MSci Computer Science')
        inputbox = self.browser.find_element_by_id('id_new_institution')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter an institution')
        # Institution #
        inputbox.send_keys('University of Birmingham')
        inputbox = self.browser.find_element_by_id('id_new_duration')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a duration')
        # Duration #
        inputbox.send_keys('October 2018 - Present')
        inputbox = self.browser.find_element_by_id('id_new_item1')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter item 1')
        # Item 1 #
        inputbox.send_keys('Bribery&Corruption game project')
        inputbox = self.browser.find_element_by_id('id_new_item1_grade')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a grade')
        # Item 1 Grade #
        inputbox.send_keys('100')
        inputbox = self.browser.find_element_by_id('id_new_item2')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter item 2')
        # Item 2 #
        inputbox.send_keys('SE: Virtual Psychologist application designed in UML')
        inputbox = self.browser.find_element_by_id('id_new_item2_grade')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a grade')
        # Item 2 Grade #
        inputbox.send_keys('93.75')
        inputbox = self.browser.find_element_by_id('id_new_item3')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter item 3')
        # Item 3 #
        inputbox.send_keys('AI: Maze and Obstacle Navigation with custom Lego EV3 running on LeJos and programmed in '
                           'Java')
        inputbox = self.browser.find_element_by_id('id_new_item3_grade')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a grade')
        # Item 3 Grade #
        inputbox.send_keys('66.67')
        self.browser.find_element_by_tag_name('form').submit()

    def test_create_hard_skill(self):
        inputbox = self.browser.find_element_by_id('id_new_hard_skill')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a hard skill')
        inputbox.send_keys('fab fa-java')
        self.browser.find_element_by_tag_name('form').submit()

    def test_create_soft_skill(self):
        inputbox = self.browser.find_element_by_id('id_new_soft_skill')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a soft skill')
        inputbox.send_keys('Proactive')
        self.browser.find_element_by_tag_name('form').submit()

    def test_create_project(self):
        inputbox = self.browser.find_element_by_id('id_new_title')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a title')
        # Title #
        inputbox.send_keys('Bribery&Corruption')
        inputbox = self.browser.find_element_by_id('id_new_description')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a description')
        # Description #
        inputbox.send_keys('A fast-paced top-down strategy game where you, as a Mayor candidate of a small village, '
                           'try to get the people\'s votes by bribing them. It was programmed in Java and JavaFX, '
                           'supported by an H2 database and accomplished as part of the Team Project module.')
        inputbox = self.browser.find_element_by_id('id_new_duration')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a duration')
        # Duration #
        inputbox.send_keys('January 2020 - March 2020')
        inputbox = self.browser.find_element_by_id('id_new_link')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a link')
        # Link (Can be empty) #
        inputbox.send_keys('')
        self.browser.find_element_by_tag_name('form').submit()

    def test_create_interest(self):
        inputbox = self.browser.find_element_by_id('id_new_icon')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter an icon')
        inputbox.send_keys('fas fa-theater-masks')
        self.browser.find_element_by_tag_name('form').submit()

    def test_create_language(self):
        inputbox = self.browser.find_element_by_id('id_new_name')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a name')
        # Name #
        inputbox.send_keys('Portuguese')
        inputbox = self.browser.find_element_by_id('id_new_proficiency')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a proficiency')
        # Proficiency #
        inputbox.send_keys('Native Proficiency')
        inputbox = self.browser.find_element_by_id('id_new_level')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a level')
        # Level #
        inputbox.send_keys('100')
        self.browser.find_element_by_tag_name('form').submit()


if __name__ == '__main__':
    unittest.main()
