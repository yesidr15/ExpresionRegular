import sys
import re
#A485btf%$(
class expres_rg():
   
    def __init__(self,cadena):
        self.cadena=cadena

    def validar(self):
        
        exp = re.match("^[A-Z][\d]{3}[a-z]{3}[\W]{3}$",self.cadena)  

        if exp is None:
            exp = False
       
        else:
            exp= True
        return exp


cadena = sys.argv[1]
expression = expres_rg(cadena)
expression.validar()
print(expression.validar())