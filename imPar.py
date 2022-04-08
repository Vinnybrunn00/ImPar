from rich import print
import pyfiglet as pg
import sys
import os

limpar = 'cls' if os.name == 'nt' else 'clear'
os.system(limpar)

def Banner():
    banner = pg.figlet_format('ImPar')
    print(banner)

def ImPar():
    Banner()
    system = sys.platform
    print(f'Sistema Operacional: [cyan]{system}[/]')

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
