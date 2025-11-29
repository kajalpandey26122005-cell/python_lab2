import os

class SOSGame:
    def __init__(self, board_size=3):
        self.board_size = board_size
        self.board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
        self.player1_score = 0
        self.player2_score = 0
        self.current_player = 1
        self.move_count = 0
    
    def display_board(self):
        """Display the current game board"""
        print("\n")
        print("   ", end="")
        for col in range(self.board_size):
            print(f" {col} ", end="")
        print()
        print("  " + "---" * self.board_size)
        
        for row in range(self.board_size):
            print(f"{row} | ", end="")
            for col in range(self.board_size):
                print(f"{self.board[row][col]} | ", end="")
            print()
            print("  " + "---" * self.board_size)
        print()
    
    def is_valid_move(self, row, col):
        """Check if a move is valid"""
        if row < 0 or row >= self.board_size or col < 0 or col >= self.board_size:
            return False
        return self.board[row][col] == ' '
    
    def check_sos(self, row, col, letter):
        """Check if placing a letter creates an SOS pattern"""
        directions = [
            (0, 1),   # Horizontal
            (1, 0),   # Vertical
            (1, 1),   # Diagonal down-right
            (1, -1),  # Diagonal down-left
        ]
        
        sos_count = 0
        
        for dr, dc in directions:
            # Check in both directions along each line
            for start_offset in [-2, 0]:
                positions = [(row + (start_offset + i) * dr, col + (start_offset + i) * dc) for i in range(3)]
                
                # Check if all positions are within bounds
                if all(0 <= r < self.board_size and 0 <= c < self.board_size for r, c in positions):
                    letters = ''.join(self.board[r][c] for r, c in positions)
                    if letters == 'SOS':
                        sos_count += 1
        
        return sos_count
    
    def make_move(self, row, col, letter):
        """Make a move on the board"""
        letter = letter.upper()
        
        if letter not in ['S', 'O']:
            print("Invalid letter! Use 'S' or 'O'")
            return False
        
        if not self.is_valid_move(row, col):
            print("Invalid position! Cell is already occupied or out of bounds.")
            return False
        
        self.board[row][col] = letter
        sos_found = self.check_sos(row, col, letter)
        
        if sos_found > 0:
            if self.current_player == 1:
                self.player1_score += sos_found
                print(f"Player 1 found {sos_found} SOS pattern(s)!")
            else:
                self.player2_score += sos_found
                print(f"Player 2 found {sos_found} SOS pattern(s)!")
            return True
        
        return True
    
    def is_board_full(self):
        """Check if the board is full"""
        return all(self.board[row][col] != ' ' for row in range(self.board_size) for col in range(self.board_size))
    
    def switch_player(self):
        """Switch to the other player"""
        self.current_player = 2 if self.current_player == 1 else 1
    
    def play(self):
        """Main game loop"""
        print("=" * 40)
        print("Welcome to SOS Game!")
        print("=" * 40)
        print("Rules: Create 'SOS' patterns horizontally, vertically, or diagonally.")
        print("Each SOS pattern earns 1 point. The player with the most points wins!")
        print()
        
        while True:
            self.display_board()
            print(f"Player 1 Score: {self.player1_score} | Player 2 Score: {self.player2_score}")
            print(f"Current Player: {self.current_player}")
            
            if self.is_board_full():
                print("\nGame Over! Board is full.")
                break
            
            while True:
                try:
                    row = int(input(f"Player {self.current_player}, enter row (0-{self.board_size-1}): "))
                    col = int(input(f"Player {self.current_player}, enter column (0-{self.board_size-1}): "))
                    letter = input("Enter letter (S or O): ")
                    
                    if self.make_move(row, col, letter):
                        break
                except ValueError:
                    print("Invalid input! Please enter numbers for row and column.")
            
            self.switch_player()
        
        # Display final results
        self.display_board()
        print("=" * 40)
        print("Final Scores:")
        print(f"Player 1: {self.player1_score}")
        print(f"Player 2: {self.player2_score}")
        
        if self.player1_score > self.player2_score:
            print("Player 1 Wins!")
        elif self.player2_score > self.player1_score:
            print("Player 2 Wins!")
        else:
            print("It's a Tie!")
        print("=" * 40)

if __name__ == "__main__":
    game = SOSGame(board_size=3)
    game.play()