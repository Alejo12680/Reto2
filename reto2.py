interes1=(int(input("Ingrese_interes_socio1 ")))
interes2=(int(input("Ingrese_interes_socio2 ")))
if (interes1<5) and (interes2<5):
	c1=(int(input("Ingrese_capital_socio1 ")))
	c2=(int(input("Ingrese_capital_socio2 ")))
	c3=(int(input("Ingrese_monto_negocio ")))
	i=0
	cap_final=(c1+c2)
	while (cap_final<c3):
		cap_inte1= float((c1*(1+interes1/100)**i))
		cap_inte2= float((c2*(1+interes2/100)**i))
		cap_final= float(cap_inte1+cap_inte2) 
		mes=i
		i+=1
	print("En el mes ",mes," pueden hacer el negocio :",f'{cap_final:.3f}', " es el rendimiento conjunto de la inversión")
else:
	print("Existe algún dato de interés inconsistente, hasta pronto")