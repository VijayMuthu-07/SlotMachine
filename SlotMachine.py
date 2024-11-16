import random 

def spin_row():
    symbols = ["🍒","🍋","⭐","🍉","🔔"]
    return [random.choice(symbols) for i in range(3)]

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        match row[0]:
            case "⭐":
                return bet * 25
            case "🍒":
                return bet * 10
            case "🍉":
                return bet * 10
            case "🔔":
                return bet * 5
            case "🍋":
                return bet * 2
    return 0

def main():
    balance = 1000
    print("*************************")
    print("Welcome to Slot Machine")
    print("symbols: 🍒 🍋 ⭐ 🍉 🔔")
    print("*************************")

    while balance > 0:
        print(f"Your current balance is {balance}.Rs")
        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid amount")
            continue
        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than zero")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You Won {payout}.Rs")
        else:
            print("Sorry you lost this round")

        balance += payout

        play_again=input("Do you want to spin again? (Y/N): ").upper()
        if play_again != "Y":
            break

    print("***********************************************")
    print(f"Game over! Your final balance is {balance}.Rs")
    print("***********************************************")

if __name__ == '__main__':
    main()