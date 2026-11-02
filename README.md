# Final Exam Project: Intro to Computer Programming

**Student Name:** [Nama Anda]
**Class:** CPro2
**Date:** [3 November 2026]

## 1. Dataset Information
*   **Dataset Name:** `most_streamed_spotify_2025.csv`
*   **Kaggle Link:** `https://www.kaggle.com/datasets/kylefengkfeng209/most-streamed-spotify-songs-2025`
*   **Why I chose this dataset:** I chose this dataset because music streaming data is engaging and highly relatable. It perfectly meets the exam requirements with exactly 730 rows (between 200 and 2,000) and contains no private personal information.
*   **Columns Used:** `rank`, `track`, `artist`, `billed_artist_count`, `is_collaboration`, `spotify_streams_total`, `daily_streams`, `daily_streams_rank`, `daily_stream_share_pct`.
*   **Columns Skipped:** I skipped the `wrapped_global_top10_rank` column because it contains blank cells for 727 out of 730 rows. My `data_loader.py` is designed to ignore this column entirely when constructing the `SpotifyTrack` object to prevent missing data issues.

## 2. How to Run the Program and Tests
*   **To run the main program:** Open your terminal or command prompt, navigate to the folder containing the python files, and execute:
    ```bash
    python main.py
    ```
*   **To run the unit tests:** In the same folder, execute the following command to run all 5 unit tests:
    ```bash
    python -m unittest test_project.py
    ```
    *(Note: Ensure you are using Python 3 and have only standard libraries installed. No pandas or numpy are required).*

## 3. Program Features
1.  **Search Track by Artist:** Allows the user to type an artist's name. The program cleans the input (lowercasing, stripping spaces) and returns all tracks by that artist using partial string matching.
2.  **Top N Tracks:** Asks the user for a number (N) and displays the top N most streamed tracks. The sorting is done using a manual Bubble Sort algorithm based on total streams, without relying on the built-in `sorted()` function.
3.  **Calculate Average Streams:** Iterates through all loaded tracks, calculates the cumulative total streams, and divides by the total number of tracks to display the global average stream count.

## 4. Known Limitations
*   The Bubble Sort algorithm used for the "Top N Tracks" feature has a time complexity of O(n^2). While it works perfectly for this dataset of 730 rows, it would be inefficient for millions of rows.
*   The search feature relies on simple substring matching. It does not support fuzzy matching for misspellings (e.g., typing "Tylor" instead of "Taylor" will yield no results).

## 5. Video Explanation Link
*   **YouTube Video Link:** [Masukkan URL video YouTube Unlisted Anda di sini]

## 6. Python Concepts Applied (Table)

| Concept | File Location | Function / Line Example |
| :--- | :--- | :--- |
| **Variables and data types** | `data_loader.py` | Defined `FILE_NAME` as a string constant in capital letters. Converted CSV data to `int`, `float`, and `str`. |
| **Input and output** | `main.py` | Used `input()` inside `main()` for menu choices and `print_aligned()` with f-strings for column formatting. |
| **Operators** | `main.py` | Calculated `avg_streams = total_streams / len(dataset)`. Used `or`, `<=`, and `>` in the Top N validation. |
| **Conditional statements** | `main.py` | Used `if`, `elif`, and `else` inside the `while True` loop to handle the 4 menu options and invalid inputs. |
| **Loop statements** | `analysis.py` | Used nested `for` loops in `get_top_n_tracks()` for Bubble Sort, and a `while True` loop in `main.py`. |
| **Functions** | `analysis.py` | Created `search_by_artist(records, artist_name)` which takes parameters and returns a results list. |
| **Lists** | `analysis.py` | Built a new `results` list in search, and used list slicing `sorted_records[:n]` to return the Top N. |
| **String manipulation** | `analysis.py` | Created `clean_text()` using `.strip().lower()` to ensure case-insensitive and space-free matching. |
| **Classes (OOP - Bonus)** | `models.py` | Created the `SpotifyTrack` class with `__init__` and `__str__` to store and represent each record. |
| **Unit tests** | `test_project.py` | Wrote a `TestAnalysis` class with 5 methods checking normal input, missing data (`None`), and empty lists. |
