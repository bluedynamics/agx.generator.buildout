Test agx.generator.buildout
===========================

Setup configuration and emulate main routine::

    >>> from zope.configuration.xmlconfig import XMLConfig

    >>> import agx.core
    >>> XMLConfig('configure.zcml', agx.core)()

    >>> from agx.core.main import parse_options

    >>> import os
    >>> modelpath = os.path.join(datadir, 'agx.generator.buildout-sample.uml')

    >>> import pkg_resources
    >>> subpath = 'profiles/pyegg.profile.uml'
    >>> eggprofilepath = \
    ...     pkg_resources.resource_filename('agx.generator.pyegg', subpath)

    >>> subpath = 'profiles/buildout.profile.uml'
    >>> buildoutprofilepath = \
    ...     pkg_resources.resource_filename('agx.generator.buildout', subpath)

    >>> modelpaths = [modelpath, eggprofilepath, buildoutprofilepath]

    >>> outdir = os.path.join(datadir, 'agx.generator.buildout-sample')
    >>> controller = agx.core.Controller()
    >>> target = controller(modelpaths, outdir)
    >>> target
    <Directory object '/.../agx.generator.buildout/src/agx/generator/buildout/testing/data/agx.generator.buildout-sample' at ...>
