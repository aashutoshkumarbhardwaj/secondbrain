import sqlite3, pathlib

DB_PATH = pathlib.Path("/root/secondbrain/jarvis_brain.db")

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS important_emails (
                msg_id TEXT PRIMARY KEY,
                sender TEXT,
                subject TEXT,
                received_at TEXT,
                category TEXT,
                logged_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)

def log_email(msg_id: str, sender: str, subject: str, received_at: str, category: str) -> bool:
    init_db()
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute(
            "INSERT OR IGNORE INTO important_emails (msg_id, sender, subject, received_at, category) VALUES (?, ?, ?, ?, ?)",
            (msg_id, sender, subject, received_at, category)
        )
        return cur.rowcount > 0

if __name__ == "__main__":
    init_db()
    print(f"jarvis_brain.db ready at {DB_PATH}")
