from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class base_page:
    def __init__(self, driver):
        self.driver = driver
    
    def find_element_by_js(self, js_query):
        return self.driver.execute_script(f"return {js_query}")

    def ingreso_al_portal(self, URL):
        self.driver.maximize_window()
        self.driver.get(URL)

    def is_displayed(self, element, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of(element))
            return True
        except NoSuchElementException or StaleElementReferenceException as ex:
            print("Exception al elemento {element}: "+str(ex))    
            return False
    
    def is_enabled(self, element, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(element))
            return True
        except NoSuchElementException or StaleElementReferenceException as ex:
            print("Exception al elemento {element}: "+str(ex))
            return False
    
    def wait_until_element_is_visible(self, js_query, timeout=30):
        try:
            return WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.execute_script(
                    f"""
                    return {js_query};
                    """
                )
            )
        except TimeoutException as ex:
            raise TimeoutException(f"No se encuentra el elemento {js_query} en {timeout} segundos: "+str(ex))
    
    def carga_pagina(self, timeout=30):
        def fetches_cargados(driver):
            return driver.execute_script("""
                return performance.getEntriesByType('resource').length;
            """) >= 5
        try:
            WebDriverWait(self.driver, timeout).until(fetches_cargados)
        except Exception as e:
            raise TimeoutError(f"{e}: No se alcanzó el mínimo de 5 fetches en {timeout} segundos.")
        

