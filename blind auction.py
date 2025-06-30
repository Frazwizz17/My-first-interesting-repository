# TODO-1: Ask the user for input
from art import logo
print(logo)


Auction_list={}
continue_bidding=True
while continue_bidding:
    bidder_name = input("What is your name?: ")
    bid_price = int(input("What's your bid?: $"))
    Auction_list[bidder_name] = bid_price
    any_other_bidder = input("Are there any other bidders? Type 'yes or 'no'\n")
    if any_other_bidder=="no":
        continue_bidding=False
        winner_name=max(Auction_list,key=Auction_list.get)
        print(f"The winner of this auction is {winner_name} with a highest bid price of ${Auction_list[winner_name]}")

    elif any_other_bidder=="yes":
        print("\n"*100)


# TODO-4: Compare bids in dictionary






