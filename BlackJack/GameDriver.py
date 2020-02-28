class GameDriver:

    def init_game(self):
        player = input("Please enter your name: ")
        monies = float(input("How much money are you playing with? "))

    def play_game(self):
        return

    def end_game(self):
        play_again = input("Would you like to play another game? Y/N: ")
        return self.start_another_game(play_again)

    def start_another_game(self, play_again):
        return True if play_again.upper() == 'Y' else False
