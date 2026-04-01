PROJECT: Transaction Reconciliation System

Problem:
Mismatch between platform transactions and bank settlements.

Solution:
Generated sample datasets and implemented comparison logic using pandas.

Features:
- Detect missing transactions
- Identify duplicates
- Find rounding mismatches
- Detect late settlements
- Identify refund inconsistencies

Limitations:
1. Settlement delays beyond expected time may cause incorrect flags
2. Incorrect transaction IDs may affect matching
3. Currency differences are not handled