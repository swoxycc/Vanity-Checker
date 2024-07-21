import requests
import os
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

print(f"""{Fore.RED}
 discord --> discord.gg/cancode  🚀
---------------------------------------------------------------

 ╦  ╦╔═╗╔╗╔╦╔╦╗╦ ╦  ╔═╗╦ ╦╔═╗╔═╗╦ ╦╦╔═╔═╗╦═╗  ╔═╗╦ ╦╔═╗═╗ ╦╦ ╦
 ╚╗╔╝╠═╣║║║║ ║ ╚╦╝  ║  ╠═╣║╣ ║  ╠═╣╠╩╗║╣ ╠╦╝  ╚═╗║║║║ ║╔╩╦╝╚╦╝
  ╚╝ ╩ ╩╝╚╝╩ ╩  ╩   ╚═╝╩ ╩╚═╝╚═╝╩ ╩╩ ╩╚═╝╩╚═  ╚═╝╚╩╝╚═╝╩ ╚═ ╩ 

---------------------------------------------------------------
""")


txt_file = input("Url Lerin Kontrol Edileceği Txt Adını Girin 📝 : ")


if not os.path.exists(txt_file):
    print(f"{Fore.RED}Dosya bulunamadı: {txt_file}")
    exit()

valid = 0
invalid = 0
with open(txt_file, 'r') as handle:
    list = handle.readlines()
    for van in list:
        vanity = van.rstrip()
        check = requests.get(f"https://discord.com/api/v9/invites/{vanity}")
        if check.status_code == 404:
            print(f"{Fore.GREEN} {vanity} Valid")
            with open("valid.txt", "a+") as file:
                file.write(vanity)
                file.write("\n")
            valid += 1
        else:
            print(f"{Fore.RED} {vanity} Invalid")
            invalid += 1

print(f"Went through list.. {valid} valid, {invalid} invalid, total {len(list)}")
