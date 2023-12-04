# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line
import operator
# PART 1


class Player():
    def __init__(self, name, speed, endurance, accuracy):
        self.name = name
        if speed >= 0 and speed <= 1:
            self.speed = speed
        else:
            raise ValueError
        if endurance >= 0 and endurance <= 1:
            self.endurance = endurance
        else:
            raise ValueError
        if accuracy >= 0 and accuracy <= 1:
            self.accuracy = accuracy
        else:
            raise ValueError

    def __str__(self):
        return f"Hello everyone, my name is {self.name}."

    def introduce(self):
        return f"Hello everyone, my name is {self.name}."

    def strength(self):
        skills = {
            'speed': self.speed,
            'endurance': self.endurance,
            'accuracy': self.accuracy
        }
        skill_max = max(skills.items(), key=operator.itemgetter(1))[0]
        print(skill_max)
        return ((skill_max), skills[skill_max])


alice = Player('Alice', 0.8, 0.2, 0.6)
bob = Player('Bob', 0.7, 0.2, 0.6)

print(alice)
print(bob)
# print('Alice', alice.strength())
# print('Bob', bob.strength())


# PART 2


class Commentator():
    profession = 'Comentator'

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Hello everyone, my name is {self.name} and I'm a {self.profession}"

    def sum_player(self, player):
        self.player = player
        speed = getattr(player, 'speed')
        endurance = getattr(player, 'endurance')
        accuracy = getattr(player, 'accuracy')

        return speed + endurance + accuracy

    def compare_players(self, player_1, player_2, att):
        player_1_sum = self.sum_player(player_1)
        player_2_sum = self.sum_player(player_2)
        x = player_1.strength()[1]
        y = player_2.strength()[1]

        if player_1.speed > player_2.speed:
            return player_1.name
        elif player_1.speed < player_2.speed:
            return player_2.name
        else:
            if x > y:
                return player_1.name
            elif x < y:
                return player_2.name
            else:
                if player_1_sum > player_2_sum:
                    return player_1.name
                elif player_1_sum < player_2_sum:
                    return player_2.name
                else:
                    return 'These two players might as well be twins!'


ray = Commentator('Ray Hudson')
print(ray.name)
print(ray.compare_players(alice, bob, 'speed'))
