import sys
from data_loader import load_data, FILE_NAME
from analysis import (
    search_by_artist, 
    search_by_track, 
    get_top_n_tracks, 
    calculate_avg_daily_streams_by_artist, 
    compare_artist_popularity
)

def print_aligned(records):
    if not records:
        print("Tidak ada data yang ditemukan.")
        return
    
    print(f"{'Peringkat':<10} | {'Judul':<35} | {'Artis':<25} | {'Total Streams':<15}")
    print("-" * 93)
    for r in records:
        track_name = r.track[:32] + "..." if len(r.track) > 35 else r.track
        artist_name = r.artist[:22] + "..." if len(r.artist) > 25 else r.artist
        print(f"{r.rank:<10} | {track_name:<35} | {artist_name:<25} | {r.spotify_streams_total:<15}")

def main():
    dataset = load_data(FILE_NAME)
    if not dataset:
        sys.exit("Gagal memuat dataset.")
        
    while True:
        print("\nMenu Utama Spotify 2025")
        print("1. Cari Lagu Berdasarkan Artis")
        print("2. Cari Lagu Berdasarkan Judul")
        print("3. Tampilkan Top N Lagu")
        print("4. Hitung Rata-rata Streams Harian Artis")
        print("5. Bandingkan Kepopuleran Dua Artis")
        print("6. Keluar")
        
        pilihan = input("Masukkan pilihan (1-6): ").strip()
        
        if pilihan == '1':
            artis = input("Masukkan nama artis: ").strip()
            if not artis:
                print("Input tidak valid. Nama artis tidak boleh kosong.")
                continue
            hasil = search_by_artist(dataset, artis)
            print_aligned(hasil)
            
        elif pilihan == '2':
            judul = input("Masukkan judul lagu: ").strip()
            if not judul:
                print("Input tidak valid. Judul lagu tidak boleh kosong.")
                continue
            hasil = search_by_track(dataset, judul)
            print_aligned(hasil)
            
        elif pilihan == '3':
            while True:
                try:
                    n = int(input("Masukkan jumlah lagu (N): "))
                    if n <= 0 or n > len(dataset):
                        print(f"Masukkan angka antara 1 dan {len(dataset)}.")
                    else:
                        break
                except ValueError:
                    print("Input tidak valid. Masukkan angka bulat.")
            hasil = get_top_n_tracks(dataset, n)
            print_aligned(hasil)
            
        elif pilihan == '4':
            artis = input("Masukkan nama artis: ").strip()
            if not artis:
                print("Input tidak valid. Nama artis tidak boleh kosong.")
                continue
            
            avg_daily = calculate_avg_daily_streams_by_artist(dataset, artis)
            
            if avg_daily > 0:
                print(f"Rata-rata streams harian untuk artis '{artis}': {avg_daily:,.2f}")
            else:
                print(f"Tidak ditemukan data untuk artis '{artis}'.")
                
        elif pilihan == '5':
            artis_a = input("Masukkan nama artis pertama (A): ").strip()
            artis_b = input("Masukkan nama artis kedua (B): ").strip()
            
            if not artis_a or not artis_b:
                print("Input tidak valid. Nama artis tidak boleh kosong.")
                continue
                
            total_a, total_b = compare_artist_popularity(dataset, artis_a, artis_b)
            
            print("\n--- Hasil Perbandingan Streams ---")
            print(f"Penyanyi A ({artis_a}): {total_a:,.0f} streams")
            print(f"Penyanyi B ({artis_b}): {total_b:,.0f} streams")
            
            if total_a > total_b:
                print(f"Kesimpulan: {artis_a} lebih populer berdasarkan total streams.")
            elif total_b > total_a:
                print(f"Kesimpulan: {artis_b} lebih populer berdasarkan total streams.")
            elif total_a == 0 and total_b == 0:
                print("Kedua artis tidak ditemukan di dalam dataset.")
            else:
                print("Kedua artis memiliki total streams yang sama kuat.")
                
        elif pilihan == '6':
            print("Program selesai.")
            break
            
        else:
            print("Pilihan tidak dikenal. Silakan pilih 1-6.")

if __name__ == "__main__":
    main()
