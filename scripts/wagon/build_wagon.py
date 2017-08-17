#!/usr/bin/env python

import os
import ast
import sys

if __name__ == '__main__':

    wagon_source = os.environ.get('wagon_source')
    wagon_create_args = os.environ.get('wagon_create_args')
    upgrade_pip = os.environ.get('upgrade_pip')
    init_file = os.environ.get('init_file')

    if not isinstance(wagon_source, basestring):
        print "The wagon source %s is not valid" % str(wagon_source)
        sys.exit(os.EX_USAGE)

    if isinstance(wagon_create_args, basestring):
        try:
            wagon_create_args = ast.literal_eval(wagon_create_args)
        except SyntaxError:
            print "The wagon_create_args structure %s is not valid." % str(wagon_create_args)
            sys.exit(os.EX_USAGE)

    execfile(init_file, dict(__file__=init_file))

    import pip

    if upgrade_pip:
        pip.main(['install', '-U', 'pip'])

    pip.main(['install', 'wagon==0.3.2'])
    from wagon import wagon
    w = wagon.Wagon(source=wagon_source)
    try:
        build_wagon_output = w.create(**wagon_create_args)
        print build_wagon_output
    except KeyError as e:
        print "Failed to create wagon because: %s." % str(e)
        sys.exit(os.EX_CANTCREAT)

    if not build_wagon_output:
        raise Exception('Wagon output: {0}'.format(build_wagon_output))

    # sys.exit(os.EX_OK)
