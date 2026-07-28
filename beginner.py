# # # # # # # #variable declaration
# # # # # # # # name = "saheed ibraheem"
# # # # # # # # age = 30
# # # # # # # # Gender = "male"
# # # # # # # # print("my name is", name, "and i am", age, "years old", "i am a", Gender)

# # # # # # # Data_types = "string", 10, 10.5, True, False, None

# # # # Hello = "Hello world"
# # # # hello = 'hello world'

# # # # Multi_strings = """ lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. """
# # # # print(Multi_strings)

# # # #looping through a string
# # # for rex in "father":
# # #     print( rex)

# # s = '1,2,3,4,5,6.7.8.9.10.' * 3
# # # print(s)
# # s[::5]
# # print(s[::5])

# S = "Saheed Ibraheem"
# S in "Saheed Ibraheem"

# # print (S in "Saheed Ibraheem")

# S not in "this is not Alabi"

# print(S not in "Alabi" )


# arr = [4,2,6,9,8,3]
# def in_sort(arr):
#     num = len(arr)
#     for i in range(1, num):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key

#     return arr
# print(in_sort(arr))

pallette = [9,5,7,85,4,34,56,5,64,1,2,3,6]
def in_sort(Num):
    Num = len(pallette)
    for i in range(1, Num):
        key = pallette[i]
        f = i - 1
        while f >= 0 and key < pallette[f]:
            pallette[f + 1] = pallette[f]
            f -= 1
            pallette[f + 1] = key

    return pallette
print(in_sort(pallette))
