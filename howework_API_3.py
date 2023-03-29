import requests


class Test_new_location():
    """Работа с новой локацией"""

    def test_create_new_location(self):
        """Создание новой локации"""
        base_url = "https://rahulshettyacademy.com"  # базовая url
        key = "?key=qaclick123"  # Параметр для всех запросов

        """Создание новой локации"""
        post_resource = "/maps/api/place/add/json"  # Ресурс метода post

        post_url = base_url + post_resource + key

        print(post_url)

        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        result_post = requests.post(post_url, json=json_for_create_new_location)
        print(result_post.text)
        print("Статус код: " + str(result_post.status_code))
        assert 200 == result_post.status_code
        if result_post.status_code == 200:
            print("Успешно!!! Создана новая локация")
        else:
            print("Провал")

        check_post = result_post.json()
        check_info_post = check_post.get("status")
        print("Статус код ответа: " + check_info_post)
        assert check_info_post == "OK"
        print("Статус ответа верен")
        place_id = check_post.get("place_id")
        print("Place id: " + place_id)
        write_to_file = open('D:\\api_tests\\place_id', 'a')
        write_to_file.write(place_id)
        write_to_file.write('\n')
        write_to_file.close()

        """Проверка создания новой локации"""
        value_from_file = open('D:\\api_tests\\place_id', 'r')
        place_id_from_file = value_from_file.readlines()                  # 32 place id
        value_from_file.close()
        print("Place id из ФАЙЛА: " + place_id_from_file[0])
        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id_from_file[4].rstrip('\n')
        print("URL по которому я иду: " + get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print("Статус код ответа: " + str(result_get.status_code))
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Успешно!!! Проверка создания новой локации прошло успешно")
        else:
            print("Провал")

        """Запись существующих локаций"""
        write_to_file = open('D:\\api_tests\\place_id_which_exists', 'a')
        write_to_file.write(place_id_from_file[4])
        write_to_file.write('\n')
        write_to_file.close()







        # """Удаление новой локации"""
        # delete_resource = "/maps/api/place/delete/json"
        # delete_url = base_url + delete_resource + key
        # print(delete_url)
        # print("Place_id который будет удален: " + place_id_from_file[3])
        # json_for_delete_new_location = {
        #     "place_id": place_id_from_file[3].rstrip('\n')
        # }
        # result_delete = requests.delete(delete_url, json=json_for_delete_new_location)
        # print(result_delete.text)
        # # print("Статус код ответа: " + str(result_post.status_code))
        # assert 200 == result_delete.status_code
        # if result_delete.status_code == 200:
        #     print("Успешно!!! Статус код успешный")
        # else:
        #     print("Провал")
        # check_delete = result_delete.json()
        # check_delete_info = check_delete.get("status")
        # print("Сообщение: " + check_delete_info)
        # assert check_delete_info == "OK"
        # print("Сообщение верно")
        #
        # """Проверка удаления новой локации"""
        # result_get = requests.get(get_url)
        # print(result_get.text)
        # print("Статус код ответа: " + str(result_get.status_code))
        # assert 404 == result_get.status_code
        # if result_get.status_code == 404:
        #     print("Успешно!!! Удаление новой локации прошло успешно")
        # else:
        #     print("Провал")
        #
        # """Проверка адреса"""
        # check_msg = result_get.json()
        # check_msg_info = check_msg.get("msg")
        # print("Сообщение: " + check_msg_info)
        # assert check_msg_info == "Get operation failed, looks like place_id  doesn't exists"
        # print("Сообщение верно")
        #
        # print("Тестирование Test_new_location завершено успешно")



new_place = Test_new_location()
new_place.test_create_new_location()
