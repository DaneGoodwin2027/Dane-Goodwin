band=input("What is the band that you're going to go see?\n>")
num_people=float(input("Number of people going?\n>"))
ticket_price=float(input("How much does each ticket cost?\n>"))
total_cost=(num_people*ticket_price)
def show_cost(band, num_people, ticket_price):
    print("The total cost to go see " + band + " with " + num_people + " different people at rate of " + ticket_price + " dollars per ticket would cost a total of " + total_cost)
show_cost(band, num_people, ticket_price)