import re
from subprocess import Popen, PIPE
from fabric.api import local


def update():
    local('rm underscore-min.js')
    output = Popen(["bower", "info", "underscore"], stdout = PIPE).communicate()[0]
    latest_version = re.findall(r"version: '([1-9]\.\d+\.\d+)',", output)[0]
    print 'latest version: {0}'.format(latest_version)
    local('wget https://cdnjs.cloudflare.com/ajax/libs/underscore.js/{0}/underscore-min.js'.format(latest_version))
