import unittest
import budget
from budget import create_spend_chart

class UnitTests(unittest.TestCase):
    maxDiff = None
    def setUp(self):
        self.food = budget.Category("Food")
        self.entertainment = budget.Category("Entertainment")
        self.business = budget.Category("Business")

    def test_deposit(self):
        self.food.deposit(900, "deposit")
        self.assertEqual(self.food.ledger[0], {"amount": 900, "description": "deposit"})

    def test_deposit_no_description(self):
        self.food.deposit(45.56)
        self.assertEqual(self.food.ledger[0], {"amount": 45.56, "description": ""})

    def test_withdraw(self):
        self.food.deposit(900)
        self.food.withdraw(45.67, "groceries")
        self.assertEqual(self.food.ledger[1], {"amount": -45.67, "description": "groceries"})

    def test_withdraw_no_description(self):
        self.food.deposit(900)
        result = self.food.withdraw(45.67)
        self.assertEqual(self.food.ledger[1], {"amount": -45.67, "description": ""})
        self.assertTrue(result)

    def test_get_balance(self):
        self.food.deposit(900)
        self.food.withdraw(45.67)
        self.assertEqual(self.food.get_balance(), 854.33)

    def test_transfer(self):
        self.food.deposit(900)
        result = self.food.transfer(200, self.entertainment)
        self.assertTrue(result)
        self.assertEqual(self.food.ledger[1], {"amount": -200, "description": "Transfer to Entertainment"})
        self.assertEqual(self.entertainment.ledger[0], {"amount": 200, "description": "Transfer from Food"})

    def test_check_funds(self):
        self.food.deposit(10)
        self.assertFalse(self.food.check_funds(20))
        self.assertTrue(self.food.check_funds(10))

    def test_withdraw_no_funds(self):
        self.food.deposit(100)
        self.assertFalse(self.food.withdraw(150))

    def test_transfer_no_funds(self):
        self.food.deposit(100)
        self.assertFalse(self.food.transfer(200, self.entertainment))

    def test_str_output(self):
        self.food.deposit(1000, "initial deposit")
        self.food.withdraw(10, "snacks")
        self.food.transfer(50, self.entertainment)
        result = str(self.food)
        self.assertIn("initial deposit", result)
        self.assertIn("snacks", result)
        self.assertIn("Transfer to Entertainment", result)
