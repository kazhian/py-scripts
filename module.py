def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

def reveal_car_specs(**specs):
    """Summarize the car we are about to buy."""
    # print(f"\nA {specs['make']} {specs['model']} with {specs['color']} color is going to buy it.")
    for key, value in specs.items():
        print(f"{key}: {value}")
    print("\n")