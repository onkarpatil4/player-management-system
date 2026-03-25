# player-management-system
# ⚽ Player Management System

A simple REST API project built using Python and Flask to manage player data.

---

## 🚀 Features
- Add Player
- View All Players
- Update Player Stats
- Delete Player

---

## 🛠 Tech Stack
- Python
- Flask
- SQLite
- REST API

---

## ▶️ How to Run

1. Install Flask:
   pip install flask

2. Run the app:
   python app.py

3. Open browser:
   http://127.0.0.1:5000/players

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|--------|---------|------------|
| POST | /add_player | Add new player |
| GET | /players | Get all players |
| PUT | /update_player/<id> | Update player |
| DELETE | /delete_player/<id> | Delete player |

---

## 💡 Example JSON

{
  "name": "Messi",
  "team": "Inter Miami",
  "goals": 20,
  "matches": 15
}

---

## 📷 Future Improvements
- Search player by name
- Top scorer feature
- GUI interface

---

## 👨‍💻 Author
Onkar Chandrakant Patil
