# Modify the the list = 64, 34, 25, 12, 22, 11, 90 in Python bubble_sort function to sort the list in descending order instead of ascending.


said = [64, 34, 25, 12, 22, 11, 90]
def bubble_sort_desc(said):
    n = len(said)
    for i in range(n):
        for j in range(0, n - i - 1):
            if said[j] < said[j + 1]:
                said[j], said[j + 1] = said[j + 1], said[j]


    return said

        
print(bubble_sort_desc(said))
    
