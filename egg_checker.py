from web3 import Web3, HTTPProvider
import sys
import os
import json
import time
import datetime
from dotenv import load_dotenv

load_dotenv()

#---------------------------

endpoint_url = os.environ['FANTOM_URI']

#---------------------------

Egg_address = sys.argv[1]

w3 = Web3(HTTPProvider(endpoint_url,request_kwargs={'timeout':60})) #Kovan node

with open("./abi/Egg_abi.json") as f:
    Egg_ABI = json.load(f)
Egg = w3.eth.contract(abi=Egg_ABI, address=Egg_address)

egg_name = Egg.functions.name().call()

while(True):
    if(sys.platform == 'win32'):
        os.system('clr')
    else:
        os.system('clear')

    current_block = w3.eth.block_number
    current_timestamp = (w3.eth.get_block(current_block))['timestamp']

    print('-----------------')
    print("Egg ", egg_name, Egg_address)
    birth_duration = 24 * 3600
    creationTimestamp = Egg.functions.creationTimestamp().call()
    tributes_count = Egg.functions.getTributes().call()
    sec_until_hatch = Egg.functions.secondsUntilHatched().call()
    real_hatch_sec = 0
    if(sec_until_hatch != 0):
        real_hatch_sec = (creationTimestamp + birth_duration - tributes_count * 100) - current_timestamp
    print("Will hatch in ~ ",str(datetime.timedelta(seconds=real_hatch_sec)))
    print("Tributes given ",tributes_count)
    print('-----------------')
    time.sleep(30)