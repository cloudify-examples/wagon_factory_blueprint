import os
import signal
from cloudify import ctx


if __name__ == '__main__':

    pid = ctx.instance.runtime_properties['pid']

    try:
        os.kill(pid, signal.SIGTERM)
        ctx.logger.info('Webserver terminated.')
    except IOError:
        ctx.logger.error('Webserver not running.')
