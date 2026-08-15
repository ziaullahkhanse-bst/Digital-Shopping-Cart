cart = []           # Creates empty list to store items you buy
total = 0           # Total money spent starts at 0

while True:         # Keeps showing menu forever
    print("\n1. Apple - $1.00")    # Shows menu option 1
    print("2. Banana - $0.50")     # Shows menu option 2
    print("3. Orange - $0.75")     # Shows menu option 3
    print("4. Milk - $3.50")       # Shows menu option 4
    print("5. Bread - $2.00")      # Shows menu option 5
    print("Type 'done' to finish") # Tells user how to exit
    
    choice = input("What would you like? ")  # Asks user for input
    
    if choice == "done":    # If user types "done"
        break               # Exit the loop
    
    if choice == "1":                       # If user wants Apple
        cart.append("Apple")                # Add Apple to cart list
        total = total + 1.00                # Add $1.00 to total
        print("Added Apple!")               # Tell user it's added
        
    elif choice == "2":                     # If user wants Banana
        cart.append("Banana")               # Add Banana to cart list
        total = total + 0.50                # Add $0.50 to total
        print("Added Banana!")              # Tell user it's added
        
    # ... same for 3, 4, 5 ...
    
    else:                                   # If user typed anything else
        print("Invalid choice! Try again.") # Show error message

print("\n===== YOUR RECEIPT =====")    # Print receipt header
for item in cart:                     # For each item in cart list
    print(item)                       # Print the item name
print("Total: $", total)              # Print the total