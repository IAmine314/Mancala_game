

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

        human_store = self.state.board[self.player_side["COMPUTER1"]]
        computer2_store = self.state.board[self.player_side["COMPUTER2"]]

        if human_store > computer2_store:
            return "COMPUTER1", human_store
        elif computer2_store > human_store:
            return "COMPUTER2", computer2_store
        else:
            return "TIE", computer2_store
         

    def evaluate(self):
        if self.heuristic == 1:
            return self.heuristic_1()
        elif self.heuristic == 2:
            return self.heuristic_2()
        


    def heuristic_1(self):
        
        computer1_store = self.state.board[self.player_side["COMPUTER1"]]
        computer2_store = self.state.board[self.player_side["COMPUTER2"]]
        return computer2_store - computer1_store  # Maximize seeds in the store

    def heuristic_2(self):
        """ Complex heuristic: prioritize capturing seeds from opponent's pits """
        human_store = self.state.board[self.player_side["COMPUTER1"]]
        computer_store = self.state.board[self.player_side["COMPUTER2"]]
        
        # Count how many seeds are captured from the opponent
        human_capture = 0
        computer_capture = 0
        
        for pit in self.state.player1_pits:
            if self.state.board[pit] == 0:  # If human's pit is empty, it's captured
                computer_capture += 1
        for pit in self.state.player2_pits:
            if self.state.board[pit] == 0:  # If computer's pit is empty, it's captured
                human_capture += 1

        return (computer_capture - human_capture) + (computer_store - human_store)
