from config.init_config import init_config

def before_scenario(context, scenario):
    init_config(context, scenario)

def after_scenario(context, scenario):
    context.driver.quit()