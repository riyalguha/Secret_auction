from replit import clear
import art
print(art.logo)
#HINT: You can call clear() to clear the output in the console.
names={}
#Done using Recursion
def Secret_Auc():
  key=input("What is the bidder's name? ")
  names[key]=int(input("Enter your Bid $"))
  while 2>1:
    choice=input("Is there anyone else in the room who wants to bid? Type 'Yes' or 'No'").lower()
    if choice == "yes":
      clear()
      Secret_Auc()
    elif choice == "no":
      clear()
      max=0
      for bid in names:
        if names[bid]>max:
          max=names[bid]
          winner=bid
      print(f"The Winner of the auction is {winner} with the value of the item as {max}")
    break

Secret_Auc()
