# Helper function untuk manipulasi string
def clean_text(text):
    """Membersihkan teks dengan menghapus spasi awal/akhir dan mengubah ke huruf kecil."""
    return str(text).strip().lower()

def search_by_artist(records, artist_name):
    """
    Mencari lagu berdasarkan nama artis. 
    Mengabaikan huruf kapital dan spasi berlebih.
    """
    results = []
    target = clean_text(artist_name)
    
    for record in records:
        # Pengecekan string menggunakan in untuk pencarian parsial
        if target in clean_text(record.artist):
            results.append(record)
            
    return results

def search_by_track(records, track_name):
    results = []
    target = clean_text(track_name)
    for record in records:
        if target in clean_text(record.track):
            results.append(record)
    return results

def filter_collaborations(records):
    """Memfilter lagu-lagu yang merupakan hasil kolaborasi."""
    results = []
    for record in records:
        # Asumsi is_collaboration bernilai string 'True'/'False' dari CSV
        if clean_text(record.is_collaboration) == 'true':
            results.append(record)
    return results

def get_top_n_tracks(records, n):
    """
    Mengambil N lagu dengan total streams terbanyak.
    Menggunakan algoritma Bubble Sort manual karena dilarang menggunakan sorted().
    """
    # Membuat salinan list agar tidak mengubah urutan data asli
    sorted_records = records[:]
    length = len(sorted_records)
    
    # Looping manual untuk pengurutan descending berdasarkan total streams
    for i in range(length):
        for j in range(0, length - i - 1):
            if sorted_records[j].spotify_streams_total < sorted_records[j + 1].spotify_streams_total:
                # Menukar posisi elemen
                sorted_records[j], sorted_records[j + 1] = sorted_records[j + 1], sorted_records[j]
                
    # Menggunakan slicing untuk memotong list sesuai jumlah N
    return sorted_records[:n]

def calculate_avg_daily_streams_by_artist(records, artist_name):
    artist_records = search_by_artist(records, artist_name)
    if not artist_records:
        return 0.0
    total_daily_streams = sum(r.daily_streams for r in artist_records)
    return total_daily_streams / len(artist_records)

def compare_artist_popularity(records, artist_a, artist_b):
    records_a = search_by_artist(records, artist_a)
    records_b = search_by_artist(records, artist_b)
    total_a = sum(r.spotify_streams_total for r in records_a)
    total_b = sum(r.spotify_streams_total for r in records_b)
    return total_a, total_b
