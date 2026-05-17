"""Personal Finance Tracker — CLI."""
import argparse


def add_expense(amount: float, category: str) -> str:
    """Return a formatted record of an expense."""
    if amount <= 0:
        raise ValueError("Amount must be positive")
    return f"Added: ${amount:.2f} to {category}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Track personal expenses.")
    parser.add_argument("amount", type=float, help="Amount spent")
    parser.add_argument("category", help="Category e.g. food, rent")
    args = parser.parse_args()
    print(add_expense(args.amount, args.category))


if __name__ == "__main__":
    main()