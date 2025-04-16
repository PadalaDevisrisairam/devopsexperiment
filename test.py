from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

# Sample test data (Multiple sets of values)
test_data = [
    {"name":"sai","password":"123","confirmpassword":"123"},
    
    {"name":"sai","password":"123","confirmpassword":"123"},

    {"name":"sai","password":"123","confirmpassword":"13"}
]

@pytest.fixture(scope="module")
def driver():
    """Setup Selenium WebDriver"""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

@pytest.mark.parametrize("data", test_data)
def test_registration_form(driver, data):
    """Test registration form with multiple values"""
    driver.get("http://127.0.0.1:9000")  # Change URL if necessary
    time.sleep(2)  # Wait for page to load

    # Fill out the form
    driver.find_element(By.NAME, "name").send_keys(data["name"])
    driver.find_element(By.NAME, "password").send_keys(data["password"])
    driver.find_element(By.NAME, "confirmpassword").send_keys(data["confirmpassword"])
   


    # Submit the form
    driver.find_element(By.CLASS_NAME, "submitbutton").click()
    time.sleep(3)

    # Validate success (Adjust according to actual success message)
    assert "Success" in driver.page_source # Modify based on response

if __name__ == "__main__":
    pytest.main(["test.py"])
