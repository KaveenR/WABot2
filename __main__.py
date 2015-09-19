import json
import logging as lg
from .wa_core.wabot_stack import wabot_stack

def run(creds):
    CREDENTIALS = (creds["phone"], creds["passw"])
    wabot_stack(CREDENTIALS, True ).start();

try:
    fh = open("WABot2/configs/config.json","r")
    creds = json.loads(fh.read())
    run(creds)
except Exception as e:
    lg.error("Conifg Loading/Parsing Failed " + str(e))
    exit()
