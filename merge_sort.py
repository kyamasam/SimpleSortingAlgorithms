def merge_sort(A):
    #list, starting index, end index
    merge_sort2(A , 0, len(A)-1)


def merge_sort2(A, first,last):
    #check if the list has more than one item
    if first<last:
        middle=first+last//2
        #call merge sort on the first half of the list
        merge_sort2(A, first, middle)
        #call merge sort on the second half of the list
        merge_sort2(A, middle+1 ,last)

        #merge the 2 sorted lists
        merge(A,first, middle, last)



def merge(A,first, middle, last):
    left=A[first:middle+1]
    right =A[middle+1:last+1]

    #add a very lasrge number at the end of both left and right
    #it will let us know when we reach the end of the list
    left.append(999999999)
    right.append(999999999)
    left_index_counter=right_index_counter=0

    #start filling in the lists from both halves to the main list A

    for main_list_counter in range (first, last+1):
        if(left[left_index_counter]<=right[right_index_counter]):
            #add it to the main list
            A[main_list_counter] = left[left_index_counter]
            left_index_counter += 1
        else:
            A[main_list_counter]=right[right_index_counter]
            #increment the right index counter
            right_index_counter+=1
    print(A)


# list_to_sort=[int(x) for x in input().split()]
A = [5,9,1,2,4,8,6,3,7]
print(A)
merge_sort(A)
print(A)
# print(list_to_sort)