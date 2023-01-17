# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

print("say one")

print("say two")

print("say three")

a = 10

b = 12.5

c = "data in some additional value"

d = True
#  list() []
value = ['data', 'in', 'some', 'additional', 'value', 11, a, c, [1, 2, 3, 4, 5]]

# tuple ()

value_permanent = ('data', 'in', 'some', 'additional', 'value', 11, a, c, [1, 2, 3, 4, 5])

# print(value_permanent)
#
# value_permanent[-1].append(123457)
#
# print(value_permanent)


new_list = [1,4,6,3,2,56,7,5,67,88,3,56,7,88,23,45,77,88,66,22,33]

new_list.sort()

var_set = set(new_list)

# print(new_list)
# print(var_set)

var_set.add("345")
var_set.add("345")
# print(var_set)

var_dict = {"float": 12.3,  (1,2,3): 345, "list": [1,2], "set": {1,2}}

print(var_dict["float"])

var_dict["bool"] = True

print(var_dict)





# loop

data = ["123", 123, [1, 2, 3], "some additional info", "expected", (11, 21, 31),
        {12, 22, 32}, "expected", "123", 123, [1, 2, 3], "some additional info",
        (11, 21, 31), {12, 22, 32},  "123", 123, [1, 2, 3], "some additional info",
        (11, 21, 31), {12, 22, 32}]
data_values = data


for iterator, something in enumerate(data_values):

    print(f"iteration {iterator+1}")

    if something == "123":
        print("not expected")
        continue

    if something == "expected":
        print(f"{something=}  found \n")
        print(data.index("expected"))
        break
else:
    print("nothing found")

print("finished")
