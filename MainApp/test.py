import string

# alf = "No"
alf = 'E'
countries = [{"Country": "Russia", "Langs": ["rus"]},
             {"Country": "Germany", "Langs": ["ger"]},
             {"Country": "France", "Langs": ["fra"]},
             {"Country": "Belgian", "Langs": ["bel", "fra"]},
             {"Country": "Espain", "Langs": ["esp"]},
             {"Country": "Argentina", "Langs": ["esp"]},
             {"Country": "England", "Langs": ["eng"]}]

print(f'countries = {countries}')
l = {"Langs": []}
for c in countries:
    for i in range(0, len(c["Langs"])):
        if True:  # l["Langs"].count(c["Langs"][i]) == 0:
            l["Langs"].append(c["Langs"][i])
print(f'l={l}')

lan = 'fra'
for c in countries:
    if c["Langs"].count(lan) != 0:
        print('FFFFRRRRAAA ', c["Country"])

for a in list(string.ascii_uppercase):
    print(a, end=' ')
print('\n')

d = countries.copy()
# print(f'd= {d}')
for c in countries:
    # print(c)
    if alf != "No" and c["Country"][0] != alf:
        d.pop(d.index(c))
    else:
        print(c["Country"][0], c["Country"])

if len(d) == 0: print('Nothing...')

# for c in d:

# print(countries)
# print(f'd= {d}')

