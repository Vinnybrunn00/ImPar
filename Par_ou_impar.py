from rich import print

while True:
    try:
        qq = int(input('Digite um numero impar: '))
        if qq % 2 == 1:
            print('[green]CERTO[/]')

        else:
            print('[red]Errado[/]')
    except:
        print('Digite apenas numeros')