from soco import SoCo, discover
#from lxml import etree

if __name__ == '__main__':
    for zone in discover():
        print(f'Playername={zone.player_name} IP={zone.ip_address}')

    sonos = SoCo(zone.ip_address)

    #print(f'Shares={sonos.music_library.list_library_shares()}')
    #albums = sonos.music_library.get_music_library_information('playlists')
    #print(albums)

    #sonos.play_uri('http://192.168.178.39:5901/stream/swyh.mp3')
    #sonos.play_uri('http://ia801402.us.archive.org/20/items/TenD2005-07-16.flac16/TenD2005-07-16t10Wonderboy.mp3')
    # FM4.ORF.AT
    sonos.play_uri('http://mp3stream1.apasf.apa.at:8000', title='FM4', force_radio=True)

    track = sonos.get_current_track_info()
    print(f'URI={track["uri"]}')

    #sonos.pause()
    sonos.play()

    sonos.volume = 45
    sonos.bass = 0
    sonos.treble = 0
    sonos.status_light = True
    print(f'Volume={sonos.volume}')
    print(f'Bass={sonos.bass}')
    print(f'Treble={sonos.treble}')
    info = sonos.get_current_track_info()
    print(f'Position={info["position"]}')

    parser = etree.XMLParser(remove_blank_text=True, ns_clean=True)
    metadata = etree.XML(info['metadata'], parser)
    #metadata = etree.fromstring(info["metadata"], pretty_print=True)
    #print(f'Metadata={etree.tostring(metadata)}')
    for item in metadata.getiterator():
        if item.tag.endswith('streamContent'):
            print(f'streamContent={item.text}')
