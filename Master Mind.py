""" 	MASTER MIND 
	Author: Dan Murphy
	Date: 2023-02-24 """

from random import choices
from dataclasses import dataclass

COLORS: list[str] = 'R O Y G B W'.split(' ')
ROUNDS: int = 10


@dataclass
class MasterMind:
    seq: list[str]
    guesses: int = 0
    rounds: int = ROUNDS

    def check_guess(self, guess_list: list[str]) -> tuple[int, int]:
        """ takes in a list of colors """
        """ returns a tuple (exact matches, partial matches) """

        temp_seq = self.seq.copy()
        rem_guess = guess_list.copy()
        exact_count = 0
        partial_count = 0

        # Check exacts first
        for guess, actual in zip(guess_list, self.seq):
            # Exact Match
            if guess == actual:
                exact_count += 1
                temp_seq.remove(guess)
                rem_guess.remove(guess)

        # Check partials next
        for guesses in rem_guess:
            if guesses in temp_seq:
                partial_count += 1
                temp_seq.remove(guesses)

        return exact_count, partial_count

    @property
    def print_guesses_remaining(self) -> str:
        return f'You have {self.rounds - self.guesses} guesses left:'

    @property
    def print_winning(self):
        return f'\nYou Win!! You guessed in {self.guesses} tries!\n\n'

    @property
    def print_losing(self):
        return f'\nYou ran out of tries. Game over!\n' \
               f'The correct seq was {self.seq}\n\n'

    @property
    def user_start_over(self) -> bool:

        self.guesses = self.rounds
        another_game = input('Would you like to play again? Y/N: ').upper()[0]
        if another_game == 'Y':
            return True
        else:
            return False

    @property
    def get_user_guess(self) -> list[str]:
        user_guess = input(f'Color Choices {COLORS}\n'
                           f'Enter 4 colors separate by spaces: ').upper().split(' ')
        if not set(user_guess).issubset(set(COLORS)):
            print('Invalid color choices!')
            raise ValueError
        if len(user_guess) != 4:
            print('Number of colors chosen Invalid!')
            raise ValueError

        return user_guess


def main():

    keep_playing = True

    while keep_playing:
        game_board = MasterMind(choices(COLORS, k=4))
        print(f'You are starting with {game_board.rounds} guesses\n')
        while game_board.guesses < game_board.rounds:
            guess = game_board.get_user_guess
            exact, partial = game_board.check_guess(guess)

            if exact == 4:
                print(game_board.print_winning)
                keep_playing = game_board.user_start_over
                break
            else:
                print(f'You got {exact} exact and {partial} partial matches\n')

            game_board.guesses += 1
            print(game_board.print_guesses_remaining)

            if game_board.guesses == game_board.rounds:
                print(game_board.print_losing)
                keep_playing = game_board.user_start_over
                break


if __name__ == '__main__':
    main()