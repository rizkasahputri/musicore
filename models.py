class SpotifyTrack:
    def __init__(self, rank, track, artist, billed_artist, is_collab, total_streams, daily_streams, daily_rank, daily_share):
        self.rank = int(rank)
        self.track = str(track).strip()
        self.artist = str(artist).strip()
        self.billed_artist_count = int(billed_artist)
        self.is_collaboration = str(is_collab).strip()
        self.spotify_streams_total = int(total_streams)
        self.daily_streams = int(daily_streams)
        self.daily_streams_rank = int(daily_rank)
        self.daily_stream_share_pct = float(daily_share)

    def __str__(self):
        return f"{self.rank}. {self.track} - {self.artist} ({self.spotify_streams_total} streams)"
