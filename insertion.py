# # Change the function so it sorts words in alphabetical order. It should ignore capital letters (so "apple" and "Apple" are treated the same).
# Part 4: sort strings
fruits = ["banana", "Apple", "cherry", "date"]

def insertion_sort_words(fruits):
    n = len(fruits)
    for i in range(1, n):
        key = fruits[i]
        j = i - 1
        i = 1
        j = 0
        while j >= 0 and key.lower() < fruits[j].lower():
            fruits[j + 1] = fruits[j]
            j -= 1
            fruits[j + 1] = key

    return fruits

print(insertion_sort_words(fruits))

# Part 5: sort backwards

pallette = [5,1,4,2,8]
def insertion_sort_biggest_first(pallette):
    num = len(pallette)
    for i in range(1, num):
        key = pallette[i]
        f = i - 1
        while f >= 0 and key > pallette[f]:
            pallette[f + 1] = pallette[f]
            f -= 1
            pallette[f + 1] = key

    return pallette
print(insertion_sort_biggest_first(pallette))