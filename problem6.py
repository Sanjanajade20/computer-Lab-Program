food_item = ("Pizza", 100)
food_list = list(food_item)
food_list[1] = 120
modified_food_item = tuple(food_list)
print(modified_food_item)