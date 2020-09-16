from rest_framework.test import APITestCase
from model_mommy import mommy
from .models import CoffeeMachine, CoffeePods
from django.contrib.auth.models import User


class CoffePodsAPITest(APITestCase):
    def test_list_cofee_pods(self):
        url = "/api/coffee/coffee-pods/"
        user = mommy.make(User)
        mommy.make(CoffeePods, _quantity=6)
        self.client.force_login(user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 6)

    def test_list_coffee_pods_filter(self):
        url = "/api/coffee/coffee-pods/?product_type=COFFEE_MACHINE_LARGE"
        user = mommy.make(User)
        mommy.make(CoffeePods, _quantity=6)
        mommy.make(CoffeePods, product_type='l')
        self.client.force_login(user)
        response = self.client.get(url)
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 3)

    def test_list_coffee_pods_filter_second(self):
        url = "/api/coffee/coffee-pods/?pack_size=7"
        user = mommy.make(User)
        mommy.make(CoffeePods, _quantity=6, pack_size='1')
        mommy.make(CoffeePods, pack_size='7', _quantity=2)
        self.client.force_login(user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)


class CoffeMachineAPITest(APITestCase):
    def test_list_cofee_machine(self):
        url = "/api/coffee/coffee-machines/"
        user = mommy.make(User)
        mommy.make(CoffeeMachine, _quantity=6)
        self.client.force_login(user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 6)

    def test_list_coffee_machine_filter(self):
        url = "/api/coffee/coffee-pods/?product_type=ALL_LARGE_PODS"
        user = mommy.make(User)
        mommy.make(CoffeeMachine, _quantity=6)
        mommy.make(CoffeeMachine, product_type='l')
        self.client.force_login(user)
        response = self.client.get(url)
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 10)
