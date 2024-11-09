import random

with open('projekt KPN\wygrana.txt', 'r') as f:
    wygrana = f.read()
with open('projekt KPN\przegrana.txt', 'r') as f:
    przegrana = f.read()
with open('projekt KPN\Remis.txt', 'r') as f:
    remis = f.read()


def gra():
    user = input("jaki jest twój wybór? 'k' dla kamien, 'p' dla papier, 'n' dla nożyce\n")
    computer = random.choice(['k', 'p', 'n'])
 
    if user == computer:
        return remis

    if win(user, computer):
        return wygrana
         

    
    return przegrana

def win(gracz, przeciwnik):
    if (gracz == 'k' and przeciwnik == 'n') or (gracz == 'n' and przeciwnik == 'p') or (gracz == 'p' and przeciwnik == 'k'):
        return True
    
print(gra())