import allure

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import BASE_URL

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = BASE_URL

    @allure.title('Метод для перехода на сайт')
    def open(self):
        self.driver.get(self.base_url)

    @allure.title('Метод для поиска элемента на веб-странице')
    def find_element(self, locator):
        return WebDriverWait(self.driver,15).until(EC.visibility_of_element_located(locator))

    @allure.step('Метод проверки кликабельности элемента')
    def check_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))

    @allure.title('Метод для клика по веб-элементу')
    def click_element(self, locator):
        target = self.check_element_is_clickable(locator)
        click = ActionChains(self.driver)
        click.move_to_element(target).click().perform()

    @allure.step('Метод для проверки отображение элемента')
    def check_displaying_of_element(self, locator):
        try:
            WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    @allure.step('Метод для перетаскивания элемента')
    def drag_and_drop_element(self, source_element, target_element):
        script = """
                function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
                    var dataTransfer = new DataTransfer();
                    var dragStartEvent = new DragEvent('dragstart', {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    sourceNode.dispatchEvent(dragStartEvent);

                    var dropEvent = new DragEvent('drop', {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    destinationNode.dispatchEvent(dropEvent);
                    var dragEndEvent = new DragEvent('dragend', {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    sourceNode.dispatchEvent(dragEndEvent);
                }
                simulateHTML5DragAndDrop(arguments[0], arguments[1]);
                """
        self.driver.execute_script(script, source_element, target_element)
