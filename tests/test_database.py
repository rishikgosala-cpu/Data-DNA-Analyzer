import sys
from pathlib import Path
import unittest

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

import database


class DatabaseConnectionTests(unittest.TestCase):
    def test_get_connection_returns_a_working_connection(self):
        conn = database.get_connection()
        try:
            row = conn.execute("SELECT 1").fetchone()
            self.assertEqual(row[0], 1)
        finally:
            conn.close()


if __name__ == "__main__":
    unittest.main()
