my_list = [1, 2, 3, 4, 5]
user_choice = input("გინდა სიის გასუფთავება? (y/n): ")
if user_choice == 'y':
    my_list.clear()
    print("სია გასუფთავდა.")
else:
    print("სია დარჩა უცვლელი:", my_list)
