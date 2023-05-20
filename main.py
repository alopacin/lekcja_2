# Program, ktory oblicza pozostałą kwotę kredytu do spłacenia z danych wejściowych wprowadzonych przez użytkownika

from inflation import *
# pobranie danych wejsciowych od użytkownika
initial_loan = float(input('Podaj wartość początkową kredytu: '))
loan_rate = float(input('Podaj oprocentowanie kredytu: '))
installment = float(input('Podaj stałą wysokość raty: '))

# glowna czesc programu

#styczen
interest = (loan_rate - january)
print(interest)
styczen = initial_loan - installment + (installment * (interest / 100))
print('Twoja pozostała kwota kredytu to {:.2f}'.format(styczen))

# luty
interest = (loan_rate - february)
luty = styczen - installment + (installment * (interest / 100))
less = styczen - luty
print('Twoja pozostała kwota kredytu to {:.2f}, to {:.2f} mniej niż w poprzednim miesiącu'.format(luty, less))

# marzec
interest = (loan_rate - march)
marzec = luty - installment + (installment * (interest / 100))
less = luty - marzec
print('Twoja pozostała kwota kredytu to {:.2f}, to {:.2f} mniej niż w poprzednim miesiącu'.format(marzec, less))

# kwiecień
interest = (loan_rate - april)
kwiecien  = marzec - installment + (installment * (interest / 100))
less = marzec - kwiecien
print('Twoja pozostała kwota kredytu to {:.2f}, to {:.2f} mniej niż w poprzednim miesiącu'.format(kwiecien, less))

# maj
interest = (loan_rate - may)
maj = kwiecien - installment + (installment * (interest / 100))
less = kwiecien - maj
print('Twoja pozostała kwota kredytu to {:.2f}, to {:.2f} mniej niż w poprzednim miesiącu'.format(maj, less))

# czerwiec
interest = (loan_rate - june)
czerwiec = maj - installment + (installment * (interest / 100))
less = maj - czerwiec
print('Twoja pozostała kwota kredytu to {:.2f}, to {:.2f} mniej niż w poprzednim miesiącu'.format(czerwiec, less))

# lipiec
interest = (loan_rate - july)
lipiec = czerwiec - installment + (installment * (interest / 100))
less = czerwiec - lipiec
print('Twoja pozostała kwota kredytu to {:.2f}, to {:.2f} mniej niż w poprzednim miesiącu'.format(lipiec, less))

#sierpien
interest = (loan_rate - august)
sierpien = lipiec - installment + (installment * (interest / 100))
less = lipiec - sierpien
print('Twoja pozostała kwota kredytu to {:.2f}, to {:.2f} mniej niż w poprzednim miesiącu'.format(sierpien, less))

#wrzesien
interest = (loan_rate - september)
wrzesien = sierpien - installment + (installment * (interest / 100))
less  = sierpien - wrzesien
print('Twoja pozostała kwota kredytu to {:.2f}, to {:.2f} mniej niż w poprzednim miesiącu'.format(wrzesien, less))

# pazdziernik
interest = (loan_rate - november)
pazdziernik = wrzesien - installment + (installment * (interest / 100))
less  = wrzesien - pazdziernik
print('Twoja pozostała kwota kredytu to {:.2f}, to {:.2f} mniej niż w poprzednim miesiącu'.format(pazdziernik, less))


# itd. :>



