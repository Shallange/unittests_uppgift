import unittest
from bil import Bil

enBil = Bil("Mercedes-Benz", "GLC", 12400,  280)
enBil2 = Bil("Volvo", "V40", 42000,  180)

assert (type(enBil) == Bil)
assert (enBil.märke == "Mercedes-Benz") # tog bort ett kommatecken som låg efterstringen 
assert (enBil.modell == "GLC")
assert (enBil.mil == 12400)
assert (enBil.topphastighet == 280)

assert (type(enBil2) == Bil)
assert (enBil2.märke == "Volvo") # tog bort ett kommatecken som låg efterstringen 
assert (enBil2.modell == "V40")
assert (enBil2.mil == 42000)
assert (enBil2.topphastighet == 180)
