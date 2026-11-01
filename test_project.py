import unittest
from models import SpotifyTrack
from analysis import search_by_artist, clean_text, filter_collaborations

class TestAnalysis(unittest.TestCase):
    def setUp(self):
        # Menyediakan data dummy untuk pengujian
        self.data = [
            SpotifyTrack(1, "Song A", "Artist One", 1, "False", 1000, 100, 1, 0.1),
            SpotifyTrack(2, "Song B", "Artist Two", 2, "True", 2000, 200, 2, 0.2),
            SpotifyTrack(3, "Song C", "Artist One feat. X", 2, "True", 1500, 150, 3, 0.15)
        ]

    # 1. Uji kondisi normal untuk manipulasi teks
    def test_clean_text_normal(self):
        self.assertEqual(clean_text("  HeLLo  "), "hello")

    # 2. Uji penanganan input yang buruk (tipe None)
    def test_clean_text_bad_input(self):
        self.assertEqual(clean_text(None), "none")

    # 3. Uji kondisi normal untuk fungsi pencarian
    def test_search_by_artist_normal(self):
        result = search_by_artist(self.data, "Artist One")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].track, "Song A")

    # 4. Uji kasus data tidak ditemukan
    def test_search_by_artist_not_found(self):
        result = search_by_artist(self.data, "Unknown Artist")
        self.assertEqual(len(result), 0)

    # 5. Uji kondisi batas (list kosong) pada fungsi filter
    def test_filter_collaborations_edge_case(self):
        empty_list = []
        result = filter_collaborations(empty_list)
        self.assertEqual(len(result), 0)

if __name__ == '__main__':
    unittest.main()
