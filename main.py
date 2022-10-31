daily_sales_replaced = daily_sales.replace(";,;", "+")
daily_transactions = daily_sales_replaced.split(",")

daily_transactions_split = []
for i in daily_transactions:
  daily_transactions_split.append(i.split("+"))

transactions_clean = []
for trans in daily_transactions_split:
  transaction_clean = []
  for data in trans: 
    transaction_clean.append(data.replace("\n"," ").strip(" "))
    transactions_clean.append(transaction_clean)

customers = []
sales = []
thread_sold = []

for transa in transactions_clean:
  customers.append(transa[0])
  sales.append(transa[1])
  thread_sold.append(transa[2])

total_sales = 0
for sale in sales:
  total_sales += float(sale.strip("$"))

thread_sold_split = []
for sale in thread_sold:
  for color in sale.split("&"):
    thread_sold_split.append(color)

def color_count(color):
  color_total = 0
  for thred_color in thread_sold_split:
    if color == thred_color:
      color_total += 1
  return color_total
print(color_count("white"))

colors = ['red','yellow','green','white','black','blue','purple']

for color in colors:
  print("Thread Shed sold {0} threads of {1} threads today.".format(color_count(color),color))
