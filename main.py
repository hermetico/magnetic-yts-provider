# coding: utf-8
from provider import *
import json
__author__ = 'hermetico'

def compose_hash(hash_, torrent_name):
    return hash_ + '&dn=' + torrent_name + \
        '&tr=udp%3A%2F%2Fopen.demonii.com:%3A1337' \
        '&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80' \
        '&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969' \
        '&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969'

def compose_magnet(torrent_hash):
    return 'magnet:?xt=urn:btih:' + torrent_hash


def extract_torrents(response=None):
    if response is not None:
        data = json.loads(response)['data']

        for movie in data['movies']:
            title = movie['title']
            for torrent in movie['torrents']:
                name = "%s - %s" %(title, torrent['quality'])
                hash_ = compose_hash(torrent['hash'], name)
                magnet = compose_magnet(hash_)
                size = torrent['size']
                seeds = str(torrent['seeds'])
                peers = str(torrent['peers'])
                yield (name, hash_, magnet, size, seeds, peers)  # name, info_hash, magnet, size, seeds, peers


def search(info):
    Filtering.use_general(info)
    return process(generator=extract_torrents)


def search_movie(info):
    Filtering.use_movie(info)
    return process(generator=extract_torrents)


def search_episode(info):
    return []


def search_season(info):
    return []


# This registers your module for use
register(search, search_movie, search_episode, search_season)
