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
initial_loan = int(input('Podaj wartość początkową kredytu: '))
loan_rate = int(input('Podaj oprocentowanie kredytu: '))
installment = int(input('Podaj stałą wartość raty: '))

# algorytm wyliczający kwotę pozostałą do spłaty

#styczen
interest = loan_rate + january
styczen = initial_loan - (installment + (interest / 10))
print('Twoja pozostała kwota kredytu to {:.2f}'.format(styczen))

#luty
interest = loan_rate + february
luty = styczen - (installment + (interest / 10))
mniej = styczen - luty
print('Twoja pozostała kwota kredytu to {:.2f}, to {:.2f} mniej niż w poprzednim miesiącu'.format(luty, mniej))

#marzec
interest = loan_rate + march
marzec = luty - (installment + (interest / 10))
mniej = luty- marzec
print('Twoja pozostała kwota kredytu to {:.2f}, to {:.2f} mniej niż w poprzednim miesiącu'.format(marzec, mniej))

#kwiecień
interest = loan_rate + april
kwiecien  = marzec - (installment + (interest / 10))
print('Twoja pozostała kwota kredytu to {:.2f}, to  mniej niż w poprzednim miesiącu'.format(kwiecien))

# maj
interest = loan_rate + may
maj = kwiecien - (installment + (interest / 10))
print('Twoja pozostała kwota kredytu to {:.2f}, to  mniej niż w poprzednim miesiącu'.format(maj))


