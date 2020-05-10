# Create your tests here.
from behave.formatter import null
from django.contrib.auth.models import User
from django.test import TestCase

from .models import *


class RestaurantReviewTestCase(TestCase):
    global user1
    global user2
    global song1
    global song2

    def setUp(self):
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")
        song1 = song.objects.create(name="crash", length=3, user=user1)
        song2 = song.objects.create(name="miedo", length=3, user=user2)

        list.objects.create(
            name="CHILL",
            description="llista de música chill",
            length=10,
            songs=song1,
            created_on=datetime.now,
            user=user1)
        list.objects.create(
            name="Hardstyle",
            description="llista de música hardstyle",
            length=10,
            songs=song2,
            created_on=datetime.now,
            user=user2)

    # def tests_creation_model_instances(self):
    #     """The average review for a restaurant with 3 reviews is properly computed"""
    #
    #     l = list.objects.get(name="CHILL")
    #
    #     self.assertTrue(l)
    #
    # def test_average_no_review(self):
    #     """The average review for a restaurant without reviews is 0"""
    #     restaurant = Restaurant.objects.get(name="Unknown Restaurant")
    #     self.assertEqual(restaurant.averageRating(), 0)
