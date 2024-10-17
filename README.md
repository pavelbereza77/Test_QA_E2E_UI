# Test_QA_E2E_UI
Проект для проверки сценария покупки товара на сайте saucedemo.com с 
использованием Python на Selenium, PyTest. Тест проверять процесс
от авторизации до завершения покупки,
с возможностью легко воспроизвести его на любом компьютере.
Так же можно протестировать каждую страницу сайта отдельно на предмет
корректной работы и наличия необходимых элементов.
Селекторы поиска элементов на сайте уникальны и вынесены в отдельный модуль.

Тест составлен на основе паттерна PageObject

### **Структура проекта**
В модуле [conftest.py](conftest.py) прописана логика запуска драйвера 
браузера Chrome и FireFox (по умолчанию запускается Chrom)

Тестовые модули:
* [test_basket_page.py](test_basket_page.py)
* [test_lists_products_page.py](test_lists_products_page.py)
* [test_login_page.py](test_login_page.py)
* [test_overview_page.py](test_overview_page.py)
* [test_product_page.py](test_product_page.py)
* [test_sale_page.py](test_sale_page.py)

Папка pages с модулями в которых прописана 
логика проверки каждой страницы, в том числе:
* [base_page.py](pages%2Fbase_page.py)
* [basket_page.py](pages%2Fbasket_page.py)
* [list_products_page.py](pages%2Flist_products_page.py)
* [login_page.py](pages%2Flogin_page.py)
* [overview_page.py](pages%2Foverview_page.py)
* [product.py](pages%2Fproduct.py)
* [sale_page.py](pages%2Fsale_page.py)

Также в папке pages в модуль [locators.py](pages%2Flocators.py) 
вынесены селекторы selenium для поиска элементов по страницам сайта  

### **Установка**

Клонировать репозиторий

[https://github.com/pavelbereza77/Test_QA_E2E_UI.git](https://github.com/pavelbereza77/Test_QA_E2E_UI.git)

### **Установка зависимостей в виртуальном окружении**

`pip install -r requirements.txt`

### **Запуск теста**
В командной строке набрать команду 
1. `pytest -v test_finish.py` для запуска теста по сценарию 
от авторизации посетителя до финальной страницы где пользователем произведен выбор и оплата товара
2. `pytest -v ` для запуска всех тестов для всех страниц
3. `pytest -v <название тестового модуля> ` для запуска теста отдельной страницы сайта