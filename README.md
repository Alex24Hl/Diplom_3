## Дипломный проект. Задание 3: Веб-приложение

### UI-тесты для тестирования Stellar Burgers

## Реализованные сценарии

### 1. Восстановление пароля
- `test_go_to_password_recovery_page.py` - проверка перехода на страницу восстановления пароля
- `test_reset_password_with_email.py` -проверка ввода почты и клика по кнопке восстановления
- `test_password_visibility.py` - проверка подсветки поля пароля
### 2. Личный кабинет
- `test_go_to_personal_account.py` - проверка перехода в личный кабинет
- `test_go_to_order_history.py` - проверка перехода в историю заказов
- `test_logout_from_account.py` - проверка логаута
### 3. Основной функционал
- `test_go_to_constructor.py` - переход в конструктор
- `test_go_to_order_feed.py` - переход в ленту заказов
- `test_open_ingredient_details.py` - открытие деталей ингредиента
- `test_close_ingredient_details.py` - закрытие модального окна ингредиента
- `test_ingredient_counter_increases.py` - увеличение счетчика ингредиента
- `test_create_order_by_logged_in_user.py` - оформление заказа авторизованным пользователем
### 4. Раздел «Лента заказов»
- `test_open_order_details.py` - открытие деталей заказа
- `test_user_orders_in_feed.py` - отображение заказов пользователя в ленте
- `test_total_orders_counter_increases.py` - увеличение счетчика 'Выполнено за всё время'
- `test_today_orders_counter_increases.py` - увеличение счетчика 'Выполнено за сегодня'
- `test_new_order_in_progress.py` - отображение заказа в разделе 'В работе'

### Структура проекта
- `locators.py` - пакет, содержащий локаторы
- `pages` - пакет, содержащий страницы экранов
- `tests`- пакет, содержащий набор тестов на разаработанную функциональность
- `allure_results` - пакет, содержащий отчеты
- `config.py` - файл, содержащий энндпоиенты и базовую урлу
- `helpers.py` - файл, содержащий вспомогательные методы
- `requirements.txt` - файл, содержащий внешние зависимости

### Запуск автотестов

**Запуск автотестов и генерация allure отчёта**

> `pytest --alluredir=allure_results`

**Установка зависимостей**

> `$ pip install -r requirements.txt`