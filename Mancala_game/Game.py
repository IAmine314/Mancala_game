

class Game:
    def __init__(self, state, player_side):
        self.state = state
        self.player_side = player_side

    def game_over(self):
        player1_empty = all(self.state.board[pit] == 0 for pit in self.state.player1_pits)
        player2_empty = all(self.state.board[pit] == 0 for pit in self.state.player2_pits)

        if player1_empty:

            for pit in self.state.player2_pits:
                self.state.board[2] += self.state.board[pit]
                self.state.board[pit] = 0

            return True
        elif player2_empty:
            for pit in self.state.player1_pits:
                self.state.board[1] += self.state.board[pit]
                self.state.board[pit] = 0

            return True
        else : return False

    def find_winner(self):

        human_store = self.state.board[self.player_side["HUMAN"]]
        computer_store = self.state.board[self.player_side["COMPUTER"]]

        if human_store > computer_store:
            return "HUMAN", human_store
        elif computer_store > human_store:
            return "COMPUTER", computer_store
        else:
            return "TIE", computer_store
         

    def evaluate(self):
        human_store = self.state.board[self.player_side["HUMAN"]]
        computer_store = self.state.board[self.player_side["COMPUTER"]]
        return computer_store - human_store
