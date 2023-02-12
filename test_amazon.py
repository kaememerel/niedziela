import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from time import sleep

#PARAMETRY TESTU

#DANE TESTOWE
imie = "Marceli"
nazwisko = "Kopytko"
email = "marcelikopytko@gmail.com"
krotkie_haslo = "mark1"
dlugie_haslo = "koteczek"

class RejestracjaNowegoUzytkownika(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("/usr/bin/chromedriver")
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.pl/")
        self.driver.find_element(By.ID, 'sp-cc-accept').click()
    def testZaKrotkieHaslo(self):
        sleep(4)
        self.driver.find_element(By.ID, "nav-link-accountList").click()
        self.driver.find_element(By.ID, "createAccountSubmit").click()
        self.driver.find_element(By.ID, "ap_customer_name").send_keys(imie, " ", nazwisko)
        self.driver.find_element(By.ID, "ap_email").send_keys(email)
        password1 = self.driver.find_element(By.ID, "ap_password")
        password1.send_keys(krotkie_haslo)
        password_check = self.driver.find_element(By.ID, "ap_password_check")
        password_check.send_keys(krotkie_haslo)
        self.driver.find_element(By.ID, "continue").click()
        error_span1 = self.driver.find_element(locate_with(By.XPATH, '//*[@id="auth-password-invalid-password-alert"]/div/div').near(password1))
        error_span2 = self.driver.find_element(locate_with(By.XPATH, '//*[@id="auth-password-invalid-password-alert"]/div/div').above(password_check))
        self.assertEqual(error_span1.id, error_span2.id)
        error_number = len(self.driver.find_elements(By.XPATH, '//*[@id="auth-password-invalid-password-alert"]/div/div'))
        self.assertEqual(error_number, 1)
        self.assertEqual(error_span1.text, "Hasło powinno składać się z minimum 6 znaków.")
    def testRozneHaslo(self):
        sleep(4)
        self.driver.find_element(By.ID, "nav-link-accountList").click()
        self.driver.find_element(By.ID, "createAccountSubmit").click()
        self.driver.find_element(By.ID, "ap_customer_name").send_keys(imie, " ", nazwisko)
        self.driver.find_element(By.ID, "ap_email").send_keys(email)
        password1 = self.driver.find_element(By.ID, "ap_password")
        password1.send_keys(dlugie_haslo)
        password_check = self.driver.find_element(By.ID, "ap_password_check")
        password_check.send_keys(krotkie_haslo)
        self.driver.find_element(By.ID, "continue").click()
        error_span1 = self.driver.find_element(locate_with(By.XPATH, '//*[@id="auth-password-mismatch-alert"]/div/div').near(password1))
        error_span2 = self.driver.find_element(locate_with(By.XPATH, '//*[@id="auth-password-mismatch-alert"]/div/div').below(password_check))
        self.assertEqual(error_span1.id, error_span2.id)
        error_number = len(self.driver.find_elements(By.XPATH, '//*[@id="auth-password-mismatch-alert"]/div/div'))
        self.assertEqual(error_number, 1)
        self.assertEqual(error_span1.text, "Podane hasła różnią się od siebie.")
    def tearDown(self):
        sleep(4)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
