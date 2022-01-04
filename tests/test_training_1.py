import unittest
from unittest.mock import patch
import mongomock

from database import Database
from training_1 import main as main_training_1


class TestSandbox(unittest.TestCase):
    def test_init(self):
        with patch("database.MongoClient", side_effect=mongomock.MongoClient):
            main_training_1()

            posts = Database.get_instance().posts.find({})
            print(list(posts))
