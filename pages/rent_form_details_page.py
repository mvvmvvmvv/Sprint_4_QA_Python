from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import FaqAccordionLocators
from base_page


class RentFormDetailsPage:

    def __init__(self, driver):
        self.driver = driver

    