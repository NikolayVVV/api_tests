import requests


class Test_star_wars():
    """Работа с новой локацией"""

    def test_get_heroes(self):
        """Создание новой локации"""
        base_url = "https://swapi.dev/"  # базовая url
        for i in range(1, 84):
            get_resource = "api/people/" + str(i) + "/"  # Ресурс метода get

            get_url = base_url + get_resource
            print(get_url)
            result_get = requests.get(get_url)
            if result_get.status_code != 200:
                continue
            print(result_get.text)
            check_get = result_get.json()
            check_get_personage = check_get.get("name")

            write_to_file = open('D:\\api_tests\\heroes_of_star_wars', 'a', encoding='utf-8')
            write_to_file.write(check_get_personage)
            write_to_file.write('\n')
            write_to_file.close()


new_place = Test_star_wars()
new_place.test_get_heroes()
