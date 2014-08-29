This is [g-sorcery](https://github.com/jauhien/g-sorcery) backend for Python PyPI packages.


Installation
======================

Currently gs-pypi is not keyworded, so [add keywords](https://bitbucket.org/mgorny/flaggie/), then install it:

```
flaggie app-portage/gs-pypi '+**'
```

```
emerge -va gs-pypi
```

Note that it needs layman-9999.


Usage
======================

There are two ways of using **gs-pypi**

** Using gs-pypi with [layman](https://wiki.gentoo.org/wiki/Layman) **

It the the recommend way and I strongly suggest it.

Then you should just run `layman -L` as
root and find an overlay you want. Type of overlay will be
displayed as *g-sorcery*. Then you add this overlay as
usually and emerge packages you want. It's all you need to do. Example:

```
layman -L
layman -a pypi
emerge -va pycallgraph
```

There is 1 gs-pypi overlays currently: [pypi](https://pypi.python.org/pypi).

When using **gs-pypi** with layman you can populate overlay only with packages you want.
To do so you should add a section named gs-pypi to */etc/g-sorcery/g-sorcery.cfg*.
In this section you can add entries named REPO_packages (REPO here is the name
of repository you want to add) which are space separated lists of packages you need. ebuilds for
dependencies will be generated automatically if backend supports this possibility.

```
[main]
package_manager=portage

[gs-pypi]
pypi_packages=pycallgraph
```
I strongly recommend to do so, as pypi overlay is quite big and you may be
do not want generate all the ebuilds from it.


** Using gs-pypi as stand-alone tool **

In this case you should create an overlay (see **portage** documentation), sync it and populate
it with one or more ebuilds. Then ebuilds could be installed by emerge or by **gs-pypi** tool.
This is not the recommended way and may be removed in the future.

Create new user overlay:

```
gs-pypi -o $OVERLAY_DIRECTORY -r pypi sync
```

List packages:

```
gs-pypi -o $OVERLAY_DIRECTORY -r pypi list
```

Install any package you want:

```
gs-pypi -o $OVERLAY_DIRECTORY -r pypi install $PACKAGE
```

Note, that if you call **generate-tree** command your overlay
will be wiped and overlay tree for a given repository will be generated. Be careful!

See man page of **gs-pypi** for further information.
