import os
from agx.core import handler
from node.ext.template import JinjaTemplate


def templatepath(name):
    return os.path.join(os.path.dirname(__file__), 'templates/%s' % name)


@handler('ploneselfcontainedbuildout', 'uml2fs', 'hierarchygenerator',
         'pythonegg', order=11)
def ploneselfcontainedbuildout(self, source, target):
    if not source.stereotype('buildout:plone_self_contained'):
        return

    root = target.anchor
    root.factories['buildout.cfg'] = JinjaTemplate
    root.factories['bootstrap.py'] = JinjaTemplate

    if 'buildout.cfg' in root:
        return # dont overwrite the .cfg
    else:
        buildout = root['buildout.cfg'] = JinjaTemplate()
    buildout.template = templatepath('buildout.cfg.jinja')
    buildout.params['package'] = source.name

    if 'bootstrap.py' in root:
        bootstrap = root['bootstrap.py']
    else:
        bootstrap = root['bootstrap.py'] = JinjaTemplate()
    bootstrap.template = templatepath('bootstrap.py.jinja')
    bootstrap.params = {}
