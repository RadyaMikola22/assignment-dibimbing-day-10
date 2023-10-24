### Instruksi Assigment Day 10 ETL Mochamad Ananda Radya Mikola ###

### Langkah-langkah untuk mengeopreasikan DAG ke airflow dengan docker ###
# Instalasi
- sudah tersedia 4 folder yang dibutuhkan untuk instal docker-compose nya
- buat dahulu imagenya dengan kode sebagai berikut
===========
docker build -t airflow-dibimbing:1.0.0 . 
===========
- kemudian buat kontainernya, ketik di terminal yang dimana folder pathnya sudah berada di folder docker composenya berada seperti berikut:
===========
docker-compose up -d
===========

# Login Airflow 
- setelah sudah terinstal, buka localhost8080 pada web yang ada
- kemudian login 

# DAGs
- terdapat 1 dag yang telah saya buat bernama ETL_to_Spreadsheet, dimana dag ini berfungsi untuk mengirimkan data ke spreadsheet yang sebelumnya telah dilakukan ekstrak dan transformasi data dari postgres sql

- Dag ETL_to_Spreadsheet ini akan ter execute sesuai dengan schedule yang ditentukan. adapun schedulenya yaitu jam 2 pagi ('0 2 * * *) sesuai dengan perintah mas Tegar sebagai task assignment

# Connection
- terdapat 2 koneksi yang dihubungkan terlebih dahulu agar DAG tersebut bisa berjalan yaitu:
    1. Koneksi ke Postgres
        connection id = dibimbing_postgres
        connection type = Postgres
        Host = postgres
        Schema = postgres
        login = airflow
        Password = <<Password>>
        Port = 5432
        Extra = {}

    2. Koneksi ke Google Spreadsheet
        connection id = dibimbing_gcp
        connection type = Postgres
        Keyfile JSON = <<google secret.json>>
        Scopes = https://www.googleapis.com/auth/spreadsheets
        Number of Retries = 5


### Keterangan Tambahan ###
# Query SQL
- untuk ekstrak dan transformasi data dari postgresnya ada di file query_sql.py yang berada di folder tugas_dibimbing_etl\dags\Postgres_to_Spreadsheet\lib. Adapun hasil querynya dan datanya dijadikan fungsi sendiri yang bernama query_sql, kemudian di import ke DAG ETL_to_Spreadsheet sebagai data yang akan di load

# Database
- untuk database postgres ada di folder tugas_dibimbing_etl\db dengan file bernama chinook

# Note dari saya pribadi
- Sebelumnya, terimakasih banyak mas Tegar atas tugasnya. Bagi saya, tugasnya sangat menantang sekali yang awalnya sempat bingung banget karena ETL nya ga berhasil terus ke Spreadsheetnya. Hingga pada akhirnya bisa setelah melihat berulang kali video rekamannya, googling juga, dan melihat pertanyaan dan jawaban yang ada di group :). Sejujurnya saya agak malu kalau bertanya di group (ini kekurangan saya).

- Mungkin pembuatan dag, query, atau code saya masih kurang sempurna atau mungkin ada cara yang lebih baik dan rapih lagi untuk melakukan ETLnya. Pesan saya, mungkin bisa diadakan extra class lagi jika mas Tegar berkenan dan juga jika kang rakhmat memfasilitasinya terkait cara mengerjakan task assigment ini dengan sempurna oleh mas Tegar.

- Untuk load ke sheet 'Production' nya saya kemungkinan telat dari deadline ya, karena baru ke load nanti jam 2 pagi sesuai arahan mas Tegar. Maaf sebelumnya karena baru hari minggu ini (h-1 deadline) saya mengerjakan tugasnya, tetapi untuk pengumpulan folder ini ke LMS saya tidak melewati batas deadlinenya :). Terimakasih mas.
