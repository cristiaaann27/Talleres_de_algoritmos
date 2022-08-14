dinero = int(input("Ingrese cantidad en COP: "))

total = ""

cien_mil = dinero  // 100000
if cien_mil > 0:
    total = total + ("100000,"*cien_mil)
    dinero -= (100000*cien_mil)

cincuenta_mil = dinero // 50000
if cincuenta_mil > 0:
    total = total + ("50000,"*cincuenta_mil)
    dinero -= (50000*cincuenta_mil)
    
veinte_mil = dinero // 20000
if veinte_mil > 0:
    total = total + ("20000,"*veinte_mil)
    dinero -= (20000*veinte_mil)
        
diez_mil = dinero // 10000
if diez_mil > 0:
    total = total + ("10000,"*diez_mil)
    dinero -= (10000*diez_mil)
            
 
cinco_mil = dinero // 5000
if cinco_mil > 0:
    total = total + ("5000"*cinco_mil)
    dinero -= (5000*cinco_mil)
                
dos_mil = dinero // 2000
if dos_mil > 0:
    total = total + ("2000,"*dos_mil)
    dinero -= (2000*dos_mil)
                    
mil = dinero // 1000
if mil > 0:
    total = total + ("1000,"*mil)
    dinero -= (1000*mil)
                        
quinientos = dinero // 500
if quinientos > 0:
    total = total + ("500,"*quinientos)
    dinero -= (500*quinientos)

                                                       
doscientos = dinero // 200
if doscientos > 0:
    total = total + ("200,"*doscientos)
    dinero -= (200*doscientos)
                                
cien = dinero // 100
if cien > 0:
    total = total + ("100,"*cien)
    dinero -= (100*cien)
                                    
cincuenta = dinero //50
if cincuenta > 0:
    total = total + ("50,"*cincuenta)                                          
print(total)
                                           

    



   