# Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.

# Return the count of how many numbers in the list are divisible by 10.


def divisible_by_ten(nums):
    count = 0
    for num in nums:
        if num % 10 == 0:
            count += 1
    return count


# function Greetings


def add_greetings(names):
    # other way easier greetings = ["Hello, " + name for name in names]
    greetings = []
    for name in names:
        greetings.append("Hello, " + name)
    return greetings


# function delete starting even numbers


def delete_starting_evens(my_list):
    while len(my_list) > 0 and my_list[0] % 2 == 0:
        my_list = my_list[1:]
    return my_list


print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))


def odd_indices(my_list):
    new_list = []
    for i in range(
        1, len(my_list), 2
    ):  # range function takes 3 arguments, start, stop, step
        new_list.append(my_list[i])
    return new_list


def exponents(bases, powers):
    my_list = []
    for num in bases:
        for nums in powers:
            my_list.append(pow(num, nums))

    return my_list


def larger_sum(
    lst1, lst2
):  # I was thinking here to use map but map gives a list an array of values
    sum1 = 0
    sum2 = 0
    for num in lst1:
        sum1 += num
    for num in lst2:
        sum2 += num

    if sum2 > sum1:
        return lst2
    else:
        return lst1


def reversed_list(lst1, lst2):
    for index in range(len(lst1)):
        if lst1[index] != lst2[len(lst2) - 1 - index]:
            return False
    return True


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
