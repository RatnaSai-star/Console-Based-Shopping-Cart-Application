cart=[]
print("Welcome to the Shopping Cart :) ")
print("Commands :- ")
print("- Type 'add' to add items to the cart")
print("- Type 'remove' to remove items from the cart")
print("- Type 'view' to see your cart")
print("- Type 'sum' to total ")
while True:
    task=input("Enter your task here :- ")
    if task=="add":
        items=eval(input("Enter the items to be added :- "))
        cart.append(items)
        print(f"The items is added {cart}")
        next=int(input("Enter one to do other opertion two to stop :- "))
        if next==1:
            continue
        else:
            break
    elif task=="remove":
        item=(input("Enter the items to be removed :- "))
        print(cart)
        if item in cart:
            print(f"'{item}' has been removed. Current cart: {cart}")
        else:
            print(f"'{item}' not found in cart. Nothing removed.")
        print(f"The items after removal {cart}")
        next=int(input("Enter one to do other opertion two to stop :- "))
        if next==1:
            continue
        else:
            break
    elif task=="view":
        print(f"The items are in {cart}")
        next=int(input("Enter one to do other opertion two to stop :- "))
        if next==1:
            continue
        else:
            break
    elif task=="sum":
        sum=0
        for i in items:
            no=int(input("Enter the cost :- "))
            sum=sum+no
        print(sum)
        next=int(input("Enter one to do other opertion two to stop :- "))
        if next==1:
            continue
        else:
            break
    else:
        print("Undefind oparation :( ")
        next=int(input("Enter one to do other opertion two to stop :- "))
        if next==1:
            continue
        else:
            break
print("Thank U shop again ")