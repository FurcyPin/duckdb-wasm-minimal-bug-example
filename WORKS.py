import duckdb

conn = duckdb.connect(database="diff_without_index.db")

result = conn.sql("""SELECT * FROM sample_0 WHERE __SAMPLE_ID__ = '{"id":13008014}' LIMIT 1""")

result.show()

