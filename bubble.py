def bubblesort(list):
#each pair of adjacent elements is compared and the elements are swapped if they are not in order.
#
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            # compare an element with the element next to it
            if list[idx]>list[idx+1]:
                # if the element on the left is greater than the one on the right
                # store the left element in a temporary variable
                temp = list[idx]
                # swap its value with that on the right
                list[idx] = list[idx+1]
                # now store the left side element where the right element was initially
                list[idx+1] = temp


list = [int(x) for x in input().split()]
bubblesort(list)
print(list)