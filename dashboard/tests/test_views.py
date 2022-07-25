from django.test import TestCase
from django.shortcuts import reverse

from dashboard import models

from homepage.models import TestimonialModel

from users.models import CustomUser


class TestimoniListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_testimoni = 10
        user = CustomUser.objects.create_superuser("TestAcc", "TestPassword")

        for testimoni_id in range(number_of_testimoni):
            TestimonialModel.objects.create(
                link_video="https://youtu.be/faGGViNtcgk",
                full_name=f"Lukman No. {testimoni_id}",
                title=f"Teacher No. {testimoni_id}",
                testimonial=f"Lorem ipsum dolor sitamet no {testimoni_id}",
            )

    def test_view_if_user_logged_in(self):
        login = self.client.login(username="TestAcc", password="TestPassword")
        response = self.client.get(reverse('testimoni'))

        self.assertEqual(str(response.context["user"]), "TestAcc")
        self.assertEqual(response.status_code, 200)

    def test_view_if_user_not_logged_in(self):
        response = self.client.get(reverse('testimoni'))
        self.assertRedirects(response, '/login/?next=/d/testimoni/')




