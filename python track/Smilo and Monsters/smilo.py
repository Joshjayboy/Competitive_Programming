t = int(input())

for _ in range(t):
    n = int(input())
    hordes = list(map(int, input().split()))
    
    total_attacks = 0
    remaining_monsters = sum(hordes)
    combo_counter = 0
    
    for horde in hordes:
        remaining_monsters -= min(horde, combo_counter)
        combo_counter = max(0, combo_counter - horde)
        
        # If there are still monsters remaining in the horde after the first type of attack
        if horde > combo_counter:
            # Calculate how many ultimate attacks we need to finish off the remaining monsters
            ultimate_attacks = (horde - combo_counter + combo_counter - 1) // combo_counter
            total_attacks += ultimate_attacks
            remaining_monsters -= combo_counter * ultimate_attacks
            combo_counter = 0
        
        # Increment the combo counter for the next attack
        combo_counter += min(horde, remaining_monsters)
        
    total_attacks += remaining_monsters // n
    if remaining_monsters % n != 0:
        total_attacks += 1
    
    print(total_attacks)
