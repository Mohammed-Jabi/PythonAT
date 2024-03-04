#Continue
#Continue is used to skip the current block, and return to the "for" or "while" statement.

for num in range(1,10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")
