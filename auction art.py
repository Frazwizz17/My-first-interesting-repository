logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


def find_highest_bid(bidder_dict):
    winner_name=""
    highest_bid=0
    for bidder in bidder_dict:
        bid_amount=bidder_dict[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner_name=bidder
    print(f"The winner is {winner_name} with a highest bid price of {highest_bid}")