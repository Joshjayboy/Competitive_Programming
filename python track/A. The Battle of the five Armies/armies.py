# def calculate_power_level(capabilities, counts):
#     return sum(capabilities[i] * counts[i] for i in range(5))

# # Read input
# capabilities = list(map(int, input().split()))
# counts = list(map(int, input().split()))

# # Power level of Bilbo's side
# bilbo_power = calculate_power_level(capabilities[:3], counts[:3])

# # Power level of opposing side
# opposing_power = calculate_power_level(capabilities[3:], counts[3:])

# # Compare power levels
# if bilbo_power > opposing_power:
#     print("WIN")
# elif bilbo_power < opposing_power:
#     print("LOSE")
# else:
#     print("DRAW")






def calculate_power_level(capabilities, counts):
    return sum(capabilities[i] * counts[i] for i in range(5))

# Read input
capabilities = list(map(int, input().split()))
counts = list(map(int, input().split()))

# Calculate total power levels
bilbo_power = calculate_power_level(capabilities[:3], counts[:3])
opposing_power = calculate_power_level(capabilities[3:], counts[3:])

# Compare power levels and output the result
if bilbo_power > opposing_power:
    print("WIN")
elif bilbo_power < opposing_power:
    print("LOSE")
else:
    print("DRAW")
