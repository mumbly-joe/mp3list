greeting = "Hello You"
print(greeting)
print(type(greeting))

my_int = 1
print(f"the integer is {my_int}")
print(f"the type of the integer is {type(my_int)}")

my_float = 1.0
print(f"the float is {my_float}")
print(f"the type of the float is {type(my_float)}")

my_float2 = 0.999999999999
print(f"this is another float: {my_float2}")
print(f"it is still of the samme type {type(my_float2)}")

# this is a very useful data type called a list


print("now we can muck with lists")
# create an empty list
my_list = []

# to add to the list you can do
my_list.append("my_string")
# add something else
my_list.append(10)
# add more stuff
my_list.append(20.234)

# we can print from the list

# print the first position because we start from 0
print(my_list[0])

# print the 3rd position
print(my_list[2])

print("now we will do a for loop")
for my_value in my_list:
    print(my_value)
    if my_value == 10:
        print("the value is 10! ")

def hello(arg1, arg2):
    print(f'hello-cunts {arg1}')
    print(f'from {arg2}')


