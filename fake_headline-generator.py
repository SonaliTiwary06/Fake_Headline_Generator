#import random module
import random

#create subjects
subject=["Sharukh khan", "Virat kohli", "Nirmala sitharaman", "A Mumbai cat",
          "Group of monkeys", "Prime Minister", "Auto Ricksaw driver from Delhi"]

actions=["launches", "cancels", "dances with", "eats", "declares war on", "orders", "celebrates"]

place_or_things=["at Red Fort", "in Mumbai local train", "a plate of samosa", "inside parliament",
                  "at Ganga ghat", "during IPL match", "at India gate"]

#start the headline generation loop
while True:
    sub=random.choice(subject)
    act=random.choice(actions)
    plc_thng=random.choice(place_or_things)

    headline=f" BREAKING NEWS : {sub} {act} {plc_thng}"
    print("\n" + headline)

    user_input=input("\nDo you want another headline? (yes/no)").strip().lower()
    if user_input=="no":
        break

#print goodbye msg
print("\nThanks for using the Fake News Headline Generator. Have a fun day")
    