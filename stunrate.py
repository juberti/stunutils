import string
import sys

times = [500, 200, 100, 50, 20, 10, 5, 2, 1]
sizes = [4, 8, 12, 16]
WIDTH = 6
STUN_SIZE = 108  # IPv4; 128 for IPv6

def format(kbps, width):
  if kbps < 10:
  	s = str(round(kbps, 2)) + 'k'
  elif kbps < 100:
  	s = str(round(kbps, 1)) + 'k'
  elif kbps < 1000:
  	s = str(int(kbps)) + 'k'
  else:
  	s = str(round(kbps / 1000, 2)) + 'M'
  return string.rjust(s, width)

def print_table(stun_size):
  print '     | packet len: ' + str(stun_size) + '+2 ufrag'
  s = '  ms |'
  for size in sizes:
    s += string.rjust(str(size), WIDTH)
  print s
  s = '-----|'
  for size in sizes:
    s += '-' * WIDTH
  print s
  for time in times:
    s = string.rjust(str(time), 4) + ' |'
    for size in sizes:
      kbps = float(stun_size + 2 * size) * 8 / time
      s += format(kbps, WIDTH)
    print s

stun_size = STUN_SIZE
if len(sys.argv) > 1:
  stun_size = int(sys.argv[1])
print_table(stun_size)
