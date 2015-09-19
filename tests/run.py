import json
from ..wa_core.wabot_stack import wabot_stack

def run(creds):
    CREDENTIALS = (creds["phone"], creds["passw"])
    wabot_stack(CREDENTIALS, True ).start();

try:
    fh = open("WABot2/configs/config.json","r")
    creds = json.loads(fh.read())
    run(creds)
except Exception as e:
    print("Conifg Loading/Parsing Failed")
    print(e)
    exit()
