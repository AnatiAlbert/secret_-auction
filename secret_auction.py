# Secret Auction
#from replit import clear

from art_auction import logo
print(logo)

bids = {}   #empty dictionary
bidding_finished = False  #set bidding finished to false

def find_highest_bidder(bidding_record):  # find_highest_bidder function with bidding_record as parameter
    highest_bid = 0 #set highest bid to zero
    winner = '' #set winner

    for bidder in bidding_record: #for loop in bidding_record
        bid_amount = bidding_record[bidder] # set bid amount as key in bidding record
        if bid_amount > highest_bid: # check whether bid is highest
            highest_bid = bid_amount
            winner = bidder
    print(f'The winner is {winner} with a bid of ${highest_bid}')

while not bidding_finished: # repeat name and price inputs
    name = input('What is your name?: ')
    price = int(input('What is your bid?: $'))
    bids[name] = price
    should_continue = input('Are there any other bidders? Type "yes" or "no".\n')
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    #elif should_continue == "yes":

