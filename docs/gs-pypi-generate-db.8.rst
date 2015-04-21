===================
gs-pypi-generate-db
===================

-----------------------
generate DB for gs-pypi
-----------------------

:Author: Written by Jauhien Piatlicki <jauhien@gentoo.org>. GSoC idea
	 and mentorship by Rafael Martins. Lots of help and improvements
	 by Brian Dolbec.
:Date:   2015-04-22
:Copyright: Copyright (c) 2013-2015 Jauhien Piatlicki, License: GPL-2
:Version: 0.2
:Manual section: 8
:Manual group: g-sorcery

SYNOPSIS
========

**gs-pypi-generate-db** [**-c** *COUNT*] [**--layout-version** *LAYOUT_VERSION*]
[**--structure-version** *STRUCTURE_VERSION*] [**-f** *FORMAT*] *DB_DIRNAME*

DESCRIPTION
===========

**gs-pypi-generate-db** is a maintenance tool for **gs-pypi**. It
generates DB that later can be used during ebuild generation.

OPTIONS
=======

**-c** *COUNT*
    Count of package entries that should be processed (if absent --
    process all packages).

**--layout-version** *LAYOUT_VERSION*
    **g-sorcery** DB directory layout version (v.1 be default).

**--structure-version** *STRUCTURE_VERSION*
    **g-sorcery** DB structure version (v.1 by default).

**-f** *FORMAT*
    Packages data file format (BSON by default).

SEE ALSO
========

**gs-pypi**\(8), **g-sorcery.cfg**\(8), **portage**\(5), **emerge**\(1), **layman**\(8)
