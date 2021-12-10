from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import os


if __name__ == "__main__":
    # setting chrome driver
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Remote(
        command_executor=os.environ["SELENIUM_URL"],
        options=webdriver.ChromeOptions(),
    )
    # for wait loading
    driver.implicitly_wait(10)
    # for wait javascript function
    driver.set_script_timeout(10)
    # visit Google.com
    driver.get("https://www.google.com/")
    WebDriverWait(driver, 10).until(ExpectedConditions.presence_of_all_elements_located)
    # take a screenshot
    script: str = "document.body.style.zoom='{}%'"
    zoom_ratio: int = 100
    driver.execute_script(script.format(zoom_ratio))
    driver.save_screenshot("./screenshot_01.png")
    # search Google
    element: WebElement = driver.find_element(By.NAME, "q")
    element.send_keys("weather japan")
    element.submit()
    # take a screenshot
    driver.save_screenshot("./screenshot_02.png")
