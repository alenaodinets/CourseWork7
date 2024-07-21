from datetime import timedelta
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from habits.models import Habit
from users.models import User


# Create your tests here.
class HabitsTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email="admin@sky.pro")
        self.user.set_password("admin")
        self.user.save()
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            owner=self.user,
            place="Дома",
            time="2024-05-27 08:05:00",
            action="Выпить стакан воды",
            is_pleasant=False,
            period=1,
            duration=timedelta(minutes=1),
            reward="Погладить собачку",
            is_public=True,
            related_habit=None,
        )

    def test_habit_create(self):
        url = reverse("habits:habits-create")
        data = {
            "owner": self.user.id,
            "place": "Дома",
            "time": "2024-05-27 08:40:00",
            "action": "Съесть кашу",
            "is_pleasant": False,
            "period": 3,
            "duration": timedelta(minutes=2),
            "reward ": "Выпить кофе",
            "is_public": True,
        }
        response = self.client.post(url, data=data)
        print("\ntest_habit_create")
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habits_retrieve(self):
        url = reverse("habits:habits-get", kwargs={"pk": self.habit.id})
        response = self.client.get(url)
        print("\ntest_habits_retrieve")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), self.habit.action)

    def test_habit_update(self):
        url = reverse("habits:habits-update", kwargs={"pk": self.habit.id})
        new_data = {
            "reward": "Послушать любимую музыку",
        }
        response = self.client.patch(url, data=new_data)
        print("\ntest_habit_update")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("reward"), "Послушать любимую музыку")

    def test_habit_delete(self):
        url = reverse("habits:habits-delete", kwargs={"pk": self.habit.id})
        response = self.client.delete(url)
        print("\ntest_habit_delete")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):
        url = reverse("habits:habits-list")
        response = self.client.get(url)
        print("\ntest_habit_list")
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.all().count(), 1)

    def test_DurationValidator(self):
        url = reverse("habits:habits-create")
        data = {
            "owner": self.user.id,
            "place": "Дома",
            "action": "позвонить близким",
            "is_pleasant": False,
            "period": 7,
            "duration": timedelta(minutes=3),
            "reward ": "Скушать вкусненькое",
            "is_public": True,
        }
        response = self.client.post(url, data=data)
        print("\ntest_DurationValidator")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
