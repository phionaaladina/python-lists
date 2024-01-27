
numbers_even = [2, 4, 6, 8, 10] #list of even numbers

numbers_odd = [1, 3, 5, 7, 9] #list of even numbers

fruits = ['apples', 'bananas', 'berries', 'cucumber']  #list of fruits

#indexing
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

#slicing
print(fruits[1:3]) #prints from position 1 up to 3 excluding item at index 3

#Modifying
fruits.append('water melon')  #adds item to the end of the list
fruits.insert(1, 'kiwi')  #adds item to index position 1 of the list
fruits.remove('apples')  #removes apple from the list
fruits.pop()  #removes the last item from the list
fruits.pop(0)  #removes item at index 0
del fruits[1]  #deletes item at index 1


#change value of string

fruits[0] = 'strawberry'
fruits[1] = 'pineapples'



print(fruits)