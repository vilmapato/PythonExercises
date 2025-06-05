def Count_Sheep(array):
    # your code here
    if not array:
        return 0
    elif len(array) == 0:
        return 0
    else:
        count = 0
        for sheep in array:
            if sheep:
                count += 1
        return count


print(Count_Sheep([True, True, False, True, False, True, True, True, False, False]))


def find_needle(haystack):
    # your code here
    index = 0
    for needle in haystack:
        if needle == "needle":
            return f"found the needle at position {index}"
        else:
            index += 1
            continue

    return "needle not found"


print(find_needle(["hay", "hay", "hay", "hay", "needle", "hay", "hay"]))
