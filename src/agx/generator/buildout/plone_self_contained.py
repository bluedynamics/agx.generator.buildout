import os
from agx.core import handler
from node.ext.template import JinjaTemplate


def templatepath(name):
    return os.path.join(os.path.dirname(__file__), 'templates/%s' % name)


@handler('bootstrappy', 'uml2fs', 'hierarchygenerator',
         'pythonegg', order=20)
def bootstrappy(self, source, target):
    root = target.anchor
    root.factories['bootstrap.py'] = JinjaTemplate
    
    if 'bootstrap.py' in root:
        bootstrap = root['bootstrap.py']
    else:
        bootstrap = JinjaTemplate()
        root['bootstrap.py'] = bootstrap
    
    bootstrap.template = templatepath('bootstrap.py.jinja')


@handler('buidloutcfg', 'uml2fs', 'hierarchygenerator',
         'pythonegg', order=20)
def buidloutcfg(self, source, target):
    root = target.anchor
    root.factories['buildout.cfg'] = JinjaTemplate
    
    if 'buildout.cfg' in root:
        buildout = root['buildout.cfg']
    else:
        buildout = JinjaTemplate()
        root['buildout.cfg'] = buildout
    
    buildout.template = templatepath('buildout.cfg.jinja')
    buildout.params['package'] = source.name