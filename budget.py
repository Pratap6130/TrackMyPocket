import math
import re

class Category:

  def __init__(self, categories):
    self.categories = categories
    self.ledger = []
    self.budget = 0.00
    self.withdrawAmt = 0.00

  def __str__(self):
    returnString = f"{self.categories:*^30}\n"
    totalValue = 0

    for entry in self.ledger:
      amount = entry["amount"]
      description = entry["description"]
      totalValue += amount
      returnString += f"{description[:23]:<23}{amount:>7.2f}\n"

    returnString += f"Total: {totalValue:.2f}"
    return returnString

  def deposit(self, amount, description=""):
    self.budget += amount
    self.ledger.append({"amount": amount,"description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.withdrawAmt += amount
      self.budget -= amount
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  def get_balance(self):
    return round(self.budget, 2)

  def transfer(self, amount, categoryDest):
    if self.check_funds(amount):
      self.budget -= amount
      self.ledger.append({"amount": -amount, "description": f"Transfer to {categoryDest.categories}"})
      categoryDest.deposit(amount, f"Transfer from {self.categories}")
      return True
    else:
      return False

  def check_funds(self, amount):
    return self.budget >= amount


def create_spend_chart(categories):
  names = []
  lengthNames = []
  returnString = "Percentage spent by category\n"
  percentages = []
  allPercentages = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]

  fullAmt = sum(cat.withdrawAmt for cat in categories)

  for category in categories:
    percentage = math.floor((category.withdrawAmt / fullAmt) * 10) * 10
    percentages.append(percentage)
    names.append(category.categories)
    lengthNames.append(len(category.categories))

  for p in allPercentages:
    returnString += f"{p:>3}|"
    for perc in percentages:
      returnString += " o " if perc >= p else "   "
    returnString += " \n"

  returnString += "    " + "---" * len(categories) + "-\n"

  maxLength = max(lengthNames)
  for i in range(maxLength):
    returnString += "     "
    for name in names:
      returnString += f"{name[i] if i < len(name) else ' '}  "
    returnString += "\n"

  return returnString.rstrip("\n")
