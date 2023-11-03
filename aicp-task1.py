item_codes = ['A1', 'A2', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3', 'D1', 'D2', 'E1', 'E2', 'E3', 'F1', 'F2', 'G1', 'G2']
descriptions = [
    'Compact Case', 'Tower Case', '8GB RAM', '16GB RAM', '32GB RAM', '1 TB HDD', '2 TB HDD', '4 TB HDD',
    '240 GB SSD', '480 GB SSD', '1 TB HDD', '2 TB HDD', '4 TB HDD', 'DVD/Blu-Ray Player', 'DVD/Blu-Ray Re-writer',
    'Standard OS', 'Professional OS'
]
prices = [75.00, 150.00, 79.99, 149.99, 299.99, 49.99, 89.99, 129.99, 59.99, 119.99, 49.99, 89.99, 129.99, 50.00, 100.00, 100.00, 175.00]

# Initialize variables
chosen_items = []
total_price = 200.00
discount = 0.0

print("Welcome to the Online Computer Shop!")
print("Please choose one case, one RAM, and one Main Hard Disk Drive:")

print("\nCase Options:")
for i in range(2):
    print(f"{item_codes[i]}: {descriptions[i]} - ${prices[i]:.2f}")

case_choice = input("Enter the item code for the case you want: ").upper()
if case_choice not in item_codes[:2]:
    print("Invalid item code for the case.")
else:
    chosen_items.append(descriptions[item_codes.index(case_choice)])
    total_price += prices[item_codes.index(case_choice)]

print("\nRAM Options:")
for i in range(2, 5):
    print(f"{item_codes[i]}: {descriptions[i]} - ${prices[i]:.2f}")

ram_choice = input("Enter the item code for the RAM you want: ").upper()
if ram_choice not in item_codes[2:5]:
    print("Invalid item code for RAM.")
else:
    chosen_items.append(descriptions[item_codes.index(ram_choice)])
    total_price += prices[item_codes.index(ram_choice)]

print("\nMain Hard Disk Drive Options:")
for i in range(5, 8):
    print(f"{item_codes[i]}: {descriptions[i]} - ${prices[i]:.2f}")

hdd_choice = input("Enter the item code for the Main Hard Disk Drive you want: ").upper()
if hdd_choice not in item_codes[5:8]:
    print("Invalid item code for Main Hard Disk Drive.")
else:
    chosen_items.append(descriptions[item_codes.index(hdd_choice)])
    total_price += prices[item_codes.index(hdd_choice)]

choice = input("Do you want to purchase additional items (yes/no)? ").lower()
if choice == 'yes':
    while True:
        print("\nAdditional Item Categories:")
        for i in range(8, len(item_codes)):
            print(f"{item_codes[i]}: {descriptions[i]} - ${prices[i]:.2f}")

        item_choice = input("Enter the item code for the additional item you want (or 'done' to finish): ").upper()
        if item_choice == 'DONE':
            break
        if item_choice not in item_codes[8:]:
            print("Invalid item code for additional item.")
        else:
            chosen_items.append(descriptions[item_codes.index(item_choice)])
            total_price += prices[item_codes.index(item_choice)]

if len(chosen_items) == 1:
    discount = total_price * 0.05
elif len(chosen_items) >= 2:
    discount = total_price * 0.10

print("\nChosen Items:")
for item in chosen_items:
    print(f"- {item}")

print(f"\nTotal Price (before discount): ${total_price:.2f}")
print(f"Discount: ${discount:.2f}")
total_price -= discount
print(f"Total Price (after discount): ${total_price:.2f}")
