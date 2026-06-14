from collections import deque
import random
import msvcrt
import os

def get_direction():
    if not msvcrt.kbhit():
        return None
    
    key = msvcrt.getch()

    if key == b"\xe0":  # special key
        key = msvcrt.getch()

        return {
            b"H": "U",  # Up
            b"P": "D",  # Down
            b"M": "R",  # Right
            b"K": "L",  # Left
        }.get(key)

    return None

class SnakeGame():
    def __init__(self, width: int, height:int , food: list[list[int]]) -> None:
        self.width = width
        self.height = height
        self.food = None
        self.food_index = 0
        self.score = 0
        start = (self.height // 2, self.width // 2)
        self.snake = deque([start])
        self.snake_set = {(start)}
        self.spawn_food()
        self.print_board()
    
    def spawn_food(self):
        empty_cells = []

        for r in range(self.height):
            for c in range(self.width):
                if (r, c) not in self.snake_set:
                    empty_cells.append((r, c))

        if not empty_cells:
            self.food = None  # player wins
            return

        self.food = random.choice(empty_cells)
    
    def move(self, direction: str) -> int:
        i, j = self.snake[0]
        x, y = i, j
        match(direction):
            case "U":
                x -= 1
            case "D":
                x += 1
            case "L":
                y -= 1
            case "R":
                y += 1
        if x < 0 or x >= self.height or y < 0 or y >= self.width:
            print("Game Over (Wall Collision)")
            return -1
        
        tail = self.snake[-1]
        
        #if self.food_index < len(self.food) and x == self.food[self.food_index][0] and y == self.food[self.food_index][1]:
        if x == self.food[0] and y == self.food[1]:
            self.score += 1
            #self.food_index += 1
            self.spawn_food()
            #if self.food_index == len(self.food):
            #    print("You Win!")
            #    return -1
        else:
            self.snake.pop()
            self.snake_set.remove(tail)
        
        if (x, y) in self.snake_set:
            print('Game Over (Ourobouros')
            return -1
        
        self.snake.appendleft((x, y))
        self.snake_set.add((x, y))
        
        self.print_board()
        return len(self.snake) - 1
        
    def print_board(self) -> None:
        os.system("cls")
        #print("|", end="")
        
        # Draw food
        #if self.food_index < len(self.food):
        #    r, c = self.food[self.food_index]
        #    board[r][c] = 'F'
        TAIL = "🟢"   # circle
        BODY = "🟩"
        HEAD = "🐍"
        FOOD = "🐀"
        EMPTY = "⬛"

        board = [[EMPTY for _ in range(self.width)]
                 for _ in range(self.height)]

        
        if self.food:
            fr, fc = self.food
            board[fr][fc] = FOOD

        # Draw snake body
        for r, c in list(self.snake)[1:]:
            board[r][c] = BODY if (r, c) != list(self.snake)[-1] else TAIL

        # Draw head
        hr, hc = self.snake[0]
        board[hr][hc] = HEAD

        for row in board:
            print(' '.join(row))
        print()
        
game = SnakeGame(10, 10, [[1,2],[0,1]])
game.print_board()
moves = ["R", "D", "R", "U", "L", "U"]

score = 0
try:
    while True:
        direction = get_direction()

        if direction:
            score = game.move(direction)

            if score == -1:
             break
except KeyboardInterrupt:
    print("\nGame terminated.")
                