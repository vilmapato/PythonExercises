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
