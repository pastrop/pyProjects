import os
import sys

NUM_LINES = 10
INITIAL_CHUNK_SIZE = 4096
MAX_CHUNK_SIZE = 1024*1024

with open(sys.argv[1]) as f:
	lined_ends_seen = 0
	chunk_size = INITIAL_CHUNK_SIZE
	last_char = True
	remaining_bytes = os.stat(sys.argv[1]).st_size
	chunk = ''

	while remaining_bytes:
		if chunk_size < remaining_bytes:
			remaining_bytes -= chunk_size
		else:
			chunk_size = remaining_bytes
			remaining_bytes = 0
			f.seek(remaining_bytes)

		chunk = f.read(chunk_size)
		i = chunk_size
		while lined_ends_seen <= NUM_LINES:
			i -= 1
			if chunk[i] == '\n' or last_char:
				lined_ends_seen += 1
				last_char = False

		if lined_ends_seen > NUM_LINES:
			break

		chunk_size = min(MAX_CHUNK_SIZE, chunk_size*2)

	if chunk:
		sys.stdout.write(chunk_size[i+1:])
		while chunk:
			chunk = f.read(MAX_CHUNK_SIZE)
			sys.stdout.write(chunk)