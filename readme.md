# Instruksi Assignment Day 10 ETL with Python #

## Instalasi ##
- Buat 4 folder (logs, dags, plugins, config) yang dibutuhkan untuk menjalankan docker-compose nya
- Buat dahulu imagenya dengan menjalankan kode di terminal yang dimana folder pathnya sudah berada di folder docker composenya berada seperti berikut:
===========
docker build -t airflow-dibimbing:1.0.0 . 
===========
- Kemudian buat kontainernya dengan menjalankan kode berikut
===========
docker-compose up -d
===========

## Login Airflow ##
- Setelah sudah terinstal, buka localhost8080 pada web yang ada
- Kemudian login 

## DAGs ##
- Terdapat 1 dag yang telah saya buat bernama ETL_to_Spreadsheet, dimana dag ini berfungsi untuk mengirimkan data ke spreadsheet yang sebelumnya telah dilakukan ekstrak dan transformasi data dari postgres sql pada script query_sql.py
- Dag ETL_to_Spreadsheet ini akan ter execute sesuai dengan schedule yang ditentukan. adapun schedulenya yaitu jam 2 pagi ('0 2 * * *) sesuai dengan perintah task assignmentnya

## Google Secret ##
- Jika ingin menjalankan task ETL_to_Spreadsheet, buat dahulu service accountnya, kemudian buat juga spreadsheet baru sebagai bahan uji cobanya
- Untuk membuat service account kunjungi web ini console.cloud.google.com

## Connection ##
- Terdapat 2 koneksi yang perlu ditambahkan pada airflownya terlebih dahulu agar DAG tersebut bisa berjalan yaitu:
    1. Koneksi ke Postgres
        - connection id = dibimbing_postgres
        - connection type = Postgres
        - Host = postgres
        - Schema = postgres
        - login = airflow
        - Password = <<Password>>
        - Port = 5432
        - Extra = {}

    2. Koneksi ke Google Spreadsheet
        - Connection id = dibimbing_gcp
        - Connection type = Google Cloud
        - Keyfile JSON = <<google secret.json>> file ini didapatkan dari membuat service account
        - Scopes = https://www.googleapis.com/auth/spreadsheets
        - Number of Retries = 5

## Keterangan Tambahan ##
### Query SQL ###
- Untuk ekstrak dan transformasi data dari postgresnya ada di file query_sql.py yang berada di folder tugas_dibimbing_etl\dags\Postgres_to_Spreadsheet\lib. Adapun hasil querynya dan datanya dijadikan fungsi sendiri yang bernama query_sql, kemudian di import ke DAG ETL_to_Spreadsheet sebagai data yang akan di load

### Database ###
- Untuk database postgres ada di folder tugas_dibimbing_etl\db dengan file bernama chinook
