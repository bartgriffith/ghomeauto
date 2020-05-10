#!/usr/bin/python

from decora_wifi import DecoraWiFiSession
from decora_wifi.models.person import Person
from decora_wifi.models.residential_account import ResidentialAccount
from decora_wifi.models.residence import Residence
import sys


if len(sys.argv) < 3:
    print('Usage: ./fetch.py [email] [pass]')

decora_email = sys.argv[1]
decora_pass = sys.argv[2]
decora_bright = None

session = DecoraWiFiSession()
session.login(decora_email, decora_pass)

# Gather all the available devices...

perms = session.user.get_residential_permissions()
all_residences = []
for permission in perms:
    if permission.residentialAccountId is not None:
        acct = ResidentialAccount(session, permission.residentialAccountId)
        for res in acct.get_residences():
            all_residences.append(res)
    elif permission.residenceId is not None:
        res = Residence(session, permission.residenceId)
        all_residences.append(res)
all_switches = []
for residence in all_residences:
    print("{'switches':[")
    for index, switch in enumerate(residence.get_iot_switches()):
        print(format(switch))
        if index < len(residence.get_iot_switches()) - 1:
            print(',')
            
    print("]}")

sys.stdout.flush()
Person.logout(session)