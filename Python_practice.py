counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver':
        print(counties[1])

if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list.")

for county in counties:
    print(county)

counties_dict = {"Arapahoe": 422829,"Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(counties_dict[county])

for voters in counties_dict.values():
    print(voters)

for county, voters in counties_dict.items():
    print(county, voters)

for county, voters in counties_dict.items():
    print(str(county) + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for key, value in voting_data[0].items():
    print(f"{voting_data[0]['county']} county has {voting_data[0]['registered_voters']} registered voters.")
for key, value in voting_data[1].items():
    print(f"{voting_data[1]['county']} county has {voting_data[1]['registered_voters']} registered voters.")
for key, value in voting_data[2].items():
    print(f"{voting_data[2]['county']} county has {voting_data[2]['registered_voters']} registered voters.")
