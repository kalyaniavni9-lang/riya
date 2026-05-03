# items = {

# "cakes ": 300,
# "pastries" : 100,
# "chocolates" : 20,
# "cookies" : 80,
# "toast ": 150,
# "khari" : 100,
# "icecreams" : 170

# }
 
# total = 0


# while True:
#     print("\nMenu") 
# #menu print
#     i = 1
#     item_list = list(items.key())
#     for item in item_list:
#       print(i , ".", "₹", items[item])
#     i +=1
       







#     choice = int(input("enter item number: "))     
#     item_list = list(item.keys())
#     selected_item = item_list[choice-1]
    

#     quantity = int(input("enter quantity: "))

#     price = items[selected_item]*quantity
#     total += price
    
#     print(f"Added{selected_item}*{quantity} = {price}")

#     more = input("do you want more items? (yes/no):")
#     break 
# print("\nFinal bill")
# print("total amount =  Rs.", total)
# print("thank you! visit again ")









items = {
    "cakes": 300,
    "pastries": 100,
    "chocolates": 20,
    "cookies": 80,
    "toast": 150,
    "khari": 100,
    "icecreams": 170
}

total = 0

print(" Welcome to my Bakery ")

while True:
    print("\nMenu:")
    
    # menu print
    i = 1
    item_list = list(items.keys())
    for item in item_list:
        print(i, ".", item, ":", "₹", items[item])
        i += 1

    # user input
    choice = int(input("\nEnter item number: "))
    
    if choice < 1 or choice > len(item_list):
        print(" Invalid choice")
        continue

    selected_item = item_list[choice - 1]
    price = items[selected_item]

    print("✅ You selected:", selected_item, "₹", price)

    total += price

    more = input("Do you want more items? (yes/no): ").lower()

    if more != "yes":
        break

# final bill
print("\n🧾 Final Bill")
print("Total amount = ₹", total)
print("🙏 Thank you! Visit again ")

#PIE CHART
items_names = list(sales_data.keys())
sales_values = list(sales_data.valu())

plt.pie(sales_values, labels=items_names,
autopct = '%1. 1f%%')
plt.title("bakery sales distribution")

plt.show()