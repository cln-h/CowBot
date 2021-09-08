import sqlite3

class RosterChannel:
    """SQL model for roster channel"""

    def add(server_id, channel_id):
        """Adds a new roster channel for a given server"""

        conn = sqlite3.connect('cowbot.db')
        c = conn.cursor()

        c.execute("""
            INSERT INTO roster_channel (channel_id, server_id)
            VALUES (:channel_id, :server_id)
            """, {'channel_id': channel_id, 'server_id': server_id})
        
        conn.commit()
        conn.close()

    def update(id, channel_id):
        """Updates a discrod server's roster channel id"""

        conn = sqlite3.connect('cowbot.db')
        c = conn.cursor()

        c.execute("""
            UPDATE roster_channel
            SET channel_id = :channel_id
            WHERE id = :id
            """, {'channel_id': channel_id, 'id': id})

        conn.commit()
        conn.close()

    def get(server_id):
        """Retrieves and returns a servers roster channel id. If not found returns undefined."""

        conn = sqlite3.connect('cowbot.db')
        c = conn.cursor()

        c.execute("""
            SELECT channel_id
            FROM roster_channel
            WHERE server_id = :server_id
            """, {'server_id': server_id})

        conn.commit()
        conn.close()
