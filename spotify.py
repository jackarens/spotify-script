import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sys
import webbrowser

class Spotify:
    def __init__(self):
        # Use scope to set permissions for API read/write
        scope = "ugc-image-upload user-read-recently-played user-top-read user-read-playback-position user-read-playback-state user-modify-playback-state user-read-currently-playing app-remote-control streaming playlist-modify-public playlist-modify-private playlist-read-private playlist-read-collaborative user-follow-modify user-follow-read user-library-modify user-library-read user-read-email user-read-private"
        # Initialize local version of spotify connection
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='1475f5e740d84869b9613c5b0c27f8f8', client_secret='3981768fc444400e878e68f71547cfea', redirect_uri='http://localhost',scope=scope))
        # Initialize instance of URI class for opening URI links
        self.uriUtil = URI()

    # Skips to the next track
    def nextTrack(self):
        self.sp.next_track()
    
    # Plays the currently selected music
    def play(self):
        self.sp.start_playback()

    # Pauses the currently selected music
    def pause(self):
        self.sp.pause_playback()

    # Retrieves and returns the currently playing content
    def currentPlayback(self):
        return self.sp.current_playback()
    
    # Opens the currently playing artist in the desktop application
    def openCurrentPlaybackArtist(self):
        current_playback = self.currentPlayback()
        current_playback_uri = current_playback['item']['album']['artists'][0]['uri']
        self.uriUtil.openURI(current_playback_uri)
    
    # Opens the currently playing album in the desktop application
    def openCurrentPlaybackAlbum(self):
        current_playback = self.currentPlayback()
        current_playback_uri = current_playback['item']['album']['uri']
        self.uriUtil.openURI(current_playback_uri)

    # Prints the current users playlists in the console window
    def printCurrentUserPlaylists(self):
        current_user_playlists = self.sp.current_user_playlists()
        for i, playlist in enumerate(current_user_playlists['items']):
            print("  ", i, ':\t', playlist['name'], sep="")
    
    # Opens the current user's playlist for the given number
    def openPlaylist(self, playlistNum):
        current_user_playlists = self.sp.current_user_playlists()
        self.uriUtil.openURI(current_user_playlists['items'][int(playlistNum)]['uri'])

    # Util function to print the dict passed in in a readable format
    def prettyPrintInfo(self, info):
        print(json.dumps(info, sort_keys=True,indent=2))

class Album:
    def __init__(self, uri):
        self.uri = uri
        print('TODO')

    def getURI(self):
        return(self.uri)

class Artist:
    def __init__(self, uri):
        self.uri = uri
        print('TODO')

    def getURI(self):
        return(self.uri)

class Playlist:
    def __init__(self, uri):
        self.uri = uri
        print('TODO')

    def getURI(self):
        return(self.uri)

class URI:
    # Util function to open a URI to access the desktop application
    def openURI(self, uri):
        webbrowser.open(uri)

def main():
    # Initialize main class
    sp = Spotify()

    # Get command line args for instructions
    args = []
    for i, arg in enumerate(sys.argv):
        args.append(arg)

    # If only python had switch statements...
    if len(args) > 1:
        if args[1] == "help":
            print('Use one of the following options as a command line argument:')
            print('  openCurrentArtist, openCurrentAlbum, play, pause, myPlaylists, openPlaylist, openPlaylist [num], uri [uri].')
        elif args[1] == "openCurrentArtist":
            sp.openCurrentPlaybackArtist()
        elif args[1] == "openCurrentAlbum":
            sp.openCurrentPlaybackAlbum()
        elif args[1] == "play":
            sp.play()
        elif args[1] == "pause":
            sp.pause()
        elif args[1] == "myPlaylists":
            sp.printCurrentUserPlaylists()
        elif args[1] == "openPlaylist":
            if len(args) == 2:
                print('Enter a playlist:')
                sp.printCurrentUserPlaylists()
                playlistNum = input()
                sp.openPlaylist(playlistNum)
            elif len(args) == 3:
                sp.openPlaylist(args[2])
        elif args[1] == "uri":
            if len(args) == 2:
                print('No valid URI given')
            elif len(args) == 3:
                sp.uriUtil.openURI(args[2])
        else:
            print('No valid option provided!')
    else:
        print('No valid option provided!')

if __name__ == "__main__":
    main()
