import random
# random.seed(56)
data_old = [736, 77, 838, 155, 139, 268, 147, 88, 206, 609, 850, 444, 625, 69, 243, 997, 671, 81, 387, 212, 189, 479, 359, 237, 129, 990, 894, 437, 565, 719, 507, 658, 621, 510, 685, 926, 130, 791, 716, 60, 937, 428, 771, 597, 457, 485, 215, 536, 68, 830, 620, 563, 769, 437, 876, 980, 106, 361, 791, 130, 112, 442, 772, 4, 734, 550, 689, 759, 838, 286, 93, 281, 75, 898, 556, 218, 541, 915, 406, 458, 142, 665, 641, 951, 753, 726, 846, 261, 166, 548, 18, 208, 13, 551, 284, 356, 284, 848, 670, 764]

data = [random.randint(0, 1000) for x in range(100)]

# with open("data.txt", "w+") as file:
#     file.write(str(data))


with open("data.txt", "r") as f:
    our_data = f.read()

our_data = our_data.strip("[]")
our_data = our_data.split(", ")
our_data = list(map(lambda x: int(x), our_data))

print(our_data)
