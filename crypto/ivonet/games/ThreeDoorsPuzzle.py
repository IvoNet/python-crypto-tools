from random import randint


# --------------------------------------------------------------------------
class Quizmaster(object):
    def __init__(self, prize):
        self.prize_door = prize
        # print "Prize door : %s" % prize

    def askToChoose(self, player):
        self.chosen_door = player.choose()
        # print "Chosen door: %s" % self.chosen_door

    def openEmptyDoor(self):
        if self.chosen_door == self.prize_door:
            ret = [1, 2, 3]
            ret.remove(self.prize_door)
            self.opened_door = ret[randint(0, 1)]
        else:
            ret = [1, 2, 3]
            ret.remove(self.chosen_door)
            ret.remove(self.prize_door)
            self.opened_door = ret[0]
        # print "Opened door: %s" % self.opened_door

    def askPlayerSwitch(self, player):
        if player.wantSwitch():
            ret = [1, 2, 3]
            # if self.chosen_door == self.prize_door:
            #     ret.remove(self.prize_door)
            #     ret.remove(self.opened_door)
            ret.remove(self.opened_door)
            ret.remove(self.chosen_door)
            self.chosen_door = ret[0]
            # print "Switched to: %s" % self.chosen_door
        return self.chosen_door


class Player(object):
    def __init__(self, switch):
        self.switch = switch

    def choose(self):
        self.choice = randint(1, 3)
        return self.choice

    def wantSwitch(self):
        if self.switch == "Random":
            return (randint(0, 1) == 1)
        else:
            return self.switch


class Game(object):
    def __init__(self, switch):
        self.prize = randint(1, 3)
        self.qmaster = Quizmaster(self.prize)
        self.player = Player(switch)

    def play(self):
        self.qmaster.askToChoose(self.player)
        self.qmaster.openEmptyDoor()
        chosen_door = self.qmaster.askPlayerSwitch(self.player)
        won = self.prize == chosen_door
        # print "Has Won: %s" % (won, )
        return won


def range_test(switch, times):
    won = 0
    lost = 0
    for i in range(times):
        game = Game(switch)
        winner = game.play()
        if winner:
            won += 1
        else:
            lost += 1
    print("Games played [%s], won [%s], lost [%s], switch [%s]" % (times, won, lost, switch,))


def main():
    # times_to_test = 1000000
    times_to_test = 100
    range_test(True, times_to_test)
    range_test(False, times_to_test)
    range_test("Random", times_to_test)


if __name__ == "__main__":
    main()
