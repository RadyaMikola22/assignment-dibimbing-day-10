#file ini adalah untuk ekstrak dan transformasi data dari postgres dengan melakukan query yang sesuai

import json 
from airflow.providers.postgres.hooks.postgres import PostgresHook

def query_sql(): #fungsi query untuk ekstrak dan transformasi data sesuai kebutuhan
    postgres_hook = PostgresHook(postgres_conn_id='dibimbing_postgres')

    sql_query = """
    SELECT
        t.id AS trackid,
        t.name AS track,
        t.name AS name,
        al.title AS albumname,
        ar.name AS artistname,
        t.media_type_id AS mediatype,
        t.genre_id AS genreid,
        t.composer,
        t.milliseconds AS milliseconds,
        t.bytes,
        CAST(t.unit_price AS FLOAT) AS unitprice,
        CAST(t.milliseconds / 60000.0 AS FLOAT) AS durationminutes,
        CAST(CURRENT_TIMESTAMP(0) AT TIME ZONE 'Asia/Jakarta' AS VARCHAR) AS etl_timestamp,
        'Name' AS studentname
    FROM
        tracks AS t
    LEFT JOIN
        albums AS al ON al.id = t.album_id
    LEFT JOIN
        artists AS ar ON ar.id = al.artist_id
    LIMIT 1;
    """
    results = postgres_hook.get_records(sql=sql_query)
    data = json.dumps(results)
    data_load = json.loads(data)
    return data_load
