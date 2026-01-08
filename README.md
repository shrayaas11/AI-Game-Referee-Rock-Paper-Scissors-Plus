This project implements a stateful conversational game referee for Rock–Paper–Scissors–Plus using Google ADK. A single ADK agent is used as the orchestration boundary, with explicit Python tool functions attached for move validation, round resolution, and game state mutation. Persistent game state is maintained in memory to track rounds, scores, and one-time bomb usage, ensuring that state does not reside in the prompt. The system operates in a CLI-based conversational loop, enforces all game constraints deterministically, handles invalid inputs gracefully, and terminates automatically after three rounds without relying on external APIs, databases, UI frameworks, or long-running services.


How to Run

Install dependencies and run the file:

pip install google-adk
python rps_plus_referee.py
