Feature: Click to Call 

Scenario Outline: CTC Internet Hogar
    Given estoy en la pagina "https://www.entel.cl"
    And ingreso a Planes Hogar
    When selecciono el plan "<PLAN>"
    And selecciono "Quiero que me llamen"
    Then ingreso la solicitud de contacto

    Examples:
        | PLAN |
        | 500 Megas |
        | 800 Megas |
        | Giga |