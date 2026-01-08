import random
from typing import Dict
from google.adk import Agent

# -----------------------------
# Game State (Persistent)
# -----------------------------
game_state = {
    "round": 0,
    "max_rounds": 3,
    "user_score": 0,
    "bot_score": 0,
    "user_bomb_used": False,
    "bot_bomb_used": False,
    "game_over": False
}

VALID_MOVES = ["rock", "paper", "scissors", "bomb"]

# -----------------------------
# Tool Functions (Plain Python)
# -----------------------------
def validate_move(move: str, player: str) -> Dict:
    move = move.lower().strip()

    if move not in VALID_MOVES:
        return {"valid": False, "reason": "Invalid move"}

    if move == "bomb":
        if player == "user" and game_state["user_bomb_used"]:
            return {"valid": False, "reason": "User already used bomb"}
        if player == "bot" and game_state["bot_bomb_used"]:
            return {"valid": False, "reason": "Bot already used bomb"}

    return {"valid": True, "move": move}


def resolve_round(user_move: str, bot_move: str) -> Dict:
    winner = "draw"

    if user_move == bot_move:
        winner = "draw"
    elif user_move == "bomb" and bot_move != "bomb":
        winner = "user"
    elif bot_move == "bomb" and user_move != "bomb":
        winner = "bot"
    else:
        rules = {
            "rock": "scissors",
            "scissors": "paper",
            "paper": "rock"
        }
        winner = "user" if rules[user_move] == bot_move else "bot"

    if winner == "user":
        game_state["user_score"] += 1
    elif winner == "bot":
        game_state["bot_score"] += 1

    return {
        "winner": winner,
        "user_move": user_move,
        "bot_move": bot_move
    }


def update_game_state(user_move: str, bot_move: str):
    game_state["round"] += 1

    if user_move == "bomb":
        game_state["user_bomb_used"] = True
    if bot_move == "bomb":
        game_state["bot_bomb_used"] = True

    if game_state["round"] >= game_state["max_rounds"]:
        game_state["game_over"] = True


# -----------------------------
# ADK Agent (Tool Registry)
# -----------------------------
referee_agent = Agent(
    name="RPSPlusReferee",
    description="AI referee for Rock–Paper–Scissors–Plus",
    tools=[validate_move, resolve_round, update_game_state]
)

# -----------------------------
# Game Loop (CLI Simulation)
# -----------------------------
def play_game():
    print("Rock–Paper–Scissors–Plus")
    print("• Best of 3 rounds")
    print("• Moves: rock, paper, scissors, bomb")
    print("• Bomb beats all moves (once per player)")
    print("• Invalid input wastes the round")

    while not game_state["game_over"]:
        print(f"\n--- Round {game_state['round'] + 1} ---")
        user_input = input("Your move: ")

        validation = validate_move(user_input, "user")
        if not validation["valid"]:
            print(f"Invalid move: {validation['reason']}")
            game_state["round"] += 1
            continue

        user_move = validation["move"]

        bot_move = random.choice(
            ["rock", "paper", "scissors", "bomb"]
            if not game_state["bot_bomb_used"]
            else ["rock", "paper", "scissors"]
        )

        result = resolve_round(user_move, bot_move)
        update_game_state(user_move, bot_move)

        print(f"You played: {result['user_move']}")
        print(f"Bot played: {result['bot_move']}")
        print(f"Round Winner: {result['winner'].upper()}")

    print("\n=== Game Over ===")
    print(f"Final Score → You: {game_state['user_score']} | Bot: {game_state['bot_score']}")

    if game_state["user_score"] > game_state["bot_score"]:
        print("You win!")
    elif game_state["bot_score"] > game_state["user_score"]:
        print("Bot wins!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    play_game()
