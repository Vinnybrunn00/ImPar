from rich import print
import pyfiglet as pg
import sys
import os

limpar = 'cls' if os.name == 'nt' else 'clear'
os.system(limpar)

banner = pg.figlet_format('ImPar')
print(banner)

def ImPar():
    qq = sys.platform
    print(f'Sistema Operacional: [cyan]{qq}[/]')

    while True:
        try:
            qq = int(input('\n\nDigite um numero: '))
            if qq % 2 == 1:
                print(f'{qq} [red]Ìmpar[/]')

            else:
                print(f'{qq} [cyan]Par[/]')
        except:
            print('Digite apenas numeros')

ImPar()
