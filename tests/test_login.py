import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()

        self.driver.get("http://127.0.0.1:8000/")

        self.wait = WebDriverWait(self.driver, 10)

    def test_login_exitoso(self):

        email = self.driver.find_element(By.ID, "email")
        password = self.driver.find_element(By.ID, "password")

        email.send_keys("admin@demo.com")
        password.send_keys("Admin123")

        self.driver.find_element(
            By.CSS_SELECTOR,
            "button[type='submit']"
        ).click()

        message = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "message")
            )
        )

        self.assertEqual(
            message.text,
            "Inicio de sesión exitoso"
        )

    def test_login_incorrecto(self):

        email = self.driver.find_element(By.ID, "email")
        password = self.driver.find_element(By.ID, "password")

        email.send_keys("admin@demo.com")
        password.send_keys("ClaveIncorrecta")

        self.driver.find_element(
            By.CSS_SELECTOR,
            "button[type='submit']"
        ).click()

        message = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "message")
            )
        )

        self.assertEqual(
            message.text,
            "Correo o contraseña incorrectos"
        )

    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":
    unittest.main()