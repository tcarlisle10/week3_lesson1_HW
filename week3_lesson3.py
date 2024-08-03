# Question 1

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

intersect = our_routes.intersection(competitor_routes)
print(intersect)

difference = our_routes.difference(competitor_routes)
print(difference)

sym_diff = our_routes.symmetric_difference(competitor_routes)
print(sym_diff)



#--------------------------------------------------------------------#
# Question 2 


customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

def no_duplicate(a_list):
    a_list = tuple(a_list)
    a_list = set(a_list)
    print(a_list)
    

no_duplicate(customer_ids)




