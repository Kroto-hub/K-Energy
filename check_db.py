import sqlite3

conn = sqlite3.connect("data/k_energy.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

print("=== 数据库中的表 ===")
for t in tables:
    table_name = t[0]
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cursor.fetchone()[0]
    print(f"  {table_name}: {count} 条记录")

print()

for t in tables:
    table_name = t[0]
    if table_name == "alembic_version":
        continue
    cursor.execute(f"SELECT * FROM {table_name} LIMIT 3")
    rows = cursor.fetchall()
    if not rows:
        print(f"--- {table_name} (空) ---")
        continue
    print(f"--- {table_name} ---")
    desc = cursor.description or []
    col_names = [d[0] for d in desc]
    for row in rows:
        print("  " + " | ".join(f"{col_names[i]}={row[i]}" for i in range(min(len(col_names), len(row)))))
    print()

conn.close()
