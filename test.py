def  simpleintrs (p,n,r):
    i = (p*n*r)/100
    amt = p+ i
    return{"intrest" : i, "amount ": amt}


p = float(input("please select principle in INR : "))
n =int(input())