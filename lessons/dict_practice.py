"""Practice with dictionaries"""

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

ice_cream["mint"] = 3
print(ice_cream)

ice_cream.pop("mint")
print(ice_cream)

print(f"Number of vanilla orders: {ice_cream['vanilla']}")

ice_cream["vanilla"] += 1
print(f"Number of vanilla orders: {ice_cream['vanilla']}")

print(len(ice_cream))
print("mint" in ice_cream)