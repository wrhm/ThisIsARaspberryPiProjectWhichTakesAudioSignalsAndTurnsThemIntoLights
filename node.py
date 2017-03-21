#!/usr/bin/env python3
import asyncio

import argparse
import raftos
import random
import string

def randomword(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

async def run(node_id, peers):
    # List of songs
    song_list = raftos.ReplicatedList(name = 'song_list')

    # Song distributions
    which_song = raftos.ReplicatedDict(name = 'which_song')

    await raftos.wait_until_leader(node_id)
    for i in range(5):
      song = node_id + ' => ' + randomword(random.randint(3, 5))
      print (song)
      await song_list.append(song)

    while True:
        # Brought to you by <ip>:<port>
        await raftos.wait_until_leader(node_id)
        snapshot = await song_list.get()
        song = snapshot.pop() if(len(snapshot) > 0) else None
        await song_list.set(snapshot)

        song is not None and print ('leader: select, %r' % song)

        # And boom goes the dynamite
        snapshot = await which_song.get()
        for peer in peers:
          snapshot[peer] = song
        await which_song.set(snapshot)

        # The Devil opened up his case and he said, "I'll start this show."
        # And fire flew from his fingertips as he rosined up his bow.
        # And he pulled the bow across the strings and it made an evil hiss.
        # And a band of demons joined in and it sounded something like this.
        keys = await which_song.keys()
        if (node_id in keys):
          song = await which_song[node_id]

          print (song)
          await asyncio.sleep(60)

if (__name__ == '__main__'):
    parser = argparse.ArgumentParser()
    parser.add_argument('--node')
    parser.add_argument('--cluster')
    args = parser.parse_args()

    cluster = ['127.0.0.1:{}'.format(port) for port in args.cluster.split()]
    node = '127.0.0.1:{}'.format(args.node)

    raftos.configure({
        'log_path': './',
        'serializer': raftos.serializers.JSONSerializer
    })

    loop = asyncio.get_event_loop()
    loop.create_task(raftos.register(node, cluster=cluster))
    loop.run_until_complete(run(node, cluster))
