import os
import csv
from datetime import datetime
from collections import defaultdict

class Expenes:
    def __init__(self, amount, catgory,description):
        self.amount = float(amount)
        self.category = catgory
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d")
    def to_list(self):
        return([self.date, self.amount, self.category, self.description])
class ExpenesTracker:
    FILE_NAME = "expenses.csv"
    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Amount", "Category", "Description"])
    def add_expenses(self,expense):
        with open(self.FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(expense.to_list())
            print(" Added Successfully")
    def view_expenses(self):
        with open(self.FILE_NAME, "r", ) as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    def monthly_summary(self):
        summary = defaultdict(float)
        with open(self.FILE_NAME, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                month = row["Date"][:7]
                summary[month] += float(row["Amount"])
            print("Monthly Summmary")
            for month, total in summary.items():
                print(f"{month} {total}")
    
    def category_analysis(self):
        category = defaultdict(float)
        with open(self.FILE_NAME, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                category[row["Category"]] += float(row["Amount"])
            print("CAtegory wise Record")
            for category, total in category.items():
                print(f"{category} {total}")
def main():
    tracker = ExpenesTracker()
    while True:
        print("\n---Expanse Tracker---")
        print("1.  Add ")
        print("2.  View ")
        print("3.  Monthly Summary")
        print("4.  Category Analysis")
        print("5.  Exit")
        choice = input("Enter Your Choice").strip()
        if choice == "1":
            try:
                amount = input("enter your amount:")
                category = input("enter your category")
                description = input("enter your description")
                expenses = Expenes(amount,category,description)
                tracker.add_expenses(expenses)
            except ValueError:
                print("invalid entry")
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.monthly_summary()
        elif choice == "4":
            tracker.category_analysis()
        elif choice == "5":
            print("Existing Program")
            break
        else:
            print("invalid Choice")
if __name__ == "__main__":
     main()