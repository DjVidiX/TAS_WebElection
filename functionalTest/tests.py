from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PollsTest(LiveServerTestCase):
    fixtures = ['admin_user.json']

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_create_new_poll_via_admin_site(self):
        self.browser.get(self.live_server_url + '/admin/')

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)

        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('lukasz')

        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('Lukasz')
        password_field.send_keys(Keys.RETURN)

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)

        candidates_links = self.browser.find_elements_by_link_text('Obywatels')
        self.assertEquals(len(polls_links), 2)

        candidates_links[1].click()

        new_candidates_link = self.browser.find_element_by_link_text('Dodaj obywatel')
        new_candidates_link.click()
        
        first_name_field = self.browser.find_element_by_name('Imie')
        first_name_field.send_keys("Selenium")
        
        last_name_field = self.browser.find_element_by_name('Nazwisko')
        last_name_field.send_keys("Test")
        
        partia_field = self.browser.find_element_by_name('PESEL')
        partia_field.send_keys("56789123456")
        
        haslo_field = self.browser.find_element_by_name('Nr dowodu')
        haslo_field.send_keys("AGH11223")

        save_button = self.browser.find_element_by_link_text('Zapisz')
        save_button.click()

        new_obywatels_links = self.browser.find_elements_by_link_text(
                "Selenium Test"
        )
        self.assertEquals(len(new_poll_links), 1)
