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
