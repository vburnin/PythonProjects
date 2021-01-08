# Declare Array of Planet Dictionaries

arrPlanets = [{"name": "Mercury", "weight": 76.15854}, {"name": "Venus", "weight": 0.91}, {"name": "Moon", "weight": 0.165},
              {"name": "Mars", "weight": 0.38}, {"name": "Jupiter", "weight": 2.34}, {"name": "Saturn", "weight": 0.93},
              {"name": "Uranus", "weight": 0.92}, {"name": "Neptune", "weight": 1.12},
              {"name": "Pluto", "weight": 0.066}]

# Prompt User for name and weight

sName = input("What is your name? ")
nMass = float(input('What is your weight on earth? '))

# Print name and answer text to console

print(sName, "here are your weights on our Solar System's planets:")

# For each planet print its name and weight of the person on it

for dicPlanet in arrPlanets:
    print(format("Weight on " + dicPlanet["name"] + ": ", "19s") + format(nMass * dicPlanet["weight"], "10,.3f"))

print(format(20, '.0%'))
print(format(0.2, '.0%'))
print(format(0.2 * 100, '.0%'))
print(format(0.2, '%'))