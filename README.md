# 💰 Well Spend Budget Tracker

A simple Python project to help you manage your expenses across different categories like Food, Clothing, Entertainment, and more. You can deposit, withdraw, transfer funds, and even see a visual chart of your spending!

---

## 🚀 Features

- Track spending for multiple categories (e.g. Food, Clothing, Business)
- Deposit and withdraw money with optional descriptions
- Transfer money from one category to another
- Get current balance for any category
- Visualize spending using a **spend chart**

---

## 📁 Files in the Project

| File Name       | Description                                     |
|----------------|-------------------------------------------------|
| `budget.py`     | Contains the main logic and the `Category` class |
| `main.py`       | Sample usage of the Budget Tracker              |
| `test_module.py`| Unit tests to verify the functionality          |

---

## 🧾 Example Output

After running the code in `main.py`, you'll get outputs like:

```text
934.11
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more f   -15.89
Transfer to Clothing    -50.00
Total: 923.96

***********Clothing***********
Transfer from Food        50.00
                         -25.55
                        -100.00
Total: -75.55

Percentage spent by category
100|          
 90|          
 80|          
 70|    o     
 60|    o     
 50|    o     
 40|    o     
 30|    o     
 20|    o  o  
 10|    o  o  
  0| o  o  o  
    ----------
     B  F  E  
     u  o  n  
     s  o  t  
     i  d  e  
     n     r  
     e     t  
     s     a  
     s     i  
           n  
           m  
           e  
           n  
           t
