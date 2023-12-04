# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line


def create_passport(nam, date, place, height, origin):
    passport = {
        "name": nam,
        "date_of_birth": date,
        "place_of_birth": place,
        "height_in_meters": height,
        "nationality": origin
    }
    return passport


def add_stamp(land):
    added_stamp = {
        "passport": {
            "name": 'Carlos Infante',
            "date_of_birth": '1980-01-31',
            "place_of_birth": 'Cienfuegos, Cuba',
            "height_in_meters": 1.76,
            "nationality": 'Cuban'
        },
        "country": 'Cuba',
        "stamp": ['Peru', 'Romania', 'Portugal']
    }
    if added_stamp["country"] != land and land not in added_stamp["stamp"]:
        added_stamp["stamp"].append(land)
    return added_stamp


carlos = create_passport(
    'Carlos', '1980-01-31', 'Cienfuegos', 1.76, 'Cuba')


def add_biometric_data(citizen, type_biosimetric, value, date):
    data = {type_biosimetric: {
            'date': date,
            'value': value,
            }
            }
    if citizen.get('biosemtric') is None:
        citizen['biosemtric'] = data
        return citizen
    else:
        citizen['biosemtric'].update(data)
        return citizen


carlos = add_biometric_data(carlos, "eye_color_left", "blue", "2020-05-05")
carlos = add_biometric_data(carlos, "eye_color_right", "blue", "2020-05-05")
carlos = add_biometric_data(carlos, "eye_color_left", "brown", "2022-01-10")


fingerprint_data = {
    "left_pinky": "2378945",
    "left_ring": "2349081",
    "left_middle": "132890",
    "left_index": "9823234",
    "left_thumb": "0924131",
    "right_thumb": "6234923",
    "right_index": "13249734",
    "right_middle": "34023784",
    "right_ring": "12332538",
    "right_pinky": "32458970",


}

carlos = add_biometric_data(carlos, 'finger_prints', fingerprint_data,
                            "2022-01-12")


if __name__ == "__main__":
    countries = get_countries()

# print(countries)
print("passport\n:", create_passport(
    'Carlos', '1980-01-31', 'Cienfuegos', 1.76, 'Cuba'))

print('new country', add_stamp('USA'))
print('already visited:', add_stamp('Peru'))
print('origin cuntry:', add_stamp('Cuba'))

print('checking', carlos)
