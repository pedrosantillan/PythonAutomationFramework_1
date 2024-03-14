from selenium.webdriver.common.by import By

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.burger_menu_btn_id = "react-burger-menu-btn"
        self.logout_sidebar_link_id = "logout_sidebar_link"

    def click_burger_menu(self):
        self.driver.find_element(By.ID, self.burger_menu_btn_id).click()

    def click_logout_sidebar_link(self):
        self.driver.find_element(By.ID, self.logout_sidebar_link_id).click()

