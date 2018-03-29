def cheese_and_crackers(cheeseCount, boxesOfCrackers):
  print(f"You have {cheeseCount} cheeses!")
  print(f"You have {boxesOfCrackers} boxes of crackers!")
  print("Man that's enough for a party!")
  print("Get a blanket.\n")
  
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)
  
print("OR, we can use variables from our script:")
amountOfCheese = 10
amountOfCrakers = 50

cheese_and_crackers(amountOfCheese, amountOfCrakers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amountOfCheese + 100, amountOfCrakers + 1000)