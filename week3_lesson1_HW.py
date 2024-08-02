# Question 1 

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}


restaurant_menu["Beverages"] = {"Dr. Pepper" : 2.00, "Sweet Tea" : 1.50}
restaurant_menu["Main Course"].update({"Steak": 17.99})
restaurant_menu["Starters"].pop("Bruschetta")

print(restaurant_menu)

#-------------------------------------------------------------------#

# Question 2


service_tickets = {
    1: {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    2: {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def next_id():
    last_id = 0
    for id in service_tickets.keys():
        if id > last_id:
            last_id = id
    return last_id + 1

print(next_id())

def new_ticket():
    new_id = next_id()
    while True:
        customer = input("Please enter your name: \n")
        issue = input("Please state the issue: \n")
        print(f"Customer: {customer}, Issue: {issue}")
        correct = input("Is this informative correct? (y/n)")
        if correct == 'y':
            service_tickets[new_id] = {'Customer': customer, "Issue": issue, 'Status': 'open'}
            break
        else:
            continue

def update():
    update_input = input("Has your issue been solved? (y/n)")

    if update_input == 'y':
        selection()
    elif update_input == 'n':
        main()


def selection():
    
    print(service_tickets)
    select = int(input("What number customer are you? "))
    if select in service_tickets:
        current_status = service_tickets[select]['Status']
        if current_status == 'open':
            service_tickets[select]['Status'] = 'closed'   
        print(service_tickets)
    



def main():
    while True:
        ans = input('''
SERVICE TICKET MANAGER
Enter the corresponding number for the action you'd like to take:
    1 - Open a new service ticket.
    2 - Update a service ticket.
    3 - Display all service tickets.
    4 - Quit                    
''')
        
        if ans == '1':
            new_ticket()
        elif ans == '2':
            update() 
        elif ans == '3':
            print(service_tickets)
        elif ans == '4':
            print("Thank you, Have a great day")
            break
        else:
            print("Enter number again")



main()