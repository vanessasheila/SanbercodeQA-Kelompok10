import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestKelompokSepuluh(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    #TC 1 Edit Name
    def test_1_edit_data(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Dashboard") 
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"Username").send_keys("vanessa123") 
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("test123") 
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click() 
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/table/tbody/tr[2]/td[7]/a[1]").click() 
        time.sleep(1)
        driver.find_element(By.ID,"Name").clear()
        driver.find_element(By.ID,"Name").send_keys("vanessa") 
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/form/div/div[7]/div/input").click() 

    #TC 2 Edit Company
    def test_2_edit_data(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Dashboard") 
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"Username").send_keys("vanessa123") 
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("test123") 
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click() 
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/table/tbody/tr[2]/td[7]/a[1]").click() 
        time.sleep(1)
        driver.find_element(By.ID,"Company").clear()
        driver.find_element(By.ID,"Company").send_keys("tokotesting") 
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/form/div/div[7]/div/input").click() 
    
    #TC 3 Edit Address
    def test_3_edit_data(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Dashboard") 
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"Username").send_keys("vanessa123") 
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("test123") 
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click() 
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/table/tbody/tr[2]/td[7]/a[1]").click() 
        time.sleep(1)
        driver.find_element(By.ID,"Address").clear()
        driver.find_element(By.ID,"Address").send_keys("jalan pramuka") 
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/form/div/div[7]/div/input").click() 

    #TC 4 Edit City
    def test_4_edit_data(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Dashboard") 
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"Username").send_keys("vanessa123") 
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("test123") 
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click() 
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/table/tbody/tr[2]/td[7]/a[1]").click() 
        time.sleep(1)
        driver.find_element(By.ID,"City").clear()
        driver.find_element(By.ID,"City").send_keys("jakarta") 
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/form/div/div[7]/div/input").click() 

    #TC 5 Edit Phone
    def test_5_edit_data(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Dashboard") 
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"Username").send_keys("vanessa123") 
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("test123") 
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click() 
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/table/tbody/tr[2]/td[7]/a[1]").click() 
        time.sleep(1)
        driver.find_element(By.ID,"Phone").clear()
        driver.find_element(By.ID,"Phone").send_keys("089898989898") 
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/form/div/div[7]/div/input").click() 

    #TC 6 Edit Email
    def test_6_edit_data(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Dashboard") 
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"Username").send_keys("vanessa123") 
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("test123") 
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click() 
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/table/tbody/tr[2]/td[7]/a[1]").click() 
        time.sleep(1)
        driver.find_element(By.ID,"Email").clear()
        driver.find_element(By.ID,"Email").send_keys("vanessa@gmail.com") 
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/form/div/div[7]/div/input").click() 

    #TC 7 Delete
    def test_7_delete_data(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Dashboard") 
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"Username").send_keys("vanessa123") 
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("test123") 
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click() 
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/table/tbody/tr[2]/td[7]/a[3]").click() 
        time.sleep(1)        
        driver.find_element(By.XPATH,"/html/body/div[1]/div/form/div/input").click() 
unittest.main()

#tekan (ctrl+?) buat jadiin komen per blok test case