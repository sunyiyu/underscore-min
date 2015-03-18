import re
from subprocess import Popen, PIPE
from fabric.api import local


def update():
    local('rm underscore-min.js')
    local('rm underscore-min.map')
    output = Popen(["bower", "info", "underscore"], stdout = PIPE).communicate()[0]
    latest_version = re.findall(r"version: '([1-9]\.\d+\.\d+)',", output)[0]
    local('wget https://cdnjs.cloudflare.com/ajax/libs/underscore.js/{0}/underscore-min.js'.format(latest_version))
    local('wget https://cdnjs.cloudflare.com/ajax/libs/underscore.js/{0}/underscore-min.map'.format(latest_version))
    print 'latest version: {0}'.format(latest_version)
