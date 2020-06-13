from django.test import SimpleTestCase
from django.urls import reverse


class HomepageTests(SimpleTestCase):

    def setUp(self): # must use exact name 'setUp', otherwise errors will be thrown
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_content_html(self):
        self.assertContains(self.response, 'Homepage')

    def test_homepage_doesnot_contain_html(self):
        self.assertNotContains(self.response, 'Hey, how are you doing?')