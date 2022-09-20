list_1 = [1, 4, 3]
list_2 = [3, 5, 1]


def sum_two_lists(list_1, list_2):
  new_list = zip(list_1, list_2)
  sum_list = [item_1 + item_2 for (item_1, item_2) in new_list]
  
  return sum_list

print(sum_two_lists(list_1, list_2))