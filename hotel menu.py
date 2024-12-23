menu={'pizza':40,
      'pasta':50,
      'burger':60,
      'coffee':80,
      'salad':70,}
print(menu)
print("pizza:40\n pasta:50\n burger:60\n salad:70\n coffee:80")
order_total=0
#80+70=150

item_1=input("enter the name of item you want to order")
if item_1 in menu:
    order_total += menu[item_1]    #0+50=50
    print(f"your item{item_1}has been added to your order")

else:
    print(f"ordered item{item_1}is not available yet!")

another_ordered= input("do you want to add another item ?(yes/no)")

if another_ordered== "yes":
    item_2= input("enter the name of second item=")

    if item_2 in menu:
        order_total+= menu [item_2]
        print(f"item{item_2}has been added to orderd")

    else:
        print(f"orderd item{item_2}is not available!")
        print(f"the total amount of item to pay is {order_total}")
