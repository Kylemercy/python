def final_amount(p,n,r,t):
  a = p*(1 + r//n)**(n*t)
  return a
num = float(input("Enter the amount you want to invest: "))
total = final_amount(num,0.07,9,5)
total = round(total,2)
print(f"At the end of the given time,you will have  ${total}")