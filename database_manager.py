import sqlite3

class DatabaseManager:
    def __init__(self, db_name="reactor_simulation.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        query = """
        CREATE TABLE IF NOT EXISTS simulation_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            power_output REAL,
            coolant_temp REAL,
            pressure REAL,
            climate_factor REAL,
            risk_level REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def save_simulation(self, power_output, coolant_temp, pressure, climate_factor, risk_level):
        query = """
        INSERT INTO simulation_results (power_output, coolant_temp, pressure, climate_factor, risk_level)
        VALUES (?, ?, ?, ?, ?)
        """
        self.conn.execute(query, (power_output, coolant_temp, pressure, climate_factor, risk_level))
        self.conn.commit()

    def close(self):
        self.conn.close()
