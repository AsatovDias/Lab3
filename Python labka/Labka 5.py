from itertools import product

# Lists of products
breads = ["white", "whole grain", "sourdough"]
meats = ["chicken", "beef", "turkey"]
vegetables = ["lettuce", "tomato", "onion"]
sauces = ["mayonnaise", "mustard", "ketchup"]

# Generate all possible sandwich combinations
combinations = product(breads, meats, vegetables, sauces)

# Output the combinations
print("All possible sandwich combinations:")
for combo in combinations:
    print(f"{combo[0]} bread with {combo[1]}, {combo[2]}, and {combo[3]}")
