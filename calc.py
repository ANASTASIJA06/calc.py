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
    return result

# nokonvertē svaru uz tuvāko mērvienību - grams, kilograms, tonna (izmanto if)
def weight(grams):
    return str(grams) + "g"

mode = str(input("Choose mode(mg; fc; cf; si; w): "))

if mode == "mg":
    megabyte = int(input("Enter megabytes amount: "))
    print(megabyte_to_megabit(megabyte))
elif mode == "fc":
    litres = int(input("Enter liters amount: "))
    kilometers = int(input("Enter kilometres amount: "))
    print(fuel_consumption(litres, kilometers))
elif mode == "cf":
    celsius = int(input("Enter celsius amount: "))
    print(celsius_to_fahrenheit(celsius))
elif mode == "si":
    tail = int(input("Enter tail: "))
    print(sigma(tail))
elif mode == "w":
    grams = int(input("Enter garms amount: "))
    print(weight(grams))
