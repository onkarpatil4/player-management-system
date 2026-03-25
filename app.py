from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Create database and table
def init_db():
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            team TEXT,
            goals INTEGER,
            matches INTEGER
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Add player
@app.route('/add_player', methods=['POST'])
def add_player():
    data = request.json
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO players (name, team, goals, matches) VALUES (?, ?, ?, ?)",
                   (data['name'], data['team'], data['goals'], data['matches']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Player added successfully"})

# Get all players
@app.route('/players', methods=['GET'])
def get_players():
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM players")
    rows = cursor.fetchall()
    conn.close()

    players = []
    for row in rows:
        players.append({
            "id": row[0],
            "name": row[1],
            "team": row[2],
            "goals": row[3],
            "matches": row[4]
        })

    return jsonify(players)

# Update player
@app.route('/update_player/<int:id>', methods=['PUT'])
def update_player(id):
    data = request.json
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE players SET goals=?, matches=? WHERE id=?",
                   (data['goals'], data['matches'], id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Player updated"})

# Delete player
@app.route('/delete_player/<int:id>', methods=['DELETE'])
def delete_player(id):
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM players WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Player deleted"})

if __name__ == '__main__':
    app.run(debug=True)
