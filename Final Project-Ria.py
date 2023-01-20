import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestRegister(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    #TC SU1 Access to Sign up page
    def test_a_dashboard(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net") # ke dashboard
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > form > ul > li:nth-child(1) > a").click() # klik tombol sign up
        time.sleep(2)

    #TC SU2 Access Sign up with input all field 
    def test_b_dashboard(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net") # ke dashboard
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > form > ul > li:nth-child(1) > a").click() # klik tombol sign up
        time.sleep(2)
        driver.find_element(By.ID,"FirstName").send_keys("Adnan") # isi first name
        time.sleep(1)
        driver.find_element(By.ID,"Surname").send_keys("RR") # isi surename
        time.sleep(1)
        driver.find_element(By.ID,"E_post").send_keys("Testing") # isi e-post
        time.sleep(1)
        driver.find_element(By.ID,"Mobile").send_keys("081254753") # isi mobile
        time.sleep(1)
        driver.find_element(By.ID,"Username").send_keys("Adnan") # isi username
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("Test123") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"ConfirmPassword").send_keys("Test123") # isi confirm password
        time.sleep(1)
        driver.find_element(By.ID,"submit").click() # klik tombol submit
        time.sleep(3)

    #TC SU3 Access Sign up with input mandatory field only
    def test_c_dashboard(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net") # ke dashboard
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > form > ul > li:nth-child(1) > a").click() # klik tombol sign up
        time.sleep(2)
        driver.find_element(By.ID,"FirstName").send_keys("Adnan") # isi first name
        time.sleep(1)
        driver.find_element(By.ID,"Surname").send_keys("RR") # isi surename
        time.sleep(1)
        driver.find_element(By.ID,"Username").send_keys("Adnan") # isi username
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("Test123") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"submit").click() # klik tombol submit
        time.sleep(3)

    #TC SU4 Access Sign up without input field
    def test_d_dashboard(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net") # ke dashboard
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > form > ul > li:nth-child(1) > a").click() # klik tombol sign up
        time.sleep(2)
        driver.find_element(By.ID,"FirstName").send_keys("") # isi first name
        time.sleep(1)
        driver.find_element(By.ID,"Surname").send_keys("") # isi surename
        time.sleep(1)
        driver.find_element(By.ID,"E_post").send_keys("") # isi e-post
        time.sleep(1)
        driver.find_element(By.ID,"Mobile").send_keys("") # isi mobile
        time.sleep(1)
        driver.find_element(By.ID,"Username").send_keys("") # isi username
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"ConfirmPassword").send_keys("") # isi confirm password
        time.sleep(1)
        driver.find_element(By.ID,"submit").click() # klik tombol submit
        time.sleep(3)
        
         #TC L1 Access to login page
    def test_Login_a_dashboard(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net") # ke dashboard
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > form > ul > li:nth-child(2) > a").click() # klik tombol login
        time.sleep(2)

    #TC L2 Login with valid username & password 
    def test_Login_a_dashboard(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net") # ke dashboard
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > form > ul > li:nth-child(2) > a").click() # klik tombol login
        time.sleep(2)
        driver.find_element(By.ID,"Username").send_keys("Ria") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("Test123") # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"body > div.container.body-content > div:nth-child(4) > form > table > tbody > tr:nth-child(7) > td:nth-child(2) > input.btn.btn-primary").click() # klik tombol login
        time.sleep(3)

    #TC L3 Login with valid username & invalid password
    def test_Login_a_dashboard(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net") # ke dashboard
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > form > ul > li:nth-child(2) > a").click() # klik tombol login
        time.sleep(2)
        driver.find_element(By.ID,"Username").send_keys("Ria") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("123456") # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"body > div.container.body-content > div:nth-child(4) > form > table > tbody > tr:nth-child(7) > td:nth-child(2) > input.btn.btn-primary").click() # klik tombol login
        time.sleep(3)

        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        driver.assertIn('Welcome', response_data)
        driver.assertEqual(response_message, 'wrong username or password')

    #TC L4 Login with invalid username & valid password
    def test_Login_a_dashboard(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net") # ke dashboard
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > form > ul > li:nth-child(2) > a").click() # klik tombol login
        time.sleep(2)
        driver.find_element(By.ID,"Username").send_keys("RiaRia") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("Test123") # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"body > div.container.body-content > div:nth-child(4) > form > table > tbody > tr:nth-child(7) > td:nth-child(2) > input.btn.btn-primary").click() # klik tombol login
        time.sleep(3)

        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        driver.assertIn('Welcome', response_data)
        driver.assertEqual(response_message, 'wrong username or password')

    #TC L5 Login without username & password
    def test_Login_a_dashboard(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net") # ke dashboard
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > form > ul > li:nth-child(2) > a").click() # klik tombol login
        time.sleep(2)
        driver.find_element(By.ID,"Username").send_keys("") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("") # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"body > div.container.body-content > div:nth-child(4) > form > table > tbody > tr:nth-child(7) > td:nth-child(2) > input.btn.btn-primary").click() # klik tombol login
        time.sleep(3)

        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        driver.assertIn('Welcome', response_data)
        driver.assertEqual(response_message, 'wrong username or password')

    #TC LO1 Successfully Logout
    def test_Login_a_dashboard(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net") # ke dashboard
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > form > ul > li:nth-child(2) > a").click() # klik tombol login
        time.sleep(2)
        driver.find_element(By.ID,"Username").send_keys("Ria") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("Test123") # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"body > div.container.body-content > div:nth-child(4) > form > table > tbody > tr:nth-child(7) > td:nth-child(2) > input.btn.btn-primary").click() # klik tombol login
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > form > ul > li:nth-child(2) > a").click() # klik tombol logout
        time.sleep(3)


        
unittest.main()