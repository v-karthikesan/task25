# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time


def setup_driver():
    # Initialize WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.imdb.com/search/name/")
    return driver


def click_element(driver, by, value):
    try:
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((by, value)))
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
    except Exception as e:
        print(f"Error clicking element: {e}")


def main():
    driver = setup_driver()
    try:
        # Scroll the window
        driver.execute_script("window.scrollTo(0, 500);")

        # Click on the Name field
        click_element(driver, By.XPATH, "//div[contains(text(),'Name')]")

        # Enter name in name element
        name_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "name-text-input")))
        name_input.send_keys("Ajith")

        # Click on the Birth Date field
        click_element(driver, By.XPATH, "//div[contains(text(),'Birth date')]")

        # Enter input in birth date field
        birth_start_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "birth-date-start-input")))
        birth_start_input.send_keys("01/01/1970")
        birth_end_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "birth-date-end-input")))
        birth_end_input.send_keys("01/07/2024")
        click_element(driver, By.XPATH, "//div[contains(text(),'Birth date')]")  # Close the dropdown

        # Click on the Birthday field
        click_element(driver, By.XPATH, "//div[contains(text(),'Birthday')]")

        # Enter birthday
        birthday_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "birthday-input")))
        birthday_input.send_keys("01-01")
        click_element(driver, By.XPATH, "//div[contains(text(),'Birthday')]")  # Close the dropdown

        # Click on the Awards field
        click_element(driver, By.XPATH, "//div[contains(text(),'Awards & recognition')]")

        # Click on the button within the Awards section
        click_element(driver, By.XPATH, "//div[@id='awardsAccordion']//button[1]")
        click_element(driver, By.XPATH, "//div[contains(text(),'Awards & recognition')]")  # Close the dropdown

        # Click on the Page Topics accordion
        click_element(driver, By.XPATH, "//label[@for='accordion-item-pageTopicsAccordion']")

        # Select "Quotes" from the dropdown using Selenium Select
        page_topics_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "within-topic-dropdown")))
        search = Select(page_topics_dropdown)
        search.select_by_visible_text("Quotes")
        click_element(driver, By.XPATH, "//label[@for='accordion-item-pageTopicsAccordion']")  # Close the dropdown

        # Scroll to the Death Date field
        death_date = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Death date')]")))
        driver.execute_script("arguments[0].scrollIntoView(true);", death_date)
        death_date.click()

        death_date_from_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "death-date-start-input")))
        death_date_from_input.send_keys("01/01/2050")
        death_date_to_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "death-date-end-input")))
        death_date_to_input.send_keys("10/10/2050")
        click_element(driver, By.XPATH, "//div[contains(text(),'Death date')]")  # Close the dropdown

        # Click the Gender Identity and select the female value
        click_element(driver, By.XPATH, "//div[contains(text(),'Gender identity')]")
        gender_identity_value = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='genderIdentityAccordion']//button[2]")))
        gender_identity_value.click()

        # Click on the Credits field
        click_element(driver, By.XPATH,
                      "//label[@for='accordion-item-filmographyAccordion']//span[@class='ipc-accordion_item_chevron']//*[name()='svg']")

        # Send keys to the input field
        credits_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']")))
        credits_input.send_keys("good")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
