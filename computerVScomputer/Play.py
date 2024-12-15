import copy
import random
class Play:
    def __init__(self, game):
        self.game = game

    

    def randomize_heuristic(self):
        """
        Randomly assign a heuristic (1 or 2) to the game for the current turn.
        """
        self.game.heuristic = random.choice([1, 2])

    def human_turn(self, clicked_pit):
        print(f"Clicked on pit: {clicked_pit}")
        pit = self.game.state.do_move(self.game.player_side["HUMAN"], clicked_pit)
        # Check for game over
        if self.game.game_over():
            return True  # Game over
        return False  # Continue game

    def computer_turn(self, current_player):
        """
        Perform a turn for the current computer player.
        Args:
            current_player: The key in player_side dictionary ('COMPUTER1' or 'COMPUTER2')
        """
        self.randomize_heuristic()  # Randomly select a heuristic
        print(f"{current_player}'s turn using heuristic {self.game.heuristic}")

        _, best_pit = self.MinimaxAlphaBetaPruning(self.game, self.game.player_side[current_player], 5, float('-inf'), float('inf'))

        if best_pit is not None:
            print(f"{current_player} chose pit: {best_pit}")
            self.game.state.do_move(self.game.player_side[current_player], best_pit)
            return self.game.game_over()  # Return whether the game is over
        else:
            print(f"{current_player} has no valid moves.")
            return True

        

    def MinimaxAlphaBetaPruning(self, game, player, depth, alpha, beta):
        """
        Minimax algorithm with Alpha-Beta Pruning.
        The evaluation function is selected based on the current player.
        """
        if game.game_over() or depth == 0:
            best_value = game.evaluate()  # This will use either heuristic 1 or 2
            return best_value, None

        if player == 2:  # COMPUTER/MAX
            best_value = float('-inf')
            best_pit = None
            for pit in game.state.possible_moves(player):
                child_game = copy.deepcopy(game)
                child_game.state.do_move(player, pit)

                value, _ = self.MinimaxAlphaBetaPruning(child_game, game.player_side["COMPUTER1"], depth - 1, alpha, beta)

                if value > best_value:
                    best_value = value
                    best_pit = pit

                alpha = max(alpha, best_value)
                if best_value >= beta:
                    break

            return best_value, best_pit

        else:  # HUMAN/MIN
            best_value = float('inf')
            best_pit = None
            for pit in game.state.possible_moves(player):
                child_game = copy.deepcopy(game)
                child_game.state.do_move(player, pit)

                value, _ = self.MinimaxAlphaBetaPruning(child_game, game.player_side["COMPUTER2"], depth - 1, alpha, beta)

                if value < best_value:
                    best_value = value
                    best_pit = pit

                beta = min(beta, best_value)
                if best_value <= alpha:
                    break

            return best_value, best_pit


        
            
        