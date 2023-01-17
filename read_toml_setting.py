#!/usr/bin/env python3

import sys
from configparser import ConfigParser


# import snoop  # print function args
# @snoop
def get_toml_value(_, filename, option_name, section='default'):
    config = ConfigParser()
    config.read(filename)

    return config.get(section, option_name)

print(get_toml_value(*sys.argv), end='')

