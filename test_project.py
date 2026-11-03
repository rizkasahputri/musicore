import unittest
from models import SpotifyTrack
from analysis import (
    clean_text, 
    search_by_artist, 
    search_by_track, 
    filter_collaborations,
    get_top_n_tracks,
    calculate_avg_daily_streams_by_artist,
    compare_artist_popularity
)

class TestSpotifyProject(unittest.TestCase):
    def setUp(self):
        # Data dummy bervariasi untuk menguji semua kemungkinan
        self.data = [
            SpotifyTrack(1, "Blinding Lights", "The Weeknd", 1, "False", 4000, 400, 1, 0.4),
            SpotifyTrack(2, "Shape of You", "Ed Sheeran", 1, "false", 3500, 350, 2, 0.35),
            SpotifyTrack(3, "Starboy", "The Weeknd feat. Daft Punk", 2, "True", 2500, 250, 3, 0.25),
            SpotifyTrack(4, "Perfect", "Ed Sheeran", 1, "FALSE ", 3000, 300, 4, 0.3),
            SpotifyTrack(5, "Save Your Tears", "The Weeknd & Ariana Grande", 2, "TRUE", 2000, 200, 5, 0.2)
        ]
        self.empty_data = []

    # 1. TEST: TEXT UTILITIES (Manipulasi String)
    def test_clean_text_normal(self):
        self.assertEqual(clean_text("  HeLLo World  "), "hello world")
        self.assertEqual(clean_text("The Weeknd"), "the weeknd")

    def test_clean_text_edge_cases(self):
        self.assertEqual(clean_text(""), "") # String kosong
        self.assertEqual(clean_text("   "), "") # Hanya spasi
        self.assertEqual(clean_text("12345!@#"), "12345!@#") # Karakter spesial dan angka

    def test_clean_text_bad_input(self):
        self.assertEqual(clean_text(None), "none") # Tipe None
        self.assertEqual(clean_text(123), "123") # Tipe Integer (bukan string)
        self.assertEqual(clean_text(True), "true") # Tipe Boolean

    # 2. TEST: PENCARIAN (Artist & Track)
    def test_search_by_artist_exact_and_partial(self):
        # Pencarian persis sama (mengabaikan kapitalisasi)
        result_ed = search_by_artist(self.data, "ed SHEERAN")
        self.assertEqual(len(result_ed), 2)
        
        # Pencarian parsial
        result_weeknd = search_by_artist(self.data, "weeknd")
        self.assertEqual(len(result_weeknd), 3) # Memastikan kolaborasi juga terhitung

    def test_search_not_found(self):
        result = search_by_artist(self.data, "Taylor Swift")
        self.assertEqual(len(result), 0)

    def test_search_edge_cases(self):
        # Pencarian pada data kosong
        self.assertEqual(len(search_by_artist(self.empty_data, "Ed Sheeran")), 0)
        # Pencarian string kosong (seharusnya mengembalikan semua, karena "" ada di setiap string)
        self.assertEqual(len(search_by_artist(self.data, "")), 5)

    def test_search_by_track(self):
        result = search_by_track(self.data, "shape")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].artist, "Ed Sheeran")

    # 3. TEST: FILTER (Kolaborasi)
    def test_filter_collaborations(self):
        result = filter_collaborations(self.data)
        self.assertEqual(len(result), 2) # Hanya Starboy dan Save Your Tears
        
        # Pastikan data yang difilter benar-benar kolaborasi
        for r in result:
            self.assertTrue(clean_text(r.is_collaboration) == 'true')

    def test_filter_collaborations_empty(self):
        self.assertEqual(len(filter_collaborations(self.empty_data)), 0)

    # 4. TEST: SORTING (Top N Tracks)
    def test_get_top_n_tracks_normal(self):
        result = get_top_n_tracks(self.data, 3)
        self.assertEqual(len(result), 3)
        # Memastikan urutan dari streams terbesar ke terkecil
        self.assertEqual(result[0].track, "Blinding Lights") # 4000
        self.assertEqual(result[1].track, "Shape of You")    # 3500
        self.assertEqual(result[2].track, "Perfect")         # 3000

    def test_get_top_n_tracks_edge_cases(self):
        # Meminta N lebih besar dari jumlah data
        result = get_top_n_tracks(self.data, 10)
        self.assertEqual(len(result), 5) 
        
        # Meminta 0 data
        self.assertEqual(len(get_top_n_tracks(self.data, 0)), 0)

    # 5. TEST: KALKULASI ARITMATIKA (Rata-rata & Bandingkan)
    def test_calculate_avg_daily_streams(self):
        # Ed Sheeran memiliki 2 lagu: 350 + 300 = 650. Rata-rata = 325
        avg = calculate_avg_daily_streams_by_artist(self.data, "Ed Sheeran")
        self.assertEqual(avg, 325.0)

    def test_calculate_avg_daily_streams_not_found(self):
        avg = calculate_avg_daily_streams_by_artist(self.data, "Unknown")
        self.assertEqual(avg, 0.0)

    def test_compare_artist_popularity(self):
        # The Weeknd (3 lagu): 4000 + 2500 + 2000 = 8500
        # Ed Sheeran (2 lagu): 3500 + 3000 = 6500
        total_a, total_b = compare_artist_popularity(self.data, "the weeknd", "ed sheeran")
        self.assertEqual(total_a, 8500)
        self.assertEqual(total_b, 6500)

    def test_compare_artist_one_not_found(self):
        total_a, total_b = compare_artist_popularity(self.data, "Ed Sheeran", "Adele")
        self.assertEqual(total_a, 6500)
        self.assertEqual(total_b, 0) # Adele tidak ada

if __name__ == '__main__':
    unittest.main()
