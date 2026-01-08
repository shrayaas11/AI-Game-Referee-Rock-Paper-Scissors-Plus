Overview

This project implements a minimal AI referee chatbot for a Rock–Paper–Scissors–Plus game using Google ADK.
The bot enforces game rules, tracks state across turns, validates inputs, and automatically ends the game after three rounds.

The game runs in a simple CLI conversational loop, as permitted by the assignment constraints.

Game Rules

Best of 3 rounds

Valid moves:
1.rock
2.paper
3.scissors
4.bomb (can be used once per player)

bomb beats all other moves

bomb vs bomb → draw

Invalid input wastes the round

Game ends automatically after 3 rounds

State Model

The game state is stored in an in-memory Python dictionary to ensure persistence across turns without using external storage.

Tracked state includes:

Current round number

Maximum rounds (3)

User score and bot score

Bomb usage flags for user and bot

Game-over flag

This ensures that state does not live in the prompt, satisfying the technical constraints.

Agent & Tool Design

A single Google ADK Agent is used as the orchestration boundary.

Explicit Tools

The following functions are registered as explicit tools on the agent:

validate_move
Validates player input and enforces the one-time bomb usage rule.

resolve_round
Applies game logic and determines the winner of each round.

update_game_state
Mutates persistent state (round count, bomb usage, and game termination).

These tools clearly separate:

Intent understanding (what move was attempted)

Game logic (who wins the round)

State mutation (updating scores and rounds)

Architecture Notes

Google ADK is used for agent definition and tool registration.

Tools are implemented as plain Python callables due to version-level ADK API differences, while still remaining explicit and agent-attached.

The CLI loop simulates conversational turns without relying on UI frameworks or servers.

This design prioritizes correctness, clarity, and determinism over UI polish.

Tradeoffs

Bot move selection is random rather than strategic to keep logic minimal.

A single agent is used instead of multiple agents for simplicity.

CLI interaction is used instead of a chat UI, as allowed by the assignment.

Future Improvements

With more time, the following could be added:

Strategic bot behavior instead of random moves

Natural language input handling

Unit tests for tool functions

A fully agent-driven conversational loop

How to Run
pip install google-adk
python rps_plus_referee.py

Final Output

The program provides:

Round number

Moves played by user and bot

Round winner

Final result: User wins / Bot wins / Draw
