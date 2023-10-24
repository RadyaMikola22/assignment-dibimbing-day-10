#Dag ini untuk ngeload data yang telah di ekstrak dan transformasi ke Spreadsheet

from datetime import datetime
import pytz
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.google.suite.hooks.sheets import GSheetsHook
from Postgres_to_Spreadsheet.lib.query_sql import query_sql

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 8, 1, 7, 0, 0, tzinfo=pytz.timezone('Asia/Jakarta')),
    'retries': 1,
}

#function untuk melakukan load ke spreadshet dari data yang sudah ada
def etl_to_spreadsheet(): 
    data_to_append = query_sql()
    google_sheet_hook = GSheetsHook(gcp_conn_id="dibimbing_gcp")
    google_sheet_hook.append_values(
        '<input google spreadsheet id>', '<input range sheet>', data_to_append
    )

with DAG(
    'ETL_to_Spreadsheet',    #Nama DAG
    default_args=default_args,
    schedule_interval='0 2 * * *',
    catchup=False,
) as dag:
    task = PythonOperator(      #Menggunakan PythonOperator
        task_id='tugas_dibimbing',
        python_callable=etl_to_spreadsheet
    )
