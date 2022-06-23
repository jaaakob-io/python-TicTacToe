class Game():
    match_fields = ['', '', '', '', '', '', '', '', '']
    player_one = ''
    player_two = ''
    move_player_one = True

    def initial_game(self):
        self.player_one = self.enter_player_name('Enter name for Player 1: ')
        self.player_two = self.enter_player_name('Enter name for Player 2: ')

    def enter_player_name(self, prompt: str):
        name = ''
        while not name:
            name = input(prompt)
        return name

    def play_game(self):
        print('Let\'s start playing')
        while not self.game_is_over():
            self.print_game()
            if self.move_player_one:
                self.perform_move(self.player_one)
            else:
                self.perform_move(self.player_two)

        self.print_game()

    def perform_move(self, player_name: str):
        field = -1
        while field < 0 or field > 8 or self.match_fields[field]:
            try:
                field = int(input(f'It\'s your move {player_name}: ')) - 1
            except ValueError:
                continue
        self.match_fields[field] = 'X' if self.move_player_one else 'O'
        self.move_player_one = not self.move_player_one

    def game_is_over(self) -> bool:
        if self.check_similarity(self.match_fields[0], self.match_fields[1], self.match_fields[2]) or \
                self.check_similarity(self.match_fields[3], self.match_fields[4], self.match_fields[5]) or \
                self.check_similarity(self.match_fields[6], self.match_fields[7], self.match_fields[8]) or \
                self.check_similarity(self.match_fields[2], self.match_fields[4], self.match_fields[6]) or \
                self.check_similarity(self.match_fields[0], self.match_fields[3], self.match_fields[6]) or \
                self.check_similarity(self.match_fields[1], self.match_fields[4], self.match_fields[7]) or \
                self.check_similarity(self.match_fields[2], self.match_fields[5], self.match_fields[8]) or \
                self.check_similarity(self.match_fields[0], self.match_fields[4], self.match_fields[8]):
            return True

        for field in self.match_fields:
            if not field:
                return False

        return True

    def check_similarity(self, a: str, b: str, c: str):
        return a == b and b == c and a == c and a != ''

    def print_game(self):
        for index, field in enumerate(self.match_fields):
            if index % 3 == 0:
                print('\n|', end='')
            if not field:
                print(' ', end='|')
            else:
                print(field, end='|')
        print('\n')


if __name__ == '__main__':
    game = Game()
    game.initial_game()
    game.play_game()
