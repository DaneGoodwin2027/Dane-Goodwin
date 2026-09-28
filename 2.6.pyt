your_item=input("What item are you buying? \n")
itme_price=float(input("How much does it cost? \n"))
tax_rate=.06875

def calcute_tax(item, price, rate):
    print(item + " costs $" + str(price) + " before tax and " + str(itme_price * rate) + " after tax.")

calcute_tax(your_item, itme_price, tax_rate)