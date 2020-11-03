from soco import SoCo, discover

if __name__ == '__main__':
    for zone in discover():
        print(zone.player_name, zone.ip_address)

    sonos = SoCo(zone.ip_address) # Pass in the IP of your Sonos speaker
    # You could use the discover function instead, if you don't know the IP

    # Pass in a URI to a media file to have it streamed through the Sonos
    # speaker
    #sonos.play_uri('http://ia801402.us.archive.org/20/items/TenD2005-07-16.flac16/TenD2005-07-16t10Wonderboy.mp3')
    sonos.play_uri('http://192.168.178.39:5901/stream/swyh.mp3')

    track = sonos.get_current_track_info()

    print(track['title'])

    sonos.pause()

    # Play a stopped or paused track
    sonos.play()
