"""Task 2: Calculate the value of a stock portfolio using sample prices."""
import csv
from pathlib import Path

# Sample prices for this beginner exercise; these are not live market prices.
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "MSFT": 420.00,
    "GOOGL": 165.00,
}


def main():
    print("=== Stock Portfolio Tracker ===")
    print("Available symbols:", ", ".join(STOCK_PRICES))
    holdings = []

    while True:
        symbol = input("Enter stock symbol (or DONE to finish): ").strip().upper()
        if symbol == "DONE":
            break
        if symbol not in STOCK_PRICES:
            print("Unknown symbol. Choose one from the available list.")
            continue
        try:
            quantity = int(input(f"Quantity of {symbol}: "))
            if quantity <= 0:
                print("Quantity must be a positive whole number.")
                continue
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        price = STOCK_PRICES[symbol]
        holdings.append({
            "symbol": symbol,
            "quantity": quantity,
            "price": price,
            "value": quantity * price,
        })

    if not holdings:
        print("No holdings entered. Nothing to calculate.")
        return

    print("\nPortfolio Summary")
    print(f"{'Symbol':<10}{'Quantity':>10}{'Price':>12}{'Value':>14}")
    print("-" * 46)
    total = 0.0
    for item in holdings:
        print(f"{item['symbol']:<10}{item['quantity']:>10}{item['price']:>12.2f}{item['value']:>14.2f}")
        total += item["value"]
    print("-" * 46)
    print(f"{'Total investment value:':<32}{total:>14.2f}")

    save = input("Save results to portfolio.csv? (y/n): ").strip().lower()
    if save == "y":
        output = Path("portfolio.csv")
        with output.open("w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["symbol", "quantity", "price", "value"])
            writer.writeheader()
            writer.writerows(holdings)
            csvfile.write(f"\nTotal investment value,{total:.2f},,\n")
        print(f"Saved portfolio to {output.resolve()}")


if __name__ == "__main__":
    main()
