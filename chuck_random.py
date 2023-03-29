import requests


class Test_new_joke():
    """Создание новой шутки"""

    def __init__(self):
        pass

    # def test_create_new_random_joke(self):
    #     """Создание случайной шутки"""
    #     url = "https://api.chucknorris.io/jokes/random"
    #     print(url)
    #     result = requests.get(url)
    #     print("Статус код: " + str(result.status_code))
    #     assert 200 == result.status_code
    #     print("Успешно!!! Мы получили новую шутку")
    #     result.encoding = 'utf-8'
    #     print(result.text)
    #     check = result.json()
    #     # check_info = check.get("categories")
    #     # print(check_info)
    #     # assert check_info == []
    #     # print("Категория верна")
    #     check_info_value = check.get("value")
    #     print(check_info_value)
    #     name = "Chuck"
    #     if name in check_info_value:
    #         print("Chuck присутствует")
    #     else:
    #         print("Chuck отсутствует")


    def test_create_new_random_categories_joke(self):
        """Создание случайной шутки на определенную тему"""
        # category = "sport"
        category = "sport"
        url = "https://api.chucknorris.io/jokes/random?category=" + category
        print(url)
        result = requests.get(url)
        print("Статус код: " + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Успешно!!! Мы получили новую шутку")
        else:
            print("Провал")
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        check_info = check.get("categories")
        print(check_info)
        assert check_info == ["sport"]
        print("Категория верна")
        # check_info_value = check.get("value")
        # print(check_info_value)
        # name = "Chuck"
        # if name in check_info_value:
        #     print("Chuck присутствует")
        # else:
        #     print("Chuck отсутствует")

    def test_get_all_categories_joke(self):
        """Создание случайной шутки на определенную тему"""
        url_for_get_all_categories = "https://api.chucknorris.io/jokes/categories"
        print(url_for_get_all_categories)
        result = requests.get(url_for_get_all_categories)
        print("Статус код: " + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Успешно!!! Мы получили новую шутку")
        else:
            print("Провал")
        result.encoding = 'utf-8'
        print(result.text)
        category = input("Введите категорию: ")
        url_for_get_some_categories = "https://api.chucknorris.io/jokes/random?category=" + category
        print(url_for_get_some_categories)
        result = requests.get(url_for_get_some_categories)
        check = result.json()
        print(check)
        check_info = check.get("categories")
        print(check_info)
        if check_info == category:
            print("Категории соответствуют")
        else:
            print("Категории не соответствуют")

        # check = result.json()
        # check_info = check.get("categories")
        # print(check_info)
        # assert check_info == ["sport"]
        # print("Категория верна")
        # check_info_value = check.get("value")
        # print(check_info_value)
        # name = "Chuck"
        # if name in check_info_value:
        #     print("Chuck присутствует")
        # else:
        #     print("Chuck отсутствует")


# random_joke = Test_new_joke()
# random_joke.test_create_new_random_joke()

# random_joke = Test_new_joke()
# random_joke.test_create_new_random_categories_joke()

random_joke = Test_new_joke()
random_joke.test_get_all_categories_joke()