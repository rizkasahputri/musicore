# Final Exam Project: Intro to Computer Programming

**Nama:** [Rizka Sahputri]
**NIM:** [26121600020]
**Kelas:** CPro2

## 1. Informasi Dataset
*   **Nama Dataset:** `most_streamed_spotify_2025.csv`
*   **Link Kaggle:** `https://www.kaggle.com/datasets/kylefengkfeng209/most-streamed-spotify-songs-2025`
*   **Alasan memilih dataset:** Dataset ini memenuhi ketentuan ujian dengan jumlah baris sebanyak 730 baris dan tidak berisi informasi pribadi.
*   **Kolom yang digunakan:** `rank`, `track`, `artist`, `billed_artist_count`, `is_collaboration`, `spotify_streams_total`, `daily_streams`, `daily_streams_rank`, `daily_stream_share_pct`.
*   **Kolom yang tidak digunakan:** Saya tidak menggunakan kolom `wrapped_global_top10_rank` karena berisi cell kosong sebanyak 727 dari 730 baris. File `data_loader.py` mengabaikan kolom tersebut ketika membuat objek `SpotifyTrack` untuk mencegah masalah adanya data yang kosong.

## 2. Cara Menjalankan Program dan Test
*   **Untuk menjalankan main program:** Buka folder yang berisi python files tersebut dan buka terminal atau command prompt, kemudian jalankan perintah:
    ```bash
    python main.py
    ```
*   **Untuk menjalankan unit tests:** Pada folder yang sama, jalankan perintah:
    ```bash
    python -m unittest test_project.py
    ```
    *(Note: Pastikan menggunakan Python 3 dan hanya meng-install standard libraries. Tidak diperlukan pandas atau numpy).*

## 3. Program Features
1.  **Cari Lagu Berdasarkan Artis:** Memungkinkan user mengetik nama artis. Program membersihkan input (seperti case-sensitive dan kelebihan spasi) dan mengembalikan semua lagu dari artis tersebut menggunakan partial string matching.
2.  **Cari Lagu Berdasarkan Judul:** Memungkinkan user mengetik nama lagu untuk menemukan lagu spesifik menggunakan partial string matching yang mengabaikan huruf kapital (case-insensitive).
3.  **Top N Tracks:** Meminta user memasukkan angka (N) dan menampilkan N lagu dengan jumlah streams terbanyak. Pengurutan dilakukan menggunakan algoritma Bubble Sort manual berdasarkan total streams, tanpa bergantung pada fungsi bawaan `sorted()`.
4.  **Hitung Rata-rata Streams Harian Artis:** Menghitung rata-rata streams harian spesifik untuk artis yang dipilih dengan menjumlahkan data dari seluruh lagu artis lalu membaginya dengan jumlah lagu.
5.  **Bandingkan Kepopuleran Dua Artis:** Meminta input dua nama artis, menghitung total kumulatif streams atas semua lagu masing-masing artis, dan membandingkannya untuk menentukan siapa yang lebih populer di Spotify.

## 4. Batasan yang Diketahui
*   Algoritma Bubble Sort yang digunakan untuk fitur "Top N Lagu" memiliki kompleksitas waktu O(n^2). Walaupun berfungsi sempurna untuk dataset berisi 730 baris ini, algoritma ini tidak akan efisien untuk jutaan baris data.
*   Fitur pencarian bergantung pada pencocokan substring sederhana. Program tidak mendukung pencarian fleksibel untuk salah eja (misalnya, mengetik "Tylor" padahal seharusnya "Taylor" tidak akan menampilkan hasil pencarian).
*   User harus mengetik nama artis atau nama lagu selengkap mungkin agar program juga tidak membaca output selain yang diinginkan user. Misalnya, user mengetik "Bad" padahal user menginginkan "Bad Bunny", program akan menampilkan hasil apapun yang nama artisnya memiliki unsur "bad" seperti "Moy Bobadilla" dan "Beabadoobee".

## 5. Link Video Penjelasan
*   **Link YouTube Video:** [https://youtu.be/HsG_WPK5BlM]

## 6. Konsep Python yang Digunakan

| Konsep | File Location | Contoh Function/Line |
| :--- | :--- | :--- |
| **Variables dan data types** | `data_loader.py` dan `models.py` | Mendefinisikan `FILE_NAME` sebagai string constant dalam huruf kapital. Mengubah data CSV menjadi `int`, `float`, and `str`. |
| **Input dan output** | `main.py` | Menggunakan `input()` di dalam `main()` untuk pilihan menu dan `print_aligned()` dengan f-strings untuk column formatting. |
| **Operators** | `analysis.py` dan `main.py` | Menggunakan `/` dan `+` untuk melakukan perhitungan. Menggunakan `or`, `<=`, `>`, dan `==` untuk perbandingan. |
| **Conditional statements** | `main.py` | Menggunakan `if`, `elif`, and `else` di dalam `while True` loop untuk menu options dan invalid inputs. |
| **Loop statements** | `analysis.py` | Menggunakan `for` loops di fungsi `get_top_n_tracks()` untuk Bubble Sort dan `while True` loop di dalam `main.py`. |
| **Functions** | `semua file` | Dapat ditemukan functions di semua file, seperti salah satu contoh `compare_artist_popularity(records, artist_a, artist_b)`. |
| **Lists** | `analysis.py` | Membuat list `results` baru di dalam fungsi pencarian dan menggunakan list slicing `sorted_records[:n]` untuk mengembalikan nilai Top N. |
| **String manipulation** | `analysis.py` | Membuat `clean_text()` using `.strip().lower()` untuk melakukan pencocokan yang mengabaikan case-insensitive dan spasi yang berlebih. |
| **Classes (OOP)** | `models.py` | Membuat class `SpotifyTrack` dengan `__init__` and `__str__` untuk menyimpan dan merepresentasikan setiap baris di CSV. |
| **Unit tests** | `test_project.py` | Menulis class `TestSpotifyProject` dengan 15 metode untuk menguji normal input, missing data (`None`), dan empty lists. |
