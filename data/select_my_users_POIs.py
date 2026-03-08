import polars as pl
import pandas as pd

CHUNK_SIZE = 100000

my_users_checkins = pl.read_csv("my_checkins_anonymized.tsv", separator="\t")
my_users_venues = my_users_checkins.get_column("venue_id").implode()
del my_users_checkins

checkins_chunks = pd.read_csv(
    "POIs.txt",
    sep="\t",
    chunksize=CHUNK_SIZE,
    header=None,
    names=["venue_id", "latitude", "longitude", "category", "country"],
)

processed_chunks = []

for idx, pd_chunk in enumerate(checkins_chunks):
    print(f"Processing chunk #{idx}")
    chunk = pl.from_pandas(pd_chunk)

    processed_chunk = chunk.filter(pl.col("venue_id").is_in(my_users_venues))

    processed_chunks.append(processed_chunk)

if processed_chunks:
    final_df: pl.DataFrame = pl.concat(processed_chunks)
    print("Done!")
    print(final_df.head())
    final_df.write_csv("my_POIs.tsv", separator="\t")
