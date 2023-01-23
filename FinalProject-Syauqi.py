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

    #TC 1   
    def test_a_dashboard(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Dashboard") # ke dashboard
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"Username").send_keys("syauqijufri") # isi username
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("anakpintar") # isi password
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click() #CREATE CTA
        time.sleep(3)

    #TC 2
    def test_b_isi(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Dashboard") # ke dashboard
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"Username").send_keys("syauqijufri") # isi username
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("anakpintar") # isi password
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click() #Login CTA
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/p[1]/a").click() #CREATE CTA
        time.sleep(3)
        driver.find_element(By.ID,"Name").send_keys("test2") # isi name setelah run ganti lagi
        time.sleep(1)
        driver.find_element(By.ID,"Company").send_keys("tokotesting") # isi company setelah run ganti lagi
        time.sleep(1)
        driver.find_element(By.ID,"Address").send_keys("jalan 1 nusantara") # isi address setelah run ganti lagi
        time.sleep(1)
        driver.find_element(By.ID,"City").send_keys("jakarta") # isi city setelah run ganti lagi
        time.sleep(1)
        driver.find_element(By.ID,"Phone").send_keys("087783834992") # isi phone setelah run ganti lagi
        time.sleep(1)
        driver.find_element(By.ID,"Email").send_keys("sogi@gmail.com") # isi email setelah run ganti lagi
        time.sleep(3)

    #TC 3
    def test_c_create_data(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Dashboard") # ke dashboard
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"Username").send_keys("syauqijufri") # isi username
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("anakpintar") # isi password
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click() #Login CTA
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/p[1]/a").click() #CREATE CTA
        time.sleep(1)
        driver.find_element(By.ID,"Name").send_keys("test2") # isi name setelah run ganti lagi
        time.sleep(1)
        driver.find_element(By.ID,"Company").send_keys("tokotesting") # isi company setelah run ganti lagi
        time.sleep(1)
        driver.find_element(By.ID,"Address").send_keys("jalan 1 nusantara") # isi address setelah run ganti lagi
        time.sleep(1)
        driver.find_element(By.ID,"City").send_keys("jakarta") # isi city setelah run ganti lagi
        time.sleep(1)
        driver.find_element(By.ID,"Phone").send_keys("087783834992") # isi phone setelah run ganti lagi
        time.sleep(1)
        driver.find_element(By.ID,"Email").send_keys("sogi@gmail.com") # isi email setelah run ganti lagi
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/form/div/div[7]/div/input").click() #CREATE data

    #TC 4
    def test_d_back_to_dashboard(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Dashboard") # ke dashboard
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"Username").send_keys("syauqijufri") # isi username
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("anakpintar") # isi password
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click() #Login CTA
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/p[1]/a").click() #CREATE CTA
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,"body > div > div > a").click() #CREATE CTA
        time.sleep(1) 

    #TC 5
    def test_e_detail(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Dashboard") # ke dashboard
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"Username").send_keys("syauqijufri") # isi username
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("anakpintar") # isi password
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click() #Login CTA
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/table/tbody/tr[2]/td[7]/a[2]").click() #detail CTA
        time.sleep(3)

    #TC 6
    def test_f_detail_sesuatu(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Dashboard") # ke dashboard
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"Username").send_keys("syauqijufri") # isi username
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("anakpintar") # isi password
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click() #Login CTA
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/table/tbody/tr[7]/td[7]/a[2]").click() #detail CTA
        time.sleep(3)

    #TC 7
    def test_g_detail_isi(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Dashboard") # ke dashboard
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"Username").send_keys("syauqijufri") # isi username
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("anakpintar") # isi password
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click() #Login CTA
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/table/tbody/tr[7]/td[7]/a[2]").click() #detail CTA
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,"body > div > div > dl > dt:nth-child(1)").text #name
        driver.find_element(By.XPATH,"/html/body/div[1]/div/dl/dd[1]").text      
        driver.find_element(By.CSS_SELECTOR,"body > div > div > dl > dt:nth-child(3)").text #company
        driver.find_element(By.XPATH,"/html/body/div[1]/div/dl/dd[2]").text
        driver.find_element(By.CSS_SELECTOR,"body > div > div > dl > dt:nth-child(5)").text #address
        driver.find_element(By.XPATH,"/html/body/div[1]/div/dl/dd[3]").text
        driver.find_element(By.CSS_SELECTOR,"body > div > div > dl > dt:nth-child(7)").text #city
        driver.find_element(By.XPATH,"/html/body/div[1]/div/dl/dd[4]").text
        driver.find_element(By.CSS_SELECTOR,"body > div > div > dl > dt:nth-child(9)").text #phone  
        driver.find_element(By.XPATH,"/html/body/div[1]/div/dl/dd[5]").text
        driver.find_element(By.CSS_SELECTOR,"body > div > div > dl > dt:nth-child(11)").text #email
        driver.find_element(By.XPATH,"/html/body/div[1]/div/dl/dd[6]").text     
        time.sleep(3)

    #TC 8
    def test_h_detail_edit(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Dashboard") # ke dashboard
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"Username").send_keys("syauqijufri") # isi username
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("anakpintar") # isi password
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click() #Login CTA
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/table/tbody/tr[7]/td[7]/a[2]").click() #detail CTA
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"body > div > p > a.btn.btn-link").click() #back dashboard
        time.sleep(3)
unittest.main()

#tekan (ctrl+?) buat jadiin komen per blok test case