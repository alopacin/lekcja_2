'''Stwórz program, który na podstawie

    -tabeli inflacji wartości
    -oprocentowania kredytu,
    -kwoty początkowej kredytu
    -stałej wartości raty
    wyliczy wartość zadłużenia w każdym miesiącu przez 2 nadchodzące lata.

    Niech program wydrukuje dla każdego miesiąca następującą linię:
    Twoja pozostała kwota kredytu to X, to Y mniej niż w poprzednim miesiącu.
    Napisz program tak, by wysokość początkowego kredytu, oprocentowanie kredytu (ponad inflację) i kwota raty były pobierane ze standardowego wejścia (terminal).
    Przykładowe wartości kredytu i formułę do jego wyliczenia znajdziesz w załączniku powyżej. Skopiuj z niego wartości inflacji dla każdego miesiąca.'''

from inflation import *
# nadanie zmiennych
wysokosc_poczatkowa_kredytu = int(input('Podaj wartość początkową kredytu: '))
loan_rate = int(input('Podaj oprocentowanie kredytu: '))
kwota_raty = int(input('Podaj stałą wartość raty: '))

# algorytm wyliczający kwotę pozostałą do spłaty
#styczen
interest = loan_rate + january
amount_to_be_repaid = wysokosc_poczatkowa_kredytu - (kwota_raty + interest / 100)
print('Twoja pozostała kwota kredytu to {:.2f}'.format(amount_to_be_repaid))

#luty
interest = loan_rate + february
amount_to_be_repaid -=  kwota_raty + interest / 100
print('Twoja pozostała kwota kredytu to {:.2f}, to  mniej niż w poprzednim miesiącu'.format(amount_to_be_repaid,))

#marzec
interest = loan_rate + march
amount_to_be_repaid -= kwota_raty + interest / 100
print('Twoja pozostała kwota kredytu to {:.2f}, to  mniej niż w poprzednim miesiącu'.format(amount_to_be_repaid,))

TODO
#skończyć program

