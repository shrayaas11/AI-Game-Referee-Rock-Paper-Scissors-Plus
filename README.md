AI Game Referee – Rock–Paper–Scissors–Plus
Overview

This project implements a minimal AI referee chatbot for a Rock–Paper–Scissors–Plus game using Google ADK. The bot enforces game rules, validates user input, maintains game state across turns, and automatically ends the game after three rounds. The interaction is implemented as a CLI-based conversational loop.

Game Rules

The game is best of three rounds

Valid moves are: rock, paper, scissors, and bomb

Bomb can be used only once per player

Bomb beats all other moves

Bomb versus bomb results in a draw

Invalid input wastes the round

The game ends automatically after three rounds

State Model

The game state is maintained using an in-memory Python dictionary. This allows the system to persist information across turns without using external storage or databases.

The state includes:

Current round number

Maximum rounds (3)

User score and bot score

Bomb usage flags for both players

Game-over flag

This ensures that state does not live inside the prompt and remains deterministic.

Agent and Tool Design

A single Google ADK Agent is used as the orchestration boundary. Explicit tool functions are attached to the agent to handle validation, game logic, and state mutation.

Tools used:

validate_move: Validates the player’s move and enforces bomb usage rules

resolve_round: Determines the winner of each round based on game rules

update_game_state: Updates scores, round count, bomb usage, and game completion

This cleanly separates intent understanding, game logic, and state management.

Architecture Notes

Google ADK is used for agent definition and tool registration. Tools are implemented as plain Python functions to remain compatible with ADK version differences. The CLI loop simulates conversational turns without using UI frameworks or long-running servers.

Tradeoffs

Bot moves are randomly selected instead of strategically optimized

A single agent is used instead of multiple agents to keep the design minimal

CLI-based interaction is used instead of a chat UI, as permitted by the assignment

Future Improvements

With additional time, the system could be enhanced by:

Adding strategic bot behavior

Supporting more flexible natural language inputs

Writing unit tests for tools and game logic

Refactoring into a fully agent-driven conversational loop

How to Run

Install dependencies and run the file:

pip install google-adk
python rps_plus_referee.py

Output

For each round, the program displays:

Round number

User move and bot move

Round winner

At the end of the game, the final result is shown as User wins, Bot wins, or Draw.

Conclusion

This project satisfies all functional, logical, and technical requirements of the assignment and demonstrates clear state management, explicit tool usage, and conversational agent design.
