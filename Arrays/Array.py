# import array
# import array as arr
# from array import *
# ya 3 type hay array import karne ke liye is ma last wala best hai kyun ke is ma kuch name nahi lana parta aur direct array use kar sakte hain



# val = array.array('i', [1, 2, 3, 4, 5])
# print(val)

# val = array.array('i', [1, 2, 3, 4, 5])
# for i in range(0, 5):
#     print(val[i])    # 'i' is ma just integer values hi array ma store karsakty hay

# val = array.array('i', [1, 2, 3, 4, 5])
# for i in range(0, 5):
    # print(val[i], end=' ')

# val = array.array('i', [1, 2, 3, 4, 5])
# for i in val:
#    print(i, end=' ')

# val = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# for i in range(0, len(val)):
#     print(val[i], end=' ')

# val = array.array('d', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10.3]) 
# for i in range(0, len(val)):
#     print(val[i], end=' ')  # 'd' is ma just float values hi array ma store karsakty hay

# val = array('u', ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
# for i in range(0, len(val)):
#     print(val[i], end=' ')
# print(val.typecode)  # 'u' is ma just unicode characters hi array ma store karsakty hay

# val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# for i in range(0, len(val)):
#     print(val[i], end=' ')



            # reverse array
# val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# val.reverse()
# for i in range(0, len(val)):
#     print(val[i], end=' ')


            #  insert value in array
# val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# val.insert(5, 11)                                    # insert 11 at index 5
# for i in range(0, len(val)):
#     print(val[i], end=' ')


            #  append value in array
# val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# val.append(11)                                    # append 11 at the end of array
# for i in range(0, len(val)):
#     print(val[i], end=' ')


            # replace value in array
# val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# val[3] = 85                                    # replace value at index 3 with 85
# for i in range(0, len(val)):
#     print(val[i], end=' ')


            # checking value witout loop
# val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# val.reverse()
# print(val)


            # Delete value from array
# val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# val.pop(5)                                    # delete value at index 5
# print(val)


            # Remove value from array
# val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# val.remove(3)                                    # remove value 3 from array
# print(val)


            #  copy array
# val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# copyArray = array(val.typecode, (x for x in val))  # copy array using list comprehension

# for i in range(0, len(val)):
#     print(copyArray[i], end=' ')


            # slice array
# val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# abc = val[2:5]                            # slice array from index 2 to 4
# print(abc)

# val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# abc = val[2: -3]                 # is ma -3 ka matlab hai ke array ke end se 3 value ko ignore karna hai
# print(abc)


# val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# abc = val[:: -1]                 # is ma -1 ka matlab hai ke array ko reverse karna hai
# print(abc)