#!/usr/bin/env python

# THIS IS A TEST SCRIPT TO INTERACT WITH NVIM's
# PYTHON INTEGRATION
#
# Run this in a separate terminal:
# $ NVIM_LISTEN_ADDRESS=/tmp/tmp.nvim nvim ~/Desktop/vim-python.tx
# Only then run this script


from pynvim import attach
nvim = attach('socket', path='/tmp/tmp.nvim')

# import ipdb
# ipdb.set_trace()

start = nvim.current.buffer.mark('<')[0] - 1
end = nvim.current.buffer.mark('>')[0]

buffer_range = nvim.current.buffer[start:end]

# TODO DEBUG
print(f'{start=}, {end=}')

print(f'{buffer_range=}')
