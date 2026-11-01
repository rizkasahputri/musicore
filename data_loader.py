import csv
import os
from models import SpotifyTrack

# Variabel konstan ditulis dengan huruf kapital
FILE_NAME = "most_streamed_spotify_2025.csv"

def load_data(file_path):
    records = []
    skipped_rows = 0

    if not os.path.exists(file_path):
        print(f"Error: File {file_path} tidak ditemukan.")
        return records

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            try:
                # Memvalidasi dan membuat objek.
                # Kolom 'wrapped_global_top10_rank' diabaikan karena banyak yang kosong.
                track = SpotifyTrack(
                    rank=row['rank'],
                    track=row['track'],
                    artist=row['artist'],
                    billed_artist=row['billed_artist_count'],
                    is_collab=row['is_collaboration'],
                    total_streams=row['spotify_streams_total'],
                    daily_streams=row['daily_streams'],
                    daily_rank=row['daily_streams_rank'],
                    daily_share=row['daily_stream_share_pct']
                )
                records.append(track)
            
            except (ValueError, KeyError, TypeError):
                # Baris yang tidak dapat dibaca dilewati dan dihitung
                skipped_rows += 1

    # Mencetak jumlah rekaman yang berhasil dimuat dan dilewati
    print(f"Berhasil memuat {len(records)} baris data.")
    if skipped_rows > 0:
        print(f"Melewati {skipped_rows} baris data yang rusak atau tidak lengkap.")

    return records

# Blok uji coba sementara
if __name__ == "__main__":
    dataset = load_data(FILE_NAME)
    if dataset:
        print("Contoh data pertama:")
        print(dataset[0])
