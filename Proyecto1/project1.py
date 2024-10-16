#Imprimeix  la linia de preus

print("""Prices:
Bubblegum: $2
Toffee: $0.2
Ice cream: $5
Milk chocolate: $4
Doughnut: $2.5
Pancake: $3.2""")

#2pas imprimeix el earned amount
#imprimeix els noms dels items i lo que ha guanyat de cada un
#imprimeix la suma total de guanys.

print("""Earned amount:
Bubblegum: $202
Toffee: $118
Ice cream: $2250
Milk chocolate: $1680
Doughnut: $1075
Pancake: $80""")

total =  202 + 118 + 2250 + 1680 + 1075 + 80

print(f"Income:  ${total}")


#Paso 3: Pedir las gastos del staff
staff_Income = int(input("Staff expenses: "))

#Pedir los gastos adicionales
others = int(input("Other expenses: "))

#Sumar todos los gastos
Total_expenses = staff_Income + others

#Mostrar els beneficio resultante de restar el total de ingresos y los gastos 
print("Net income: $", total - Total_expenses)