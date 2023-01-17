#!/usr/bin/env python3

import os
import sys
from configparser import ConfigParser


# import snoop  # print function args
# @snoop
def get_toml_value(_, filename, option_name, section='default'):
    config = ConfigParser()
    config.read(filename)

    return config.get(section, option_name)

try:
    print(get_toml_value(*sys.argv), end='')
except Exception as e:
    print(e, file=sys.stderr)
    purple = os.environ['PURPLE']
    no_color = os.environ['NC']
    print(sys.argv, file=sys.stderr)
    print('USAGE: {}read_toml_setting <CONF_FILE> <ITEM> [<SECTION>]{}'.format(purple, no_color))
