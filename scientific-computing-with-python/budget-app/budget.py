class Category:

  def __init__(self, category):
    self.category = category
    self.ledger = []

  def deposit(self, price, desc=""):
    self.ledger.append({"amount": price, "description": desc})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False

  def get_balance(self):
    return sum(item["amount"] for item in self.ledger)

  def transfer(self, amount, budget_category):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {budget_category.category}")
      budget_category.deposit(amount, f"Transfer from {self.category}")
      return True
    return False

  def check_funds(self, amount):
    return amount <= self.get_balance()

  def __str__(self):
    title = self.category.center(30, "*")
    items = "\n".join([
        f"{item['description'][:23]:23} {item['amount']:.2f}"
        for item in self.ledger
    ])
    total = f"Total: {self.get_balance():.2f}"
    return f"{title}\n{items}\n{total}"


def create_spend_chart(categories):
  spend_percentages = []
  total_spent = 0

  for category in categories:
    withdrawals = sum(transaction["amount"] for transaction in category.ledger
                      if transaction["amount"] < 0)
    total_spent += withdrawals

  for category in categories:
    withdrawals = sum(transaction["amount"] for transaction in category.ledger
                      if transaction["amount"] < 0)
    spend_percentage = (withdrawals / total_spent) * 100
    spend_percentages.append(spend_percentage - spend_percentage % 10)

  chart = "Percentage spent by category\n"
  for i in range(100, -1, -10):
    chart += str(i).rjust(3) + "| "
    for percentage in spend_percentages:
      if percentage >= i:
        chart += "o  "
      else:
        chart += "   "
    chart += "\n"

  chart += "    -" + "---" * len(categories) + "\n"

  max_category_length = max(len(category.category) for category in categories)

  for i in range(max_category_length):
    chart += "     "
    for category in categories:
      if i < len(category.category):
        chart += category.category[i] + "  "
      else:
        chart += "   "
    if i < max_category_length - 1:
      chart += "\n"

  return chart

