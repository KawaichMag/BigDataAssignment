import time

import polars as pl

uri = "postgresql://postgres:1234@localhost:5432/foursquaredb"


def ingest_tsv_to_postgres(file_path, table_name):
    start = time.time()

    df = pl.read_csv(file_path, separator="\t", has_header=True)

    if "userid" in df.columns:
        df = df.rename({"userid": "user_id"})
        df = df.with_columns(
            [
                pl.col("user_id").cast(pl.Int32),
                pl.col("timezone_offset_mins").cast(pl.Int32),
            ]
        )

    if "user_id" in df.columns and "friend_id" in df.columns:
        df = df.with_columns(
            [
                pl.col("user_id").cast(pl.Int32),
                pl.col("friend_id").cast(pl.Int32),
            ]
        )

    print(df.columns)

    if "utc_time" in df.columns:
        print("utc_time detected. Reformatting to datetime..")
        df = df.with_columns(
            pl.col("utc_time").str.to_datetime(
                "%a %b %d %H:%M:%S +0000 %Y", strict=False
            )
        )
        print(df.head())

        df = df.drop_nulls(subset=["utc_time"])

    df.write_database(
        table_name=table_name, connection=uri, if_table_exists="append", engine="adbc"
    )
    print("Done!")
    print(f"Time consumed: {time.time() - start}s")


# ingest_tsv_to_postgres("./data/my_POIs.tsv", "pois")
# ingest_tsv_to_postgres("./data/my_checkins_anonymized.tsv", "checkins")
ingest_tsv_to_postgres("./data/my_frienship_before.tsv", "friendship_before")
ingest_tsv_to_postgres("./data/my_frienship_after.tsv", "friendship_after")
