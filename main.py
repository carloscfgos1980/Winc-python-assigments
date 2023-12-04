# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line


def farm_action(weather, time_of_day, cow_milk_status, location_cow, season, slurry_tank_full, grass_long):
    if weather == 'sunny' and time_of_day == 'day' and cow_milk_status == True and location_cow == 'pasture' and season == 'spring' and slurry_tank_full == False and grass_long == True:
        return ('take cows to cowshed \nmilk cows \ntake cows back to pasture')
    elif grass_long == True and season == 'spring' and weather == 'sunny' and location_cow == 'cowshed':
        print('mow grass')
        return True
    elif cow_milk_status == True and location_cow == 'cowshed':
        print('milk cows')
        return True
    elif slurry_tank_full == True and location_cow == 'cowshed' and weather != 'sunny' and weather != 'windy':
        print('fertilize pasture')
        return True
    elif weather == 'rain' or time_of_day == 'night':
        print('take cows to cowshed')
        return True
    else:
        print('Wait')
        return False


print(farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True))

print(farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True))

print(farm_action('windy', 'night', True, 'cowshed', 'winter', True, True))

print(farm_action('sunny', 'day', True, 'pasture', 'spring', False, True))
