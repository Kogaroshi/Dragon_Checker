from web3 import Web3, HTTPProvider
import sys
import os
import json
import time
import datetime

#---------------------------

endpoint_url = ""

#---------------------------

Dragon_address = sys.argv[1]

w3 = Web3(HTTPProvider(endpoint_url,request_kwargs={'timeout':60})) #Kovan node

with open("./abi/Dragon_abi.json") as f:
    Dragon_ABI = json.load(f)
Dragon = w3.eth.contract(abi=Dragon_ABI, address=Dragon_address)

dragon_name = Dragon.functions.name().call()

while(True):
    if(sys.platform == 'win32'):
        os.system('clr')
    else:
        os.system('clear')
    print('-----------------')
    print("Dragon ", dragon_name, Dragon_address)
    print("Health ", Dragon.functions.health().call(), "/", Dragon.functions.maxHealth().call())
    print("Health Regen ", Dragon.functions.healthRegeneration().call())
    print("Damages ", Dragon.functions.damage().call())
    print('-----------------')
    print("Uncleanliness ", Dragon.functions.getUncleanliness().call())
    print("Sleepiness ", Dragon.functions.getSleepiness().call())
    print("Hunger ", Dragon.functions.getHunger().call())
    print("Boredom ", Dragon.functions.getBoredom().call())
    print('-----------------')
    breed_cooldown = Dragon.functions.secondsUntilBreed().call()
    print("Can breed in  ",str(datetime.timedelta(seconds=breed_cooldown)))
    print('-----------------')
    atk_cooldown = Dragon.functions.secondsUntilAttack().call()
    print("Can attack in  ",str(datetime.timedelta(seconds=atk_cooldown)))
    print('-----------------')
    time.sleep(30)