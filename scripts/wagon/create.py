#!/usr/bin/env python

import tempfile

from cloudify import ctx
from cloudify.exceptions import NonRecoverableError

import pip
pip.main(['install', '--upgrade', 'pip'])

try:
    from wagon import create as create_wagon
except ImportError:
    pip.main(['install', 'wagon==0.6.0'])
    from wagon import create as create_wagon


def build_wagon(_source):

    ctx.logger.debug('building wagon from source: {0}.'.format(_source))

    wagon_location = \
        create_wagon(
            _source,
            archive_destination_dir=tempfile.mkdtemp(),
            archive_format='tar.gz'
        )

    ctx.logger.info('wagon_location: {0}'.format(wagon_location))

    return wagon_location


if __name__ == '__main__':

    resource_config = ctx.node.properties['resource_config']

    if resource_config.get('url'):
        source = \
            resource_config['url']
    elif resource_config.get('file'):
        source = \
            ctx.download_resource(resource_config['file'])
    else:
        raise NonRecoverableError(
            'Either url or file must be passed.')

    wagon_path = \
        build_wagon(source)

    ctx.instance.runtime_properties['wagon'] = wagon_path
