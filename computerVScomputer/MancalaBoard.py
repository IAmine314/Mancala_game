
import pygame
class MancalaBoard:
    def __init__(self):
        self.board = {
            "A":4, "B":4, "C":4, "D":4, "E":4, "F":4, 1:0,
            "G":4, "H":4, "I":4, "J":4, "K":4, "L":4, 2:0,
        }

        self.player1_pits = ("A", "B", "C", "D", "E", "F")
        self.player2_pits = ("G", "H", "I", "J", "K", "L")

        self.opposite_pits = {
            "A": "G", "B": "H", "C": "I", "D": "J", "E": "K", "F": "L",
            "G": "A", "H": "B", "I": "C", "J": "D", "K": "E", "L": "F",
        }

        self.next_pit = {
            "A": "B", "B": "C", "C": "D", "D": "E", "E": "F", "F": 1,
            "G": "H", "H": "I", "I": "J", "J": "K", "K": "L", "L": 2,
            1: "G", 2: "A",
        }

    def possible_moves(self, player):
        
        pits = self.player1_pits if player == 1 else self.player2_pits

        return [pit for pit in pits if self.board[pit] > 0]

    def do_move(self, player, pit):

        if pit not in self.possible_moves(player):
            pygame.quit()
            raise ValueError("invalid move : pit is empty or does not belong to this player")
        else:
            seeds = self.board[pit]
            self.board[pit] = 0

            current_pit = pit
            while seeds > 0 :
                current_pit = self.next_pit[current_pit]
                if (current_pit == 1 and player == 2) or (current_pit == 2 and player == 1):
                    continue

                self.board[current_pit] += 1
                seeds -= 1


            if current_pit in self.player1_pits + self.player2_pits:
                if self.board[current_pit] == 1 and current_pit in (
                    self.player1_pits if player == 1 else self.player2_pits
                ):
                    opposite = self.opposite_pits[current_pit]
                    captured_seeds = self.board[opposite]
                    self.board[opposite] = 0
                    self.board[current_pit] = 0
                    self.board[player] += captured_seeds + 1

            return current_pit
