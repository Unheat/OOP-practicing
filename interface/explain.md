https://algomaster.io/learn/lld/interfaces

### Study Note: Interfaces, Polymorphism, and Decoupling

An interface is a powerful contract in object-oriented programming that defines what a class must do, without dictating how it should do it. In enterprise software development, designing systems around interfaces is a fundamental requirement for creating scalable, maintainable, and testable codebases.

---

### Key Concepts

1. **Programming to an Interface, Not an Implementation**
Instead of declaring variables as specific concrete classes (e.g., `StripePayment`), you declare them using the interface type (e.g., `PaymentGateway`). This ensures your high-level logic is completely insulated from changes in low-level infrastructure.
2. **Polymorphism ("Many Forms")**
Polymorphism allows a single interface type to hold different underlying concrete objects at runtime. When a method is called on the interface reference, the system dynamically executes the specific implementation belonging to the active object.
3. **Decoupling and Single Responsibility**
By wrapping infrastructure tasks (like third-party API connections) inside independent gateway classes, your core service classes (like checkout or order processing) stay completely focused on business logic. They do not need to know about HTTP headers, encryption keys, or API endpoints.
4. **Unit Testability**
Interfaces allow you to easily replace real-world external dependencies with harmless "mock" or "fake" implementations during testing, avoiding real network calls or financial charges.

---

### Production-Grade Code Example

Here is the complete architectural layout demonstrating how these components interact cleanly:

```java
// 1. The Contract (Interface)
interface PaymentGateway {
    void initiatePayment(double amount);
}

// 2. Concrete Implementation A
class StripePayment implements PaymentGateway {
    @Override
    public void initiatePayment(double amount) {
        // Real infrastructure logic for Stripe
        System.out.println("Executing Stripe API network call to charge $" + amount);
    }
}

// 3. Concrete Implementation B
class PayPalPayment implements PaymentGateway {
    @Override
    public void initiatePayment(double amount) {
        // Real infrastructure logic for PayPal
        System.out.println("Redirecting to PayPal secure portal to charge $" + amount);
    }
}

// 4. Core Business Logic (The Orchestrator)
class CheckoutService {
    private final PaymentGateway gateway; // Decoupled reference

    // Dependency Injection: Pass the implementation via the constructor
    public CheckoutService(PaymentGateway gateway) {
        this.gateway = gateway;
    }

    public void checkout(double amount) {
        // High-level business rules would go here (e.g., tax, inventory)
        
        // Delegate the actual payment setup to the injected gateway
        gateway.initiatePayment(amount);
    }
}

```

### Why We Design Systems This Way

Without this setup, changing from Stripe to PayPal would require you to open up your `CheckoutService` class and manually rewrite the core business logic, introducing significant regression risks.

With this setup, the `CheckoutService` remains completely untouched. You simply swap the implementation at runtime when instantiating the service:

```java
// To use Stripe:
CheckoutService stripeService = new CheckoutService(new StripePayment());
stripeService.checkout(120.50);

// To switch to PayPal, no core logic changes:
CheckoutService payPalService = new CheckoutService(new PayPalPayment());
payPalService.checkout(120.50);

```

---
