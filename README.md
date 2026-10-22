# Python Mini Projects: Tasks 2, 3 & 4

This repository contains three beginner-friendly Python projects.

## Requirements
- Python 3.8 or newer
- No third-party packages required

## Task 2 — Stock Portfolio Tracker
Run:
```bash
python task2_stock_portfolio/stock_portfolio.py
```
Enter stock symbols and quantities. Prices are stored in a hardcoded dictionary. The program calculates the total and can save holdings to a CSV file.

Example supported symbols: `AAPL`, `TSLA`, `MSFT`, `GOOGL`.

## Task 3 — JPG File Organizer
Run:
```bash
python task3_automation/organize_jpgs.py
```
The script asks for a source folder and moves `.jpg` and `.jpeg` files into a `jpg_files` subfolder. It does not overwrite files: duplicate destination names receive a numbered suffix.

## Task 4 — Rule-Based Chatbot
Run:
```bash
python task4_chatbot/chatbot.py
```
Try: `hello`, `how are you`, `help`, or `bye`.

## Notes
- Stock prices are sample hardcoded values for learning, not live market prices or investment advice.
- For Task 3, test with a sample folder first. Files are moved, not copied.
