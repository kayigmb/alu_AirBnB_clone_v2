#!/usr/bin/python3
""" Module for testing db storage"""

import unittest
import models
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.place import Place
import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                 "Not testing db storage")
class TestDBStorage(unittest.TestCase):
    """ Class to test the DBStorage method """

    def setUp(self):
        """ Set up test environment """
        self.db = models.storage

    def tearDown(self):
        """ Remove storage file at end of tests """
        del self.db

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(self.db.all()), 0)

    def test_new_state(self):
        """ New State is instantiated with name"""
        new_state = State("California")
        self.db.new(new_state)
        self.db.save()
        self.assertEqual(len(new_state.id), 36)
        self.assertEqual(new_state.name, "California")

    def test_new_city(self):
        """ New City is instantiated with name"""
        new_state = State("California")
        new_city = City("San Francisco", state_id=new_state.id)
        self.db.new(new_state)
        self.db.save()
        self.db.new(new_city)
        self.db.save()
        self.assertEqual(len(new_city.id), 36)
        self.assertEqual(new_city.name, "San Francisco")
        self.assertEqual(new_city.state_id, new_state.id)

    def test_user(self):
        """ New User is instantiated with email and password"""
        new_user = User(email="ssam@test.com",
                        password="test", first_name="Sam")
        self.db.new(new_user)
        self.db.save()
        self.assertEqual(len(new_user.id), 36)
        self.assertEqual(new_user.email, "ssam@test.com")
        self.assertEqual(new_user.password, "test")
        self.assertEqual(new_user.first_name, "Sam")

    def test_place(self):
        """ New Place is instantiated with name"""
        new_place = Place(name="My_little_house", number_rooms=4)
        self.db.new(new_place)
        self.db.save()
        self.assertEqual(len(new_place.id), 36)
        self.assertEqual(new_place.name, "My_little_house")
        self.assertEqual(new_place.number_rooms, 4)

    def test_amenity(self):
        """ New Amenity is instantiated with name"""
        new_amenity = Amenity(name="Microwave")
        self.db.new(new_amenity)
        self.db.save()
        self.assertEqual(len(new_amenity.id), 36)
        self.assertEqual(new_amenity.name, "Microwave")

    def test_review(self):
        """ New Review is instantiated with text"""
        new_review = Review(text="Warm bath and quality amenities")
        self.db.new(new_review)
        self.db.save()
        self.assertEqual(len(new_review.id), 36)
        self.assertEqual(new_review.text, "Warm bath and quality amenities")
