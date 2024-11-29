
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import base_page
import logging


class clickToCall_page(base_page):

    def __init__(self, driver):
        super().__init__(driver) 
        self.driver = driver

        #Boton Planes Hogar - Home
        self.boton_planesHogar = 'document.querySelector("#section-nav-home > andino-navigationbar-accesos-directos").shadowRoot.querySelector("div > div > a:nth-child(2) > andino-text-styler")'

        #Titulo Acceso Pagina Planes Hogar
        self.titulo_planesHogar = 'document.querySelector("#content > main > section > div.banner-1.box-banners.banner-redirect > andino-banner-seccion > andino-text:nth-child(1)")'

        #Boton Plan 500 Megas
        self.boton_500Megas = 'document.querySelector("#tab-planes-hogar-internet-hogar-1 > div > div > div > section > div > andino-card-planes").shadowRoot.querySelector("swiper-container > swiper-slide:nth-child(3) > div > div.card-plans-body > div > andino-button")'
        #Boton Plan 800 Megas
        self.boton_800Megas = 'document.querySelector("#tab-planes-hogar-internet-hogar-1 > div > div > div > section > div > andino-card-planes").shadowRoot.querySelector("swiper-container > swiper-slide.swiper-slide-next > div > div.card-plans-body > div > andino-button")'
        #Boton Plan Giga
        self.boton_Giga = 'document.querySelector("#tab-planes-hogar-internet-hogar-1 > div > div > div > section > div > andino-card-planes").shadowRoot.querySelector("swiper-container > swiper-slide.swiper-slide-active > div > div.card-plans-body > div > andino-button")'
        
        #Titulo Acceso Contratacion Online
        self.titulo_contratacion = 'document.querySelector("#root > section > div > div > div.plan-container.bg-white.col-12.col-lg-5.p-0 > div > div > div > andino-card-planes").shadowRoot.querySelector("div > div > div.plan-details > div.plan-subtitle > andino-text-styler").shadowRoot.querySelector("p > span:nth-child(2)")'

        #Boton "Quiero que me llamen"
        self.boton_llamada = 'document.querySelector("#root > section > div > div > div.flow-container.bg-neutral-050.col-12.col-lg-7.p-0 > div > div > div.choose-hiring-option > div > div > div.c2c-flow.mb-3 > andino-card-sm").shadowRoot.querySelector("div > div.content > andino-text-styler.title").shadowRoot.querySelector("p > span")'

        #Titulo Formulario
        self.titulo_formulario = 'document.querySelector("#phoneC2c").shadowRoot.querySelector("div > andino-input-label").shadowRoot.querySelector("label > div.body_2-xs > andino-text")'

        #Input telefono
        self.input_telefono = 'document.querySelector("#phoneC2c").shadowRoot.querySelector("#phoneC2c")'

        #Input correo
        self.input_correo = 'document.querySelector("#emailC2c").shadowRoot.querySelector("#emailC2c")'

        #Boton "Quiero que me llamen" para enviar formulario
        self.boton_enviar = 'document.querySelector("#formC2C > eds-btn")'

        #Titulo solicitud ingresada
        self.solicitud_ingresada = 'document.querySelector("#root > section > div > div > div.flow-container.bg-neutral-050.col-12.col-lg-7.p-0 > div > div > div > div > div > h3")'

    def click_boton_planesHogar(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_planesHogar)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))
        
    def get_text_titulo_planesHogar(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_planesHogar)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))
        
    def click_boton_500Megas(self):
        try:
            element = self.wait_until_element_is_visible(self.boton_500Megas)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))
        
    def click_boton_800Megas(self):
        try:
            element = self.wait_until_element_is_visible(self.boton_800Megas)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))
        
    def click_boton_Giga(self):
        try:
            element = self.wait_until_element_is_visible(self.boton_Giga)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))
        
    def get_text_titulo_contratacion(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_contratacion)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))
        
    def click_boton_llamada(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_llamada)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))
        
    def get_text_boton_llamada(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_llamada)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))
        
    def get_text_titulo_formulario(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.titulo_formulario)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))
        
    def send_keys_input_telefono(self, texto):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.input_telefono)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.send_keys(texto)
        except Exception as ex:
            raise Exception(str(ex))
        
    def send_keys_input_correo(self, texto):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.input_correo)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.send_keys(texto)
        except Exception as ex:
            raise Exception(str(ex))
        
    def click_boton_enviarSolcitud(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.boton_enviar)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            element.click()
        except Exception as ex:
            raise Exception(str(ex))
        
    def get_text_solicitud_ingresada(self):
        try:
            super().carga_pagina()
            element = self.wait_until_element_is_visible(self.solicitud_ingresada)
            if not super().is_displayed(element):
                print("Elemento no Desplegado.")
            if not super().is_enabled(element):
                print("Elemento no Disponible.")
            element.location_once_scrolled_into_view
            return element.text
        except Exception as ex:
            raise Exception(str(ex))
                

    # def send_keys(self, rutaJs, texto):
    #     driver = self.driver
    #     try:
    #         element = super().find_element_by_js(rutaJs)
    #         driver.execute_script("arguments[0].scrollIntoView();", element)
    #         if not super().is_displayed(element):
    #             print("Elemento no Desplegado.")
    #         if not super().is_enabled(element):
    #             print("Elemento no Disponible.")
    #         element.send_keys(texto)
    #     except Exception as ex:
    #         print(str(ex))
    #         raise
    
    # def click_button(self, rutaJs):
    #     driver = self.driver
    #     try:
    #         element = super().find_element_by_js(rutaJs)
    #         driver.execute_script("arguments[0].scrollIntoView();", element)
    #         if not super().is_displayed(element):
    #             print("Elemento no Desplegado.")
    #         if not super().is_enabled(element):
    #             print("Elemento no Disponible.")
    #         element.click()
    #     except Exception as ex:
    #         print(str(ex))
    #         raise
    
    # def get_text(self, rutaJs):
    #     driver = self.driver
    #     try:
    #         element = super().find_element_by_js(rutaJs)
    #         driver.execute_script("arguments[0].scrollIntoView();", element)
    #         if not super().is_displayed(element):
    #             print("Elemento No Desplegado")
    #         if not super().is_enabled(element):
    #             print("Elemento no Disponible")
    #         return element.text
    #     except Exception as ex:
    #         print(str(ex))
    #         raise