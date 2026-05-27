# create list
countries = ["America", "Australia", "Egypt", "Brazil", "Argentina", "Belgium"]

# print list
print(countries)

# print length of list
print(len(countries))

# print data type
print(type(countries))

# access item using index
print(countries[2])

# access last item
print(countries[-1])

# slicing
print(countries[1:3])
print(countries[:3])
print(countries[2:])
print(countries[-3:-1])

# check item exists
if "Brazil" in countries:
    print("Yes, 'Brazil' is here.")

# insert item
countries.insert(2, "Portugal")
print(countries)

# add item at end
countries.append("England")
print(countries)

# add multiple items
countries.extend(["France", "Germany"])
print(countries)

# remove item
countries.remove("Egypt")
print(countries)

# remove item using pop
countries.pop(3)
print(countries)

# delete item
del countries[1]
print(countries)

# sort list
countries.sort()
print(countries)

# reverse list
countries.reverse()
print(countries)

# copy list
newCountries = countries.copy()
print(newCountries)

# loop through list
for country in countries:
    print(country)

# clear list
countries.clear()
print(countries)