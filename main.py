import pandas as pd

print("---- GENERATING DATA ----")

# Transactions Data
transactions = pd.DataFrame([
    {"id": 1, "amount": 100.00, "date": "2024-01-30"},
    {"id": 2, "amount": 200.00, "date": "2024-01-31"},
    {"id": 3, "amount": 300.50, "date": "2024-01-31"},
    {"id": 4, "amount": 150.00, "date": "2024-01-29"}
])

# Bank Data (with errors)
bank = pd.DataFrame([
    {"id": 1, "amount": 100.00, "date": "2024-02-01"},  # Late settlement
    {"id": 2, "amount": 200.00, "date": "2024-01-31"},
    {"id": 3, "amount": 300.49, "date": "2024-01-31"},  # Rounding issue
    {"id": 2, "amount": 200.00, "date": "2024-01-31"},  # Duplicate
    {"id": 5, "amount": -50.00, "date": "2024-01-31"}   # Refund without original
])

# Convert date format
transactions["date"] = pd.to_datetime(transactions["date"])
bank["date"] = pd.to_datetime(bank["date"])

# Merge data
merged = pd.merge(transactions, bank, on="id", how="outer", suffixes=("_txn", "_bank"))

print("\n---- CHECKING ISSUES ----")

# Missing in bank
print("\nMissing in Bank:")
print(merged[merged["amount_bank"].isna()])

# Missing in transactions
print("\nMissing in Transactions:")
print(merged[merged["amount_txn"].isna()])

# Amount mismatch
print("\nAmount Mismatch:")
print(merged[
    (merged["amount_txn"].notna()) &
    (merged["amount_bank"].notna()) &
    (abs(merged["amount_txn"] - merged["amount_bank"]).round(2) >= 0.01)
])

# Late settlements
print("\nLate Settlements:")
print(merged[
    (merged["date_bank"] > merged["date_txn"])
])

# Duplicates
print("\nDuplicate Entries:")
print(bank[bank.duplicated(subset=["id"], keep=False)])

# Refund issues
print("\nRefund Without Original:")
refunds = bank[bank["amount"] < 0]
print(refunds[~refunds["id"].isin(transactions["id"])])