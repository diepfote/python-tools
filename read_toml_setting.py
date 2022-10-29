#!/usr/bin/env python3

import sys
from configparser import ConfigParser


# import snoop  # print function args
# @snoop
def get_toml_value(filename, option_name):
    config = ConfigParser()
    config.read(filename)

    return config.get('default', option_name)

print(get_toml_value(sys.argv[1], sys.argv[2]), end='')

