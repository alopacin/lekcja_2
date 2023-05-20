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

wysokosc_poczatkowa_kredytu = int(input('Podaj wartość początkową kredytu: '))
oprocentowanie_kredytu = int(input('Podaj jakie jest oprocentowanie kredytu: '))
kwota_raty = int(input('Podaj kwotę raty: '))


a = oprocentowanie_kredytu - inflacja
pozostala_kwota_kredytu = wysokosc_poczatkowa_kredytu - (kwota_raty * a)
y =

print('Twoja pozostała kwota kredytu to {}, to y mniej niż w poprzednim miesiącu'.format(pozostala_kwota_kredytu))
