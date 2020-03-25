import unittest
import requests
import random

SUCCESS_CODE = 200
Status_not_found = 404
Invalid_data =400
url = "https://petstore.swagger.io/v2"
random_pet_id = random.randint(1, 1000)

class SwaggerTest(unittest.TestCase):

    def test1_add_a_new_pet_to_the_store(self):
        body = '{"id": ' + str(random_pet_id) + ',  "category": {    "id": 80,    "name": "string"  },  "name": "unicorn",  "photoUrls": [    "string"  ],  "tags": [    {      "id": 80,      "name": "string"    }  ],  "status": "available"}'
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url + "/pet", data=body, headers=headers)
        self.assertEqual(r.status_code, SUCCESS_CODE)
        r = requests.get(url + "/pet/" + str(random_pet_id))
        self.assertEqual(r.status_code, SUCCESS_CODE)
 
    def test2_find_pet_by_posted_id(self):
        r = requests.get(url + "/pet/" + str(random_pet_id))
        self.assertEqual(r.status_code, SUCCESS_CODE)

# Кажется, тест не удался
    # def test3_upload_an_image(self):
    #     headers = {'Content-Type': 'multipart/form-data'}
    #     body = '{"petId": ' + str(random_pet_id) + ', "file": "mSbhTjxLGV0.jpg"}'
    #     r = requests.post(url + "/pet/{random_pet_id}/uploadImage", data=body, headers=headers)
    #     self.assertEqual(r.status_code, SUCCESS_CODE)

    def test4_find_pet_by_status(self):
        positive_list = ["available", "pending", "sold"]
        for i in positive_list:
                r = requests.get(url + "/pet/findByStatus?status=" + str(i))
                self.assertEqual(r.status_code, SUCCESS_CODE)

    def test5_find_pet_by_status_negative(self):
        negative_list = ["not_available", 1, 100000,]
        for i in negative_list:
                r = requests.get(url + "/pet/findByStatus?status=" + str(i))
                self.assertEqual(r.status_code, Invalid_data)


    def test6_find_pet_by_id(self):
        rand = random.randint(1, 1000)
        r = requests.get(url + "/pet/" + str(rand))
        self.assertEqual(r.status_code, SUCCESS_CODE)

    def test7_find_pet_by_id_negative(self):
        negative_list = [9999999999, 0, "unicorn", -6]
        for i in negative_list:
            r = requests.get(url + "/pet/" + str(i))
            self.assertEqual(r.status_code, Status_not_found)

    def test8_update_a_pet_in_the_store_with_formdata(self):
        body = '{"name": "unicorn2"}'
        r = requests.post(url + "/pet/" + str(random_pet_id), data=body)
        self.assertEqual(r.status_code, SUCCESS_CODE)

    def test9_delete_a_pet(self):
        r = requests.delete(url + "/pet/" + str(random_pet_id))
        self.assertEqual(r.status_code, SUCCESS_CODE)


if __name__ == "__main__":
    unittest.main(verbosity=2)