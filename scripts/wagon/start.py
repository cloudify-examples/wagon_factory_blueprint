import os
import sys
import subprocess
from cloudify import ctx

IS_WIN = os.name == 'nt'


def run_server(_path, _port):
    webserver_cmd = [sys.executable, '-m', 'SimpleHTTPServer', str(_port)]
    if not IS_WIN:
        webserver_cmd.insert(0, 'nohup')
    ctx.logger.info('Serving wagon port: {0}'.format(str(_port)))
    with open(os.devnull, 'wb') as dn:
        process = subprocess.Popen(webserver_cmd, stdout=dn, stderr=dn, cwd=_path)
    return process.pid


def set_pid(_pid):
    ctx.logger.info('Setting `pid` runtime property: {0}'.format(str(pid)))
    ctx.instance.runtime_properties['pid'] = _pid


if __name__ == '__main__':

    wagon_directory = os.path.dirname(ctx.instance.runtime_properties['wagon'])
    port = ctx.node.properties['port']
    pid = run_server(wagon_directory, port)
    set_pid(pid)
