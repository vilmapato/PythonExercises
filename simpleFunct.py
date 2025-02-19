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
