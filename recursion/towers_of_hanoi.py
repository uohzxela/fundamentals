def move_towers(n):
	move_towers_(n, 'src', 'dest', 'spare')

def move_towers_(n, src, dest, spare):
	if n > 0:
		move_towers_(n - 1, src, spare, dest)
		print 'move disk', n, 'from', src, 'to', dest
		move_towers_(n - 1, spare, dest, src)

move_towers(3)
