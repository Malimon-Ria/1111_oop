import colorama

print(dir(colorama))
print(help(colorama))

from colorama import Fore
print(Fore.GREEN + 'Hello' + Fore.RESET)
print(Fore.BLUE + 'Python' + Fore.RESET)
