#!/usr/bin/env python

import os
from cloudify import ctx


if __name__ == '__main__':

    wagon_path = ctx.instance.runtime_properties['wagon']
    os.remove(wagon_path)
