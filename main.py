import sqlite3
import pandas as pd

class BusinessIntelligenceEngine:
    """
    Natural Language BI Engine
    Parses database schemas and facilitates structured SQL analytics execution.
    """
    def __init__(self, db_path=":memory:"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._setup_mock_data()

    def _setup_mock_data(self):
        self.cursor.execute("CREATE TABLE sales (id INTEGER, amount REAL, category TEXT)")
        self.cursor.executemany("INSERT INTO sales VALUES (?, ?, ?)", [
            (1, 150.0, "Electronics"),
            (2, 80.0, "Books"),
            (3, 300.0, "Electronics")
        ])
        self.conn.commit()

    def run_query(self, sql_query):
        print(f"Executing Query: {sql_query}")
        return pd.read_sql_query(sql_query, self.conn)

if __name__ == "__main__":
    bi = BusinessIntelligenceEngine()
    print("BI Engine initialized. Sample Sales Table Analysis:")
    print(bi.run_query("SELECT category, SUM(amount) FROM sales GROUP BY category"))
