import logging
import time
from behave import *
from utils.utils import *

@given(u'estoy en la pagina "{url}"')
def step_impl(context, url):
    context.driver.get("https://www.entel.cl")   
    attach_screenshot(context.driver)

@step(u'ingreso a Planes Hogar')
def step_impl(context):
    try:
        context.clickToCall_page.click_boton_planesHogar()
        time.sleep(5)
        assert "Planes Internet Hogar" in context.clickToCall_page.get_text_titulo_planesHogar()
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))

@when(u'selecciono el plan "{plan}"')
def step_impl(context, plan):
    try:
        print(plan)
        match plan:
            case "500 Megas":
                context.clickToCall_page.click_boton_500Megas()
            case "800 Megas":
                context.clickToCall_page.click_boton_800Megas()
            case "Giga":
                context.clickToCall_page.click_boton_Giga()
        time.sleep(5)
        assert plan in context.clickToCall_page.get_text_titulo_contratacion()
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))

@when(u'selecciono "{texto}"')
def step_impl(context, texto):
    try:
        assert texto in context.clickToCall_page.get_text_boton_llamada()
        context.clickToCall_page.click_boton_llamada()
        assert "Ingresa tu número" in context.clickToCall_page.get_text_titulo_formulario()
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))

@then(u'ingreso la solicitud de contacto')
def step_impl(context):
    try:
        context.clickToCall_page.send_keys_input_telefono("959595959")
        context.clickToCall_page.send_keys_input_correo("pruebaQA@QAEntel.cl")
        attach_screenshot(context.driver)
        context.clickToCall_page.click_boton_enviarSolcitud()
        time.sleep(5)
        assert "¡Recibimos tu solicitud!" in context.clickToCall_page.get_text_solicitud_ingresada()
        attach_screenshot(context.driver)
    except AssertionError as ex:
        attach_screenshot(context.driver)
        raise AssertionError(str(ex))