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
# pobranie danych wejsciowych
initial_loan = float(input('Podaj wartość początkową kredytu: '))
loan_rate = float(input('Podaj oprocentowanie kredytu: '))
installment = float(input('Podaj stałą wartość raty: '))

# glowna czesc programu

#styczen
interest = (loan_rate - january) / 12
print(interest)
styczen = initial_loan - installment * (interest / 10)
print('Twoja pozostała kwota kredytu to {:.2f}'.format(styczen))

# luty
interest = (loan_rate - february) / 12
luty = styczen - (installment * (interest / 10))
less = styczen - luty
print('Twoja pozostała kwota kredytu to {:.2f}, to {:.2f} mniej niż w poprzednim miesiącu'.format(luty, less))

# marzec
interest = (loan_rate - march) / 12
marzec = luty - (installment * (interest / 10))
less = luty - marzec
print('Twoja pozostała kwota kredytu to {:.2f}, to {:.2f} mniej niż w poprzednim miesiącu'.format(marzec, less))

# kwiecień
interest = (loan_rate - april) / 12
kwiecien  = marzec - (installment * (interest / 10))
less = marzec - kwiecien
print('Twoja pozostała kwota kredytu to {:.2f}, to {:.2f} mniej niż w poprzednim miesiącu'.format(kwiecien, less))

# maj
interest = (loan_rate - may) / 12
maj = kwiecien - (installment * (interest / 10))
less = kwiecien - maj
print('Twoja pozostała kwota kredytu to {:.2f}, to {:.2f} mniej niż w poprzednim miesiącu'.format(maj, less))

# czerwiec
interest = (loan_rate - june) / 12
czerwiec = maj - (installment * (interest / 10))
less = maj - czerwiec
print('Twoja pozostała kwota kredytu to {:.2f}, to {:.2f} mniej niż w poprzednim miesiącu'.format(czerwiec, less))

# lipiec
interest = (loan_rate - july) / 12
lipiec = czerwiec - (installment * (interest / 10))
less = czerwiec - lipiec
print('Twoja pozostała kwota kredytu to {:.2f}, to {:.2f} mniej niż w poprzednim miesiącu'.format(lipiec, less))

#sierpien
interest = (loan_rate - august) / 12
sierpien = lipiec - (installment * (interest / 10))
less = lipiec - sierpien
print('Twoja pozostała kwota kredytu to {:.2f}, to {:.2f} mniej niż w poprzednim miesiącu'.format(sierpien, less))

#wrzesien
interest = (loan_rate - september) / 12
wrzesien = sierpien - (installment * (interest / 10))
less  = sierpien - wrzesien
print('Twoja pozostała kwota kredytu to {:.2f}, to {:.2f} mniej niż w poprzednim miesiącu'.format(wrzesien, less))

# pazdziernik
interest = (loan_rate - november) / 12
pazdziernik = wrzesien - (installment * (interest / 10))
less  = wrzesien - pazdziernik
print('Twoja pozostała kwota kredytu to {:.2f}, to {:.2f} mniej niż w poprzednim miesiącu'.format(pazdziernik, less))




