# 🍔 Food Ordering System – Creational Design Patterns

## 📌 Overview
This is a Python console application that demonstrates **four Creational Design Patterns** in a single real-life scenario: an **Online Food Ordering System**.  
The project showcases:
- **Singleton**
- **Factory Method**
- **Builder**
- **Prototype**

---

## 🛠 Features
- Build **custom burgers** step-by-step using the **Builder Pattern**.
- Order **pre-made meals** instantly using the **Prototype Pattern**.
- Choose from different payment methods (**Factory Method**).
- Manage all orders through a **Singleton** order manager (centralized state).
- Simple and interactive console menu.

---

## 🧩 Design Patterns Used
### 1️⃣ Singleton – `OrderManager`
Ensures there is **only one instance** managing all orders across the system.

### 2️⃣ Factory Method – `PaymentFactory`
Creates payment method objects (`CreditCard`, `PayPal`, `CashOnDelivery`) dynamically based on user choice.

### 3️⃣ Builder – `CustomBurgerBuilder`
Constructs a burger **step-by-step**, allowing customization of bread, meat, toppings, and sauce.

### 4️⃣ Prototype – `MealPrototype`
Stores **ready-made meal templates** (e.g., Pizza Combo, Sushi Combo) that can be **cloned** quickly for new orders.

---

## ▶️ How to Run
1. **Clone the repository**:
```bash
git clone https://github.com/ahmadashrafgalal/Food-Ordering-Creational-Design-Patterns.git
cd Food-Ordering-Creational-Design-Patterns
````

2. **Run the application**:

```bash
python main.py
```

---

## 📸 Example Output

```
--- Online Food Ordering ---
1. Build custom burger
2. Order pre-made meal (Prototype)
3. Show all orders
4. Exit
Choose: 1
Choose bread: Brioche
Choose meat: Beef
Add a topping: Cheese
Choose sauce: BBQ
Payment method (credit/paypal/cash): paypal
Paid 10$ using PayPal.
```

---

## 💡 Why This Project?

This project is a hands-on example for learning **Creational Design Patterns** in Python.
It’s easy to understand, modify, and extend with more meals, payment methods, or customization options.

---

## 👨‍💻 Author

**Ahmad Ashraf Galal**

LinkedIn: [ahmadashrafgalal](https://www.linkedin.com/in/ahmadashrafgalal)
---