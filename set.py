#set
mixed_set={"hello",101,-2,"bye"}
print("print mixed sets",mixed_set)
#duplicate
numbers={1,2,3,4,5,6,7,7,6,5,1,1}
print(numbers)
#empty
empty_dictionary={}
print("print the empty",empty_dictionary)
#add items
numbers={12,23,45,67}
print(numbers)
numbers.add(49)
print("added set",numbers)
#update python set
companies={"lacoste","ralph","vibro"}
remove=companies.discard("vibro")
print(companies)
#for loop
animals={"cat","dog","elephant"}
for x in animals:
    print(x)
#find numbers
num={1,2,3,4}
print("the set is",num)
print("total elements",len(num))
#set operation
A={1,2,3,4}
B={4,5,6,7}
print("union using union():",A.union(B))
#set intersection
A={1,2,3,4}
B={2,3,4,5}
print("intersection using intersection():",A.intersection(B))
print("difference using&:",A-B)
print("using^:",A^B)
print("using symmetric_difference():",A.symmetric_difference(B))
A={1,2,3}
B={2,3,4}
if A==B:
    print("set A and set B are equal")
else:
    print("set A and set B are not equal")




# Create a set of integer type
student_id={112,114,116,118,115}
print("student_id:",student_id)


# create a set of string type
vowel_letters={"a","e","i","o","u"}
print("vowel_letters:",vowel_letters)


# Create a set of mixed data types
mixed_set={"hello",101,-2,"bye"}
print("print mixed sets",mixed_set)


# Create an empty set
empty_set=set()
# create an empty dictionary
empty_dictionary={}
# check data type of empty_set
print("Data type of empty_set:",type(empty_set))
# check data type of dictionary_set
print("data type of empty_dictionary",type(empty_dictionary))


# Duplicate items in a set
numbers={1,2,3,4,5,6,7,7,6,5,1,1}
print(numbers)


# Add items to a set in python
numbers={21,34,54,12}
print("Initial set:",numbers)
# using add()method
numbers.add(32)
print("updated set:",numbers)


#update python set
companies={"lacoste","ralph","vibro"}
tech_companies=["apple","google","apple"]
companies.update(tech_companies)
print(companies)

# remove an element from a set
languages={"swift","java","python"}
print("Initial set:",languages)
# remove "java from a set"
removevalue=languages.discard("java")
print("set ofter remove():",languages)
# Iterate over a set in python
fruits={"apple","pench","mango"}
# for loop to acces each fruits
for fruit in fruits:
    print(fruit)
animals={"cat","dog","elephant"}
for x in animals:
    print(x)

#find numbers
num={1,2,3,4}
print("the set is",num)
print("total elements",len(num))

#set operation
A={1,2,3,4}
B={4,5,6,7}
print("union using union():",A.union(B))

#set intersection
A={1,2,3,4}
B={2,3,4,5}
print("intersection using intersection():",A.intersection(B))
print("difference using&:",A-B)
print("using^:",A^B)
print("using symmetric_difference():",A.symmetric_difference(B))

#using difference
A={1,2,3}
B={1,2,6}
print("Difference using &:",A-B)
print("Difference using difference():",(B)) 

#using symmetric difference
A={1,2,3}
B={1,2,6}
print("using ^:",A^B)
print("using symmetric_difference():",A.symmetric_difference(B))

#difference using if else
A={1,2,3}
B={2,3,4}
if A==B:
    print("set A and set B are equal")
else:
    print("set A and set B are not equal")



