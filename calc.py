# konvertē datu mērvienības
def megabyte_to_megabit(megabyte):
   result = megabyte * 8

   return result

# saskaiti degvielas patēriņu uz 100 km
def fuel_consumption(litres, kilometers):
   koef = 100 / kilometers
   result =int(litres * koef)
   return result

# konvertē temperatūru
def celsius_to_fahrenheit(celsius):
    result = celsius*9/5+32
    return result

# saliec visus skaitļus pirms dota skaitļa (izmanto for)
def sigma(tail):
    result = 0
    for i in range(1,tail+1):
        result += i
    return result

# nokonvertē svaru uz tuvāko mērvienību - grams, kilograms, tonna (izmanto if)
def weight(grams):
    if grams < 1000:
        return(str(grams)+"g")
    elif grams < 100000:
        result = grams / 1000
        return(str(int(result))+"kg")
    elif grams < 1000000:
        result=grams/100000
        return(str(int(result))+"c")
    elif grams >= 1000000:
        result=grams/1000000
        return(str(int(result))+"t")

mode = str(input("Choose mode(Mg; Fc; Cf; Si; W): "))

if mode == "Mg":
    megabyte = int(input("Enter megabytes amount: "))
    print(megabyte_to_megabit(megabyte))
elif mode == "Fc":
    litres = int(input("Enter liters amount: "))
    kilometers = int(input("Enter kilometres amount: "))
    print(fuel_consumption(litres, kilometers))
elif mode == "Cf":
    celsius = int(input("Enter celsius amount: "))
    print(celsius_to_fahrenheit(celsius))
elif mode == "Si":
    tail = int(input("Enter tail: "))
    print(sigma(tail))
elif mode == "W":
    grams = int(input("Enter garms amount: "))
    print(weight(grams))
