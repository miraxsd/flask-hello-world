import unittest
from app import app

class HouseEndpointTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_house(self):
        response = self.app.get('/house')
        self.assertEqual(response.status_code, 200)
        self.assertIn('house', response.json)

    def test_post_house(self):
        new_house = {
            'address': '123 Main St',
            'price': 250000,
            'bedrooms': 3,
            'bathrooms': 2
        }
        response = self.app.post('/house', json=new_house)
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)

    def test_put_house(self):
        update_house = {
            'price': 260000
        }
        response = self.app.put('/house/1', json=update_house)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['price'], 260000)

    def test_delete_house(self):
        response = self.app.delete('/house/1')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()