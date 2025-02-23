destinations = [
    "Paris, France",
    "Shanghai, China",
    "Los Angeles, USA",
    "São Paulo, Brazil",
    "Cairo, Egypt",
]

test_traveler = [["Erin Wilkes", "Shanghai, China"], ["historical site", "art"]]


def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index


print(get_destination_index("Los Angeles, USA"))
# print(get_destination_index("Hyderabad, India"))


def get_traveler_location(traveler):
    traveler_destination = traveler[0][1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index


test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)

attractions = [[], [], [], [], []]


def add_attraction(destination, attraction):
    destination_index = get_destination_index(destination)
    attractions[destination_index].append(attraction)
    return


print(add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]]))
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction(
    "Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]]
)
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# print(attractions)


def find_attractions(destination, interests):
    attractions_in_city = []
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]

    attraction_tags = []
    attractions_with_interest = []
    possible_attraction = []

    for item in attractions_in_city:
        possible_attraction.append(item)
        attraction_tags.append(item[1])

    for item in possible_attraction:
        for interest in interests:
            if interest in item[1]:
                attractions_with_interest.append(item[0])

    return attractions_with_interest


# print(find_attractions("Los Angeles, USA", ["art"]))
print(find_attractions("Paris, France", ["monument"]))


def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    attraction_traveler = find_attractions(traveler_destination, traveler_interests)

    # getting all the attractions in string format suppossing that the attractions are in the list
    attraction_traveler_string = ""
    for i in range(len(attraction_traveler)):
        attraction_traveler_string += f"the {attraction_traveler[i]}"

    greeting = f"Hi {traveler[0]}, we think you'll like these places around {traveler_destination}: {attraction_traveler_string}"
    return greeting


print(get_attractions_for_traveler(["Dereck Smill", "Paris, France", ["monument"]]))
# print(get_attractions_for_traveler(["Dereck Smill", "Paris, France", ["monument"]]))
