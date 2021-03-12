import winsound
import time


def som(x,y):
    a = 0

    winsound.PlaySound('som.wav', winsound.SND_FILENAME)

    time.sleep(x)

    while a < y:
        a += 1
        winsound.PlaySound('som.wav', winsound.SND_FILENAME)


def main():
    x = int(input("informe qual intervalo de tempo você quer de um audio para o outro:\n"))
    y = int(input("Informe o numero de vez que você deseja repruduzir o audio:\n"))

    som(x,y)

main()
        



