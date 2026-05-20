# Python Mini-Toolkit

## Project Description
[cite_start]An interactive, menu-based command line toolkit containing five mini-applications designed to showcase foundational Python programming concepts[cite: 17, 57].

## Features of your Project
**Grade Calculator**: Prompts the user for a dynamic number of subjects, collects scores with boundary checks (0–100), and automatically averages scores to calculate academic standing and letter grades[cite: 19].
* [cite_start]**Even or Odd Checker**: A mathematical validator that uses the modulus operator to instantly check and identify number properties[cite: 19, 28].
* [cite_start]**Simple Quiz Game**: A 5-question general knowledge and coding trivia game that evaluates user answers dynamically and tracks your final score[cite: 19].
* [cite_start]**Number Guessing Game**: A logic-based game utilizing random generation, live countdowns, and limited attempts with helpful hints[cite: 19].
* [cite_start]**Budget Tracker**: A financial logging tool that lets users dynamically add income/expenses, view historical transactions in South African Rands (R), and monitor a real-time net balance dashboard[cite: 19].

## Python Concepts Used
* [cite_start]**Variables & Type Casting**: Converting raw string inputs to `int` and `float` metrics appropriately[cite: 21].
* [cite_start]**Control Flow**: Implementing `if/elif/else` conditional blocks, boolean expressions, and `while` / `for` loop controls[cite: 23, 24].
* [cite_start]**Data Structures**: Implementing a list of dictionaries to track multi-layered transaction records (type, category, amount)[cite: 26].
* [cite_start]**Modular Coding**: Separating core logic cleanly into functions inside a custom module (`helpers.py`) and importing it into the driver file[cite: 25, 26].
* **Error Handling**: Using structured `try/except` blocks to catch `ValueError` bugs and prevent crashes from bad user inputs.

## How to Run the Project
1. Clone this repository to your local machine.
2. Open your terminal or command prompt.
3. [cite_start]Navigate to the project directory: `cd python-mini-toolkit` [cite: 31]
4. [cite_start]Execute the application script: `python main.py` [cite: 32]

## Challenges Faced
* Structuring the input validation routines within infinite loops so that invalid entries or empty strings would re-prompt the user instead of breaking the terminal flow.
* Managing how complex variables and data structures (like the transaction logs library) cleanly passed through function scopes across separate files without creating circular dependencies.

## What you learned / Future improvements
* [cite_start]Learned how to effectively break down raw code into reusable functions, leverage Python's built-in modules (`time` and `random`), and implement clean multi-file software architecture[cite: 25, 26].
* Future improvement: Save user data locally using file inputs/outputs (like CSV or JSON files) so that budget logs persist across program restarts.

## Repository Structure

```text
python-mini-toolkit/
├── main.py
├── helpers.py
├── README.md
└── screenshots/
    └── folder_structure.png
