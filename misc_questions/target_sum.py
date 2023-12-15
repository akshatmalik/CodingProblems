
def recur_helper(array, target_sum, current_sum, index):

    if target_sum == current_sum:
        return True

    if current_sum > target_sum:
        return False

    if index >= len(array):
        return False

    res1 = recur_helper(array, target_sum, current_sum + array[index], index+1)
    res2 = recur_helper(array, target_sum, current_sum, index+1)

    return res1 or res2


def target_sum(array, target_sum):


    return recur_helper(array, target_sum, 0, 0)



if __name__ == "__main__":

    assert target_sum([2,4,7], 8) == False
    assert target_sum([2,4,7], 9) == True
    assert target_sum([2,3,5], 5) == True
    assert target_sum([2,4,5], 3) == False