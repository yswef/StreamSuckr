import unittest
from core.json_handler import  JsonHandler

class TestJsonHandler(unittest.TestCase):

    
    def test_read_data(self):
        json_data = '{"name": "Yusuf", "age": 20}'
        result = JsonHandler.read_data(json_data)
        self.assertIsInstance(result, dict)
    
    
    def test_seve_data(self):
        data = {
    "name": "Yusuf",
    "age": 20,
    "tasks": ["Download video", "Encrypt file"]
}
        result = JsonHandler.save_data(data)
        self.assertIsInstance(result, str)







if __name__ == "__main__":
    unittest.main()