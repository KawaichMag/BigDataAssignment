import polars as pl
import pandas as pd

CHUNK_SIZE = 100000

my_users = pl.read_csv("my_checkins_anonymized.tsv", separator="\t")

checkins_chunks = pd.read_csv(
    "checkins_anonymized.txt",
    sep="\t",
    chunksize=CHUNK_SIZE,
    header=None,
    names=["userid", "venue_id", "utc_time", "timezone_offset_mins"],
)

processed_chunks = []

for idx, pd_chunk in enumerate(checkins_chunks):
    print(f"Processing chunk #{idx}")
    chunk = pl.from_pandas(pd_chunk)

    processed_chunk = chunk.join(my_users, on="userid", how="semi")

    processed_chunks.append(processed_chunk)

if processed_chunks:
    final_df: pl.DataFrame = pl.concat(processed_chunks)
    print("Done!")
    print(final_df.head())
    final_df.write_csv("my_checkins_anonymized.tsv", separator="\t")
