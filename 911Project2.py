import duckdb
df = duckdb.read_csv('estimated_crimes_1979_2019.csv', header=True)
df.to_parquet('NEWYearlyCrime.parquet')
