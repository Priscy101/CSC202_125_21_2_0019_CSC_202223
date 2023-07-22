# Day_9
# learning dictionaries

print("Welcome to secret auction program ")
auct = True
prices = []
high_est = 0
winner = ""
while auct:
    Name = input("What is your name\n").upper()
    Bid_price = int(input("How much are you bidding? $"))
    Bid_dit = {}
    Bid_dit[Name] = Bid_price

    # print(Bid_dit)
    for reis in Bid_dit:
        score = Bid_dit[reis]

        if score > high_est:
            high_est = score
        winner = reis

    peo_ple = input("Are there more bidders? yes or no ").lower()
    if peo_ple != "yes":
        auct = False
        print(f"{winner}, ${high_est} IS THE WINNER")

