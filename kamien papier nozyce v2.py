import random

wygrana = open('projekt KPN\wygrana.txt', 'r')
przegrana = open('projekt KPN\przegrana.txt', 'r')
remis = open('projekt KPN\Remis.txt', 'r')


def gra():
    user = input("jaki jest twój wybór? 'k' dla kamien, 'p' dla papier, 'n' dla nożyce\n")
    computer = random.choice(['k', 'p', 'n'])
 
    if user == computer:
        return print(remis.read())

    if win(user, computer):
        return print(wygrana.read())
         

    
    return print(przegrana.read())

def win(gracz, przeciwnik):
    if (gracz == 'k' and przeciwnik == 'n') or (gracz == 'n' and przeciwnik == 'p') or (gracz == 'p' and przeciwnik == 'k'):
        return True
    
print(gra())