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
    print("Attack Damages ", Dragon.functions.damage().call())
    attack_cooldown = Dragon.functions.attackCooldown().call()
    print("Attack Cooldown ", attack_cooldown)
    print('-----------------')
    print("Uncleanliness ", Dragon.functions.getUncleanliness().call())
    print("Sleepiness ", Dragon.functions.getSleepiness().call())
    print("Hunger ", Dragon.functions.getHunger().call())
    print("Boredom ", Dragon.functions.getBoredom().call())
    print('-----------------')
    breed_count = Dragon.functions.breedCount().call()
    print("Eggs layed ", breed_count)
    print('-----------------')
    breed_cooldown = ((12 * 3600)  * (2**(breed_count + 1)))
    sec_until_breed = Dragon.functions.secondsUntilBreed().call()
    real_breed_sec = (2 * breed_cooldown) - sec_until_breed
    print("Can breed in ~ ",str(datetime.timedelta(seconds=real_breed_sec)))
    print('-----------------')
    sec_until_atk = Dragon.functions.secondsUntilAttack().call()
    real_atk_sec = (2 * attack_cooldown) - sec_until_atk
    print("Can attack in ~ ",str(datetime.timedelta(seconds=real_atk_sec)))
    print('-----------------')
    upgrade_cooldown = 3600
    sec_until_upgrade = Dragon.functions.secondsUntilUpgrade().call()
    real_upgrade_sec = (2 * upgrade_cooldown) - sec_until_upgrade
    print("Can upgrade in ~ ",str(datetime.timedelta(seconds=real_upgrade_sec)))
    print('-----------------')
    time.sleep(30)