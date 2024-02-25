import art

print(art.logo)
print("Welcome to the Silent Auction!")

auctionStatus = ''
biddersList = []
personBid = {}
highestBid = 0.0

while auctionStatus != 'no':
    name = input("Enter your name: ")
    bid = float(input("Enter your bid: $"))
    personBid = {name: bid}
    biddersList.append(personBid)
    auctionStatus = input("Is there another bidder: Yes or No? ").lower()

for bidder in biddersList:
    for name in bidder:
        currentBid = bidder[name]
        if currentBid > highestBid:
            highestBid = currentBid
            winner = name
    
print(art.logo)    
print(f"The winner is {name} with a bid of ${highestBid}")