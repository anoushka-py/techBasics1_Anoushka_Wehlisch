import time
import random
import csv
import os
from datetime import datetime


DEBUG = False

#
RECORDS_FILE = "maths_records.csv"  # File where records are saved
PLACEHOLDER_TIME = 99.9


def load_records():

    records = []

    try:

        with open(RECORDS_FILE, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                records.append(row)
        print(f"(Records loaded from '{RECORDS_FILE}')")

    except FileNotFoundError:

        print("(No existing records found. A new file will be created.)")

    except Exception as e:

        print(f"(Error loading records: {e})")

    return records



def save_records(records):

    try:
        with open(RECORDS_FILE, "w", newline="") as file:

            fieldnames = ["name", "timestamp", "time_seconds", "result"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)


            writer.writeheader()


            for record in records:
                writer.writerow(record)

        print(f"(Record saved to '{RECORDS_FILE}')")

    except Exception as e:
        print(f"(Error saving records: {e})")



def add_record(records, name, elapsed, result):


    new_record = {
        "name": name,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "time_seconds": f"{elapsed:.1f}",
        "result": result
    }


    records.append(new_record)


    records.sort(key=lambda r: (
        0 if r["result"] == "correct" else 1,
        float(r["time_seconds"])
    ))

    return records


def show_leaderboard(records):

    print("\n" + "=" * 50)
    print("           🏆  LEADERBOARD  🏆")
    print("=" * 50)

    if len(records) == 0:
        print("No records yet!")
        return


    print(f"{'#':<4} {'Name':<15} {'Time':<10} {'Result':<12} {'Date'}")
    print("-" * 50)

    for i, record in enumerate(records):
        rank = i + 1


        if rank == 1:
            medal = "🥇"
        elif rank == 2:
            medal = "🥈"
        elif rank == 3:
            medal = "🥉"
        else:
            medal = f"  {rank}."

        print(
            f"{medal:<4} "
            f"{record['name']:<15} "
            f"{record['time_seconds']}s{'':<6} "
            f"{record['result']:<12} "
            f"{record['timestamp']}"
        )

    print("=" * 50)



def play_game(name):

    print(f"\nWelcome, {name}! You have 10 seconds to answer.")
    time.sleep(1)


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

    try:
        answer = int(input("   Your answer: "))
    except ValueError:
        print("That's not a number! Counting as wrong.")
        answer = None

    elapsed = time.time() - start
    print()


    if elapsed > 10:
        print(f"⏰  Too slow! The answer was {correct}.")
        result = "too slow"

    elif answer == correct:
        if elapsed < 4:
            print(f"⚡  LIGHTNING fast! ({elapsed:.1f}s)  Correct!")
        else:
            print(f"✅  Correct!  ({elapsed:.1f}s)  Nice work!")
        result = "correct"

    else:
        print(f"❌  Wrong. The answer was {correct}.")
        result = "wrong"

    return elapsed, result



def main():


    print("=" * 45)
    print("      ⚡  Quick Maths – Beat the Clock!  ⚡")
    print("=" * 45)
    time.sleep(1)

    name = input("\nEnter your name: ")


    if DEBUG:
        print("\n⚠️  DEBUG MODE ON — skipping game.")
        print(f"Saving placeholder score for '{name}'...")

        elapsed = PLACEHOLDER_TIME
        result = "debug"


    else:
        elapsed, result = play_game(name)


    records = load_records()
    records = add_record(records, name, elapsed, result)
    save_records(records)


    show_leaderboard(records)


    time.sleep(0.8)
    again = input("\nPlay again? (yes / no): ")

    if again.lower() == "yes":
        print("\nRefreshing...\n")
        time.sleep(1)
        main()
    else:
        print(f"\nThanks for playing, {name}! See you next time. 👋")



if __name__ == "__main__":
    main()