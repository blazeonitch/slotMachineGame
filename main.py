import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbolCount = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbolValue = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def checkWinning(cols, lines, bet, values):
    winnings = 0
    winningLines = []
    for line in range(lines):
        symbol = cols[0][line]
        for column in cols:
            symbolToCheck = column[line]
            if symbol != symbolToCheck: break
        else:
            winnings += values[symbol] * bet
            winningLines.append(line + 1)

    return winnings, winningLines

def getSlotMachineSpin(rows:int, cols:int, symbols):
    allSymbols = []
    for symbol, symbolCount in symbols.items():
        for _ in range(symbolCount):
            allSymbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        currentSymbols = allSymbols.copy()
        for row in range(rows):
            value = random.choice(currentSymbols)
            currentSymbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def printSlotMachine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1: print(column[row], end=" | ")
            else: print(column[row], end="")
        print()


def deposit():
    while True:
        try:
            amount = float(input("What would you like to deposit? $"))
            if amount > 0: break
            else: print("Amount must be greater than 0.")
        except ValueError: print("Enter a valid number!")

    return amount

def getNumberOfLines():
    while True:
        try:
            lines = int(input("Enter the number of line to bet on (1-" + str(MAX_LINES) + ")? "))
            if 1 <= lines <= MAX_LINES: break
            else: print("Enter a valid number of lines")
        except ValueError: print("Enter a valid number!")

    return lines

def getBet():
    while True:
        try:
            amount = float(input("What would you like to bet on each line? $"))
            if 1 <= amount <= MAX_BET: break
            else: print(f"Amount must be between {MIN_BET} - {MAX_BET}")
        except ValueError: print("Enter a valid number!")

    return amount

def spin(balance):
    lines = getNumberOfLines()
    while True:
        bet  = getBet()
        totalBet = bet * lines
        if totalBet > balance: print(f"You do not have enough that amount, your current balance is {balance}")
        else: break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${totalBet}")

    slots = getSlotMachineSpin(ROWS, COLS, symbolCount)
    printSlotMachine(slots)
    winnings, winningLines = checkWinning(slots, lines, bet, symbolValue)
    print(f"You won ${winnings}")
    print(f"You won on lines:", *winningLines)
    return winnings - totalBet


def main():
    balance = deposit()
    while 1:
        print(f"Current Balance is ${balance}")
        answer = input("Press Enter to play (q to quit).")
        if answer == "q": break
        balance += spin(balance)

    print(f"You left with ${balance}")

if __name__ == "__main__":
    main()
