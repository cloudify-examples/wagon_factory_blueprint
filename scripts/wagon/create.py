#!/usr/bin/env python

import os
import tempfile
import virtualenv
from cloudify import ctx
from cloudify.exceptions import NonRecoverableError
from cloudify.state import ctx_parameters as inputs


if __name__ == '__main__':

    # Get the wagon source in a zip file.
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
    ctx.instance.runtime_properties['source'] = source

    # Arguments for creating the new virtualenv.
    venv_create_args = inputs.get('venv_create_args')
    _home_dir = venv_create_args.get('home_dir')
    if not _home_dir:
        _home_dir = tempfile.mkdtemp()
        venv_create_args['home_dir'] = _home_dir
    ctx.instance.runtime_properties['venv_create_args'] = venv_create_args

    # The python binary to use to execute the script.
    python_path = inputs.get('python_path', os.path.join(_home_dir, 'bin/python'))
    ctx.instance.runtime_properties['python_path'] = python_path

    # Create the new virtualenv.
    virtualenv.create_environment(**venv_create_args)
    # The path to the init_script for the virtualenv
    init_file = os.path.join(_home_dir, 'bin', 'activate_this.py')
    ctx.instance.runtime_properties['init_file'] = init_file

    # Arguments for creating the wagon.
    wagon_create_args = inputs.get('wagon_create_args')
    _archive_destination_dir = wagon_create_args.get('archive_destination_dir')
    if _archive_destination_dir is None:
        _archive_destination_dir = tempfile.gettempdir()
    if not os.path.exists(_archive_destination_dir):
        os.mkdir(_archive_destination_dir)
    wagon_create_args['archive_destination_dir'] = _archive_destination_dir
    ctx.instance.runtime_properties['wagon_create_args'] = wagon_create_args
