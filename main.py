import sys
from data_loader import load_data, FILE_NAME
from analysis import search_by_artist, filter_collaborations, get_top_n_tracks

def print_aligned(records):
    """Mencetak data dalam kolom yang sejajar menggunakan f-strings."""
    if not records:
        print("Tidak ada data yang ditemukan.")
        return
    
    # Menampilkan format header dengan lebar kolom tetap
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
        print("2. Tampilkan Top N Lagu")
        print("3. Hitung Rata-rata Streams")
        print("4. Keluar")
        
        pilihan = input("Masukkan pilihan (1-4): ").strip()
        
        if pilihan == '1':
            artis = input("Masukkan nama artis: ").strip()
            if not artis:
                print("Input tidak valid. Nama artis tidak boleh kosong.")
                continue
            hasil = search_by_artist(dataset, artis)
            print_aligned(hasil)
            
        elif pilihan == '2':
            while True:
                try:
                    n = int(input("Masukkan jumlah lagu (N): "))
                    # Menggunakan operator kondisional 'or' dan relasional '<='
                    if n <= 0 or n > len(dataset):
                        print(f"Masukkan angka antara 1 dan {len(dataset)}.")
                    else:
                        break
                except ValueError:
                    print("Input tidak valid. Masukkan angka bulat.")
            hasil = get_top_n_tracks(dataset, n)
            print_aligned(hasil)
            
        elif pilihan == '3':
            # Memenuhi syarat penggunaan operator aritmatika untuk menghitung nilai turunan
            total_streams = sum(r.spotify_streams_total for r in dataset)
            avg_streams = total_streams / len(dataset) if len(dataset) > 0 else 0
            print(f"Rata-rata Streams Keseluruhan: {avg_streams:,.2f}")
            
        elif pilihan == '4':
            print("Program selesai.")
            break
            
        else:
            print("Pilihan tidak dikenal. Silakan pilih 1-4.")

if __name__ == "__main__":
    main()
