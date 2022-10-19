""" Skriv en funktion som returner olika texter beroende på
 vad för typ argumentet var och vilket värde

Om argumentet var ett heltal och hade värdet 42:
"Answer to the Ultimate Question of Life, the Universe, and Everything"

I övrigt om det var ett heltal:
"Det var ett heltal"

Om argumentet var ett flyttal och är under 0:
"Var inte så negativ"

I övrigt om det är ett flyttal:
"Det var ett flyttal"

Om argumentet var en boolean och hade värdet False:
"Lögnare!"

Om argumentet var en boolean och hade värdet True:
"Det var en boolean"

Om argumentet var en sträng och hade värdet "Hej!"
"Hej på dig!"

I övrigt om det är en sträng:
"Det var en sträng"
 """

def type_checking(arg):
    
    if type(arg) == int:
        if arg == 42:
            return "Answer to the Ultimate Question of Life, the Universe, and Everything"
        else:
            return "Det var ett heltal"

    if type(arg) == float:
        if arg < 0:
            return "Var inte så negativ"
        else:
            return "Det var ett flyttal"

    if type(arg) == bool:
        if arg == False:
            return "Lögnare!"
        else:
            return "Det var en boolean" 

    if type(arg) == str:
        if arg == "Hej!":
            return "Hej på dig!"
        else:
            return "Det var en sträng" 