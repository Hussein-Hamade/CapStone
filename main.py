"""Personal Finance Tracker — CLI."""
import argparse


def add_expense(amount: float, category: str) -> str:
    """Return a formatted record of an expense."""
    if amount <= 0:
        raise ValueError("Amount must be positive")
    return f"Added: ${amount:.2f} to {category}"

def remove_expense(amount: float, category: str) -> str:
    if amount <= 0:
        raise ValueError("Amount must be positive")
    return f"Remove ${amount:.2f} from {category}"

def main() -> None:
    parser = argparse.ArgumentParser(description="Track personal expenses.")
    parser.add_argument("amount", type=float, required=True, help="Amount spent")
    parser.add_argument("category", required=True, help="Category e.g. food, rent")
    parser.add_argument("action", choices=["add", "remove"], type=str, help="can be add or remove expense")
    args = parser.parse_args()
    if args.action == "add":
        print(add_expense(args.amount, args.category))
    elif args.action == "remove":
        print(remove_expense(args.amount, args.category))


if __name__ == "__main__":
    main()