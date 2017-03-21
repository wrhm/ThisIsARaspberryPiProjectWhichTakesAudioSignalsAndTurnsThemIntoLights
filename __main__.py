#!/usr/bin/env python3
# __main__.py
# aoneill - 03/21/17

import contextlib
import socket

BUF_SIZE = 1024
MSG = b'fuck you'

def expect(*e_args):
  def decorator(func):
    def wrapper(*args, **kwargs):
      if (len(e_args) != len(args)):
        raise TypeError

      # wtf python3
      args = map(lambda item: e_args[item[0]](item[1]), enumerate(args))
      args = list(args)
      return func(*args, **kwargs)
    return wrapper
  return decorator

def session(conn, buf_size):
  buf = conn.recv(buf_size)
  while (len(buf) > 0):
    yield buf
    buf = conn.recv(buf_size)

@expect(int, str)
def main(port, other):
  # Server like a person who serves you food
  print('Starting: localhost, %r' % (port))
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind(('localhost', port))
  server.listen(1)

  # Only the best for our B2B client's. We leverage the cloud for
  # enterprise-grade bullshit
  (ohost, oport) = tuple(other.split(':'))
  oport = int(oport)

  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  print('Connecting: %r, %r' % (ohost, oport))
  while True:
    # Try to make a difference over and over until the world changes in
    # some small, imperceptible way. Does anything really matter? ...
    try:
      client.connect((ohost, oport))
      break

    # who cares anyways
    except ConnectionRefusedError:
      pass

  # The never ending struggle between man and machine starts here
  while True:
    # All-inclusive
    print('Accept')
    (conn, addr) = server.accept()

    # Start a fight
    if(port < oport):
      client.send(b'0')

    # Rocky IV
    for buf in session(conn, BUF_SIZE):
      count = int(buf)

      # music, lights


      client.send(b'%d' % (count + 1))

if (__name__ == '__main__'):
  import sys
  main(*sys.argv[1:])
