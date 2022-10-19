""" Skapa en egen exception class som heter:
EgenException
Klassen ska ärva utav 
Exception  """


""" Skapa en funktion som heter:
Kasta
Metoden ska kasta/raise EgenException
"""

class EgenException(Exception):
    
    def __init__(self,error="own Exeption message: kasta() not kastad"):
        self.error = error

def Kasta():
    try:
        Kasta()
    except:
        raise EgenException