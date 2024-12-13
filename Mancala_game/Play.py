import copy

class Play:
    def __init__(self, game):
        self.game = game

    def human_turn(self, clicked_pit):
        print(f"Clicked on pit: {clicked_pit}")
        pit = self.game.state.do_move(self.game.player_side["HUMAN"], clicked_pit)
        # Check for game over
        if self.game.game_over():
            return True  # Game over
        return False  # Continue game

    def computer_turn(self):
        print("Computer's turn")
        _, best_pit = self.MinimaxAlphaBetaPruning(self.game, self.game.player_side["COMPUTER"], 5, float('-inf'), float('inf'))

        if best_pit:
            print(f"Computer chose pit: {best_pit}")
            self.game.state.do_move(self.game.player_side["COMPUTER"], best_pit)

        # Check for game over
        if self.game.game_over():
            return True  # Game over
        return False  # Continue game

    def MinimaxAlphaBetaPruning(self, game, player, depth, alpha, beta):
        """
        Minimax algorithm with Alpha-Beta Pruning.

        Args:
            game (Game): Current game state.
            player (int): Current player (1 for COMPUTER/MAX, -1 for HUMAN/MIN).
            depth (int): Maximum depth of the search tree.
            alpha (float): Alpha value for pruning.
            beta (float): Beta value for pruning.

        Returns:
            tuple: Best value and best pit.
        """
        if game.game_over() or depth == 0:
            best_value = game.evaluate()
            return best_value, None

        if player == 2:  # COMPUTER/MAX
            best_value = float('-inf')
            best_pit = None
            for pit in game.state.possible_moves(player):
                child_game = copy.deepcopy(game)
                child_game.state.do_move(player, pit)

                value, _ = self.MinimaxAlphaBetaPruning(child_game, self.game.player_side["HUMAN"], depth - 1, alpha, beta)

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

                value, _ = self.MinimaxAlphaBetaPruning(child_game, self.game.player_side["COMPUTER"], depth - 1, alpha, beta)

                if value < best_value:
                    best_value = value
                    best_pit = pit

                beta = min(beta, best_value)
                if best_value <= alpha:
                    break

            return best_value, best_pit

        
            
        