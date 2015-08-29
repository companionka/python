# Hotel
def hotel_cost(nights):
    return 140 * nights

# Plane
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        return False

# Rental car        
def rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost

# Pull it Together
def trip_cost(city, days, spending_money):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money

# What if we went to Los Angeles for 5 days and brought an extra 600 dollars of spending money?
#print trip_cost("Los Angeles", 5, 600)

trip_cost = trip_cost("Los Angeles", 5, 600)
print ("%.2f" % trip_cost + "$")