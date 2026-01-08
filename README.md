AI Game Referee – Rock–Paper–Scissors–Plus
Overview

This project implements a minimal AI referee chatbot for a Rock–Paper–Scissors–Plus game using Google ADK. The bot enforces game rules, tracks state across turns, validates inputs, and automatically ends the game after three rounds.

The game runs in a simple CLI conversational loop, as permitted by the assignment constraints.

Game Rules

Best of 3 rounds

Valid moves:

rock

paper

scissors

bomb (can be used once per player)

bomb beats all other moves

bomb vs bomb results in a draw

Invalid input wastes the round

The game ends automatically after 3 rounds

State Model

The game state is stored in an in-memory Python dictionary to ensure persistence across turns without using external storage.

The state tracks:

Current round number

Maximum number of rounds (3)

User score and bot score

Bomb usage flags for both user and bot

Game-over flag

This ensures that state does not live in the prompt, satisfying the technical constraints.

Agent and Tool Design

A single Google ADK Agent is used as the orchestration boundary.

Explicit Tools

The following functions are registered as explicit tools on the agent:

validate_move
Validates player input and enforces the one-time bomb usage rule.

resolve_round
Applies game logic and determines the winner of each round.

update_game_state
Updates persistent state including round count, bomb usage, and game termination.

This design clearly separates:

Intent understanding (what move the user attempted)

Game logic (who won the round)

State mutation (updating scores and rounds)

Architecture Notes

Google ADK is used for agent definition and tool registration.

Tools are implemented as plain Python callables to remain compatible with ADK version differences.

The CLI loop simulates conversational turns without relying on UI frameworks or servers.

This approach prioritizes correctness, clarity, and determinism over UI polish.

Tradeoffs

Bot move selection is random rather than strategic to keep the logic minimal.

A single agent is used instead of multiple agents for simplicity.

CLI-based interaction is used instead of a chat UI, as allowed by the assignment.

Future Improvements

With more time, the following enhancements could be made:

Strategic bot decision-making

Natural language input handling

Unit tests for game logic and tools

A fully agent-driven conversational loop

How to Run
pip install google-adk
python rps_plus_referee.py

Output

The program provides:

Round number

Moves played by the user and the bot

Round winner

Final result: User wins, Bot wins, or Draw

Conclusion

This submission satisfies all functional, logical, and technical requirements outlined in the assignment and demonstrates clear state management, explicit tool usage, and conversational agent design.
