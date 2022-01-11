import unittest
from unittest.mock import patch, Mock
import mongomock
from settings import *

from training_1 import main as main_training_1


class TestSandbox(unittest.TestCase):
    def test_init(self):
        mock_mongo_client = Mock()
        mock_mongo_client.return_value = {
            MONGODB_DB: mongomock.MongoClient()[MONGODB_DB]
        }
        with patch("training_1.MongoClient", mock_mongo_client):
            main_training_1()
            print(list(mock_mongo_client()[MONGODB_DB].posts.find({})))
