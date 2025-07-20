# Single Responsibility Principle
# Open Close Primaciple
# Liskov Substitituion Principle
# Interface segregation principle
# Dependency Inversion Principle

from abc import ABC,abstractmethod
#-- Signle Responsibility Principle
class Order:
    def __init__(self,items:list[dict],customer_email:str):
        self.items=items
        self.customer_email=customer_email
        self.total_price=0.0
    
    def add_item(self,item:dict):
        self.items.append(item)
        
    #Note 
    #Calculation, Payment and Notification responsibility all these are seperate responsibility

class PriceCalculator:
    def calculate_total(self,order:Order) -> float:
        total=0.0
        for item in order.items:
            total += item.get('price',0.0) * item.get('quantity',1)
        order.total_price=total
        return total   
    
class OrderValidator:
    def is_valid(self, order: Order) -> bool:
        if not order.items:
            print("Validation Error: Order must have items.")
            return False
        if not order.customer_email or "@" not in order.customer_email:
            print("Validation Error: Invalid customer email.")
            return False
        # Add more validation rules as needed
        return True
        
        
# --- O: Open/Closed Principle (OCP) ---
# Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.

# PaymentProcessor (abstraction - open for extension)
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

class CreditCardPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing credit card payment of ${amount:.2f}")
        # Simulate payment gateway interaction
        return True

class PayPalPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing PayPal payment of ${amount:.2f}")
        # Simulate PayPal API interaction
        return True

# NotificationSender (abstraction - open for extension)
class NotificationSender(ABC):
    @abstractmethod
    def send_notification(self, recipient: str, message: str):
        pass

class EmailNotificationSender(NotificationSender):
    def send_notification(self, recipient: str, message: str):
        print(f"Sending email to {recipient}: {message}")

class SMSNotificationSender(NotificationSender):
    def send_notification(self, recipient: str, message: str):
        print(f"Sending SMS to {recipient}: {message}")                
        
# --- L: Liskov Substitution Principle (LSP) ---
# Subtypes must be substitutable for their base types without altering the correctness of the program.
# This is demonstrated by how CreditCardPaymentProcessor and PayPalPaymentProcessor can be used interchangeably
# wherever a PaymentProcessor is expected. Similarly for NotificationSender.

# --- I: Interface Segregation Principle (ISP) ---
# Clients should not be forced to depend on interfaces they do not use.
# Better to have many small, specific interfaces than one large, general-purpose interface.

# Instead of a single 'IOrderService' with all methods, we have smaller, focused interfaces (ABCs).
# PaymentProcessor and NotificationSender are good examples of segregated interfaces.
# A class implementing PaymentProcessor doesn't need to care about notifications.

# For a more explicit ISP example, imagine if we had a single `IManager` interface:
# class IManager(ABC):
#     @abstractmethod
#     def manage_orders(self): pass
#     @abstractmethod
#     def manage_customers(self): pass
#     @abstractmethod
#     def generate_reports(self): pass
# If a `CustomerManager` only needed `manage_customers`, it would be forced to implement the others, violating ISP.
# Our current design implicitly follows ISP by having focused abstractions like PaymentProcessor and NotificationSender.

# --- D: Dependency Inversion Principle (DIP) ---
# High-level modules should not depend on low-level modules. Both should depend on abstractions.
# Abstractions should not depend on details. Details should depend on abstractions.

class OrderProcessor:
    def __init__(self,
                 price_calculator: PriceCalculator,
                 validator: OrderValidator,
                 payment_processor: PaymentProcessor, # Depends on abstraction
                 notification_sender: NotificationSender): # Depends on abstraction
        self.price_calculator = price_calculator
        self.validator = validator
        self.payment_processor = payment_processor
        self.notification_sender = notification_sender

    def process_order(self, order: Order) -> bool:
        if not self.validator.is_valid(order):
            self.notification_sender.send_notification(
                order.customer_email, "Your order could not be processed due to validation errors."
            )
            return False

        total = self.price_calculator.calculate_total(order)
        print(f"Calculated total for order: ${total:.2f}")

        if not self.payment_processor.process_payment(total):
            self.notification_sender.send_notification(
                order.customer_email, "Payment failed for your order."
            )
            return False

        self.notification_sender.send_notification(
            order.customer_email, f"Your order #{order.items[0].get('id', 'N/A')} has been successfully processed!"
        )
        print("Order processed successfully.")
        return True

# --- Demonstration of Usage ---

if __name__ == "__main__":
    # --- Setup Dependencies ---
    price_calculator = PriceCalculator()
    order_validator = OrderValidator()

    # Different payment and notification methods can be chosen at runtime
    credit_card_processor = CreditCardPaymentProcessor()
    paypal_processor = PayPalPaymentProcessor()

    email_sender = EmailNotificationSender()
    sms_sender = SMSNotificationSender()

    # --- Order Processing Scenarios ---

    # Scenario 1: Successful Order with Credit Card and Email
    print("\n--- Scenario 1: Successful Order (Credit Card & Email) ---")
    order1 = Order(items=[
        {'id': 'A1', 'name': 'Laptop', 'price': 1200.00, 'quantity': 1},
        {'id': 'B2', 'name': 'Mouse', 'price': 25.00, 'quantity': 2}
    ], customer_email="alice@example.com")

    order_processor1 = OrderProcessor(
        price_calculator=price_calculator,
        validator=order_validator,
        payment_processor=credit_card_processor, # DIP in action
        notification_sender=email_sender         # DIP in action
    )
    order_processor1.process_order(order1)

    # Scenario 2: Successful Order with PayPal and SMS
    print("\n--- Scenario 2: Successful Order (PayPal & SMS) ---")
    order2 = Order(items=[
        {'id': 'C3', 'name': 'Keyboard', 'price': 75.00, 'quantity': 1}
    ], customer_email="bob@example.com")

    order_processor2 = OrderProcessor(
        price_calculator=price_calculator,
        validator=order_validator,
        payment_processor=paypal_processor, # DIP in action (LSP allows this substitution)
        notification_sender=sms_sender       # DIP in action (LSP allows this substitution)
    )
    order_processor2.process_order(order2)

    # Scenario 3: Invalid Order (no items)
    print("\n--- Scenario 3: Invalid Order (No Items) ---")
    order3 = Order(items=[], customer_email="charlie@example.com")
    order_processor3 = OrderProcessor(
        price_calculator=price_calculator,
        validator=order_validator,
        payment_processor=credit_card_processor,
        notification_sender=email_sender
    )
    order_processor3.process_order(order3)

    # Scenario 4: Invalid Order (bad email)
    print("\n--- Scenario 4: Invalid Order (Bad Email) ---")
    order4 = Order(items=[{'id': 'D4', 'name': 'Monitor', 'price': 300.00, 'quantity': 1}], customer_email="david.com")
    order_processor4 = OrderProcessor(
        price_calculator=price_calculator,
        validator=order_validator,
        payment_processor=credit_card_processor,
        notification_sender=email_sender
    )
    order_processor4.process_order(order4)