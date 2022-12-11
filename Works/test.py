class Airport:
    def __init__(self,a, b, c):
        self.name = a
        self.country = b
        self.city = c


allAirports = []
c = ['YYZ', 'Canada', 'Toronto']
tmp = Airport(c[0],c[1],c[2])
allAirports.append(tmp)


# initialize a empty dictionary
allFlights = {}
# for example, if the extracted data looks like this
c = ['YYZ', 'C201']
# check if the key is exist
if c[0] not in allFlights.keys():
    # if not, create a key-value pair.
    # note the value should be a list
    allFlights[c[0]] = [c[1]]
else:
    # if it is, add the new flight info into the list.
    allFlights[c[0]] = allFlights[c[0]].append(c[1])

print(allFlights)