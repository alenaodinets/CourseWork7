from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User


# Create your tests here.
class UsersTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(email="admin@sky.pro")
        self.user.set_password("admin")
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_user_create(self):
        url = reverse("users:register")
        data = {"email": "alena.odinecz2013@yandex.ru", "password": "25665gde254"}
        response = self.client.post(url, data=data)
        print("\ntest_user_create")
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 2)
