from django.test import SimpleTestCase
from django.urls import reverse


class HomepageTests(SimpleTestCase):

    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_homepage_content_html(self):
        response = self.client.get('/')
        self.assertContains(response, 'Homepage')

    def test_homepage_doesnot_contain_html(self):
        response = self.client.get('/')
        self.assertNotContains(response, 'Hey, how are you doing?')