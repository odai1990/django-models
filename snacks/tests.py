
from django.test import TestCase,SimpleTestCase
from django.urls import reverse

class Snacks_Test(TestCase):

    def testing_urls_snack_list(self):

        # for snack_list
        url=reverse('snacklist')
        expacted_status_code=self.client.get(url).status_code
        actual_status_code=200
        self.assertEqual(expacted_status_code,actual_status_code)

    def testing_urls_snack_detial(self):

        # for snack_list
        url=reverse('snacksdetial',args=[6])
        expacted_status_code=self.client.get(url).status_code
        actual_status_code=404
        self.assertEqual(expacted_status_code,actual_status_code)


    def testing_templates_snack_list(self):

        # for snack_list
        url=reverse('snacklist')
        expacted_template_code=self.client.get(url)
        actual_template_code='snack_list.html'
        self.assertTemplateUsed(expacted_template_code,actual_template_code)
    
        # # for snack_detail

        # url_about=reverse('about')
        # expacted_status_code_about=self.client.get(url_about).status_code
        # actual_status_code_about=200
        # self.assertEqual(expacted_status_code_about,actual_status_code_about)

    # def testing_templates(self):      

    #     # for home
    #     url_home=reverse('home')
    #     expacted_template_home=self.client.get(url_home)
    #     actual_template_home='home.html'
    #     self.assertTemplateUsed(expacted_template_home,actual_template_home)

    #     # for about

    #     url_about=reverse('about')
    #     expacted_template_about=self.client.get(url_about)
    #     actual_template_about='about.html'
    #     self.assertTemplateUsed(expacted_template_about,actual_template_about)