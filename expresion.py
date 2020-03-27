import re
class expres_rg():
   
    def __init__(self,cadena):
        self.cadena=cadena

    def validar(self):
        exp = re.match("^[A-Z][\d]{3}[a-z]{3}[\W]{3}$",self.cadena)  
        return exp

print("Ingrese contraseña: ")
cadena = input()
expression = expres_rg(cadena)
if expression.validar() is None:
    print("La contraseña ingresada no es valida")
else:
    print("La contraseña ingresada es correcta")