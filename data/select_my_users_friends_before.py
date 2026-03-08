import polars as pl
import pandas as pd

CHUNK_SIZE = 100000

my_users = pl.read_csv("my_users.csv")

checkins_chunks = pd.read_csv(
    "friendship_before_old.txt",
    sep="\t",
    chunksize=CHUNK_SIZE,
    header=None,
    names=["user_id", "friend_id"],
)

processed_chunks = []

for idx, pd_chunk in enumerate(checkins_chunks):
    print(f"Processing chunk #{idx}")
    chunk = pl.from_pandas(pd_chunk)

    processed_chunk = chunk.filter(
        pl.col("user_id").is_in(my_users.get_column("userid").implode())
        & pl.col("friend_id").is_in(my_users.get_column("userid").implode())
    )

    processed_chunks.append(processed_chunk)

if processed_chunks:
    final_df: pl.DataFrame = pl.concat(processed_chunks)
    print("Done!")
    print(final_df.head())
    final_df.write_csv("my_frienship_before.tsv", separator="\t")
