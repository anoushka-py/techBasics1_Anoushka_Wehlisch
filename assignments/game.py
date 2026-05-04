import time
import random

# ── Opening ───────────────────────────────────────────────────────────────────
print("=" * 45)
print("      ⚡  Quick Maths – Beat the Clock!  ⚡")
print("=" * 45)
time.sleep(1)

name = input("\nEnter your name: ")                   # User input 1
print(f"\nWelcome, {name}! You have 10 seconds to answer.")
time.sleep(1)

# ── Generate random equation ──────────────────────────────────────────────────
a = random.randint(0, 100)
b = random.randint(0, 100)
op = random.choice(["+", "-", "*", "/"])

if op == "+":
    correct = a + b
elif op == "-":
    correct = a - b
elif op == "*":
    correct = a * b
else:
    b = random.randint(1, 10)
    a = b * random.randint(1, 10)
    correct = a // b

print(f"\n   What is  {a} {op} {b} ?")
print("   (Round to the nearest whole number if needed)\n")

start = time.time()
answer = int(input("   Your answer: "))               # User input 2
elapsed = time.time() - start

print()
if elapsed > 10:                                      # Conditional 1
    print(f"⏰  Too slow! The answer was {correct}.")
else:
    if answer == correct:                             # Conditional 2
        if elapsed < 4:                               # Conditional 3
            print(f"⚡  LIGHTNING fast! ({elapsed:.1f}s)  Correct!")
        else:
            print(f"✅  Correct!  ({elapsed:.1f}s)  Nice work!")
    else:
        print(f"❌  Wrong. The answer was {correct}.")

time.sleep(0.8)
again = input("\nPlay again? (yes / no): ")           # User input 3

if again.lower() == "yes":                            # Conditional 4
    print("\nRefreshing...\n")
    time.sleep(1)
    import os, sys
    os.execv(sys.executable, [sys.executable] + sys.argv)
else:                                                 # Conditional 5
    print(f"\nThanks for playing, {name}! See you next time. 👋")


