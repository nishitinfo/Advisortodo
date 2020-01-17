import unittest

import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class test_Project(unittest.TestCase) :

    @classmethod
    def setUpClass(self) :
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get("https://advisortodo.gntkwhqzn-test.advisortodo.com/#/auth/signin")
        self.driver.set_window_size(1366, 741)

    def test_Project_Task(self) :
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control").click()
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control").send_keys(
            "Test@qa.com")
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").click()
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").send_keys("Test@123#")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(4) .menu-title").click()
        self.driver.find_element_by_id("addProject").click()
        self.driver.find_element(By.XPATH, "//input[@class='ml-2 m-0 form-control input-xs']").send_keys("test project",
                                                                                                         Keys.ENTER)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//input[@class='ml-2 m-0 form-control input-xs']").click()
        self.driver.find_element(By.ID, "projectDurationStartInput").click()
        self.driver.find_element(By.CSS_SELECTOR, ".react-datepicker__day--019").click()
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.ID, "projectDurationEndInput").click()
        self.driver.find_element(By.CSS_SELECTOR, ".react-datepicker__day--024").click()
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.CSS_SELECTOR, "#projectTaskCount1 > p").click()
        self.driver.find_element(By.CSS_SELECTOR, ".textarea-control").click()
        element = self.driver.find_element(By.ID, "addTask")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".textarea-control").send_keys("test")
        self.driver.implicitly_wait(10)
        element = self.driver.find_element(By.ID, "addTask")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".fa-plus")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, "combobox1").click()
        self.driver.find_element(By.ID, "combobox1").send_keys("Task for test")
        self.driver.find_element(By.ID, "combobox1").send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.CSS_SELECTOR, ".m-0").click()
        self.driver.find_element(By.XPATH, "//div[@id=\'taskPriority\']/div[2]/div/div").click()
        self.driver.find_element(By.XPATH, "//div[@id=\'taskPriority\']/div[2]/div[2]/div/div[2]").click()
        self.driver.find_element(By.ID, "taskDueDate").click()
        self.driver.find_element(By.CSS_SELECTOR, ".react-datepicker__day--019").click()
        self.driver.find_element(By.XPATH,
                                 "//html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]").click()
        self.driver.find_element(By.CSS_SELECTOR, ".react-datepicker__day--020").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.CSS_SELECTOR, ".react-tagsinput-input").click()
        self.driver.find_element(By.CSS_SELECTOR, ".react-tagsinput-input").send_keys("test")
        self.driver.find_element(By.CSS_SELECTOR, ".react-tagsinput-input").send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.CSS_SELECTOR, ".react-tagsinput-input").send_keys("task")
        self.driver.find_element(By.CSS_SELECTOR, ".react-tagsinput-input").send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.CSS_SELECTOR, ".react-tagsinput-input").send_keys("nishit")
        self.driver.find_element(By.CSS_SELECTOR, ".react-tagsinput-input").send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        element = self.driver.find_element(By.ID, "cloneTask")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.implicitly_wait(10)
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".m-0 > span").click()
        element = self.driver.find_element(By.ID, "deleteTask")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.implicitly_wait(10)
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.implicitly_wait(10)
        element = self.driver.find_element(By.CSS_SELECTOR, ".fa-trash")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.implicitly_wait(10)
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, "deleteTask").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) .m-0").click()
        element = self.driver.find_element(By.ID, "deleteTask")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # self.driver.find_element(By.ID, "deleteTask").click()
        self.driver.find_element(By.CSS_SELECTOR, ".m-0 > span").click()
        element = self.driver.find_element(By.ID, "deleteTask")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, "deleteTask").click()
        self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(4) .menu-title").click()
        self.driver.find_element(By.CSS_SELECTOR, ".pl-2").click()
        element = self.driver.find_element(By.ID, "deleteProject")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.ID, "deleteProject")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.implicitly_wait(10)
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, "deleteProject").click()
        self.driver.find_element_by_id("profileDropdown").click()
        self.driver.find_element_by_xpath("//span[contains(text(),'Logout')]").click()
        print('Project Tested successfully')

    @classmethod
    def tearDownClass(self) :
        self.driver.implicitly_wait(10)
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__' :
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./Reports', report_title='Advisortodo Report'))