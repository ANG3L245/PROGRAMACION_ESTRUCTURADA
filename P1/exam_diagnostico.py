# Limpiar terminal
def borrarPantalla():
    print("\033c")
    
#
def ventaAutos(opc,autos,acum_pv):
    borrarPantalla()
    while opc=="S":
        #Entrada
        marca=input("Marca: ").strip().upper()
        origen=input("Origen: ").strip().upper()
        costo=float(input("Costo: "))

        #proceso
        impuesto=0
        if origen=="ALEMANIA":
            impuesto=0.20
        elif origen=="JAPON":
            impuesto=0.20
        elif origen=="ITALIA":
            impuesto=0.15
        elif origen=="USA":
            impuesto=0.08
            
        impuesto_pesos=costo*impuesto
        pv=impuesto_pesos+costo
        

        #salida
        print(f"El impuesto  pagar es: ${impuesto_pesos}")
        print(f"El precio de venta es: ${pv}")
        
        autos+=1
        acum_pv+=pv
        
        opc=input("¿Deseas realizar otra vez el proceso (S/N): ").upper().strip()
    return autos,acum_pv
        
        
OPC="S"
AUTOS=0
ACUM_PV=0        
tot_autos,acum_precios=ventaAutos(OPC,AUTOS,ACUM_PV)
print(f"El total de los vehiculos ingresados es: {tot_autos} \n Y el monto total de los precios de venta es: ${acum_precios}")