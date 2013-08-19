PhD Dissertation
================

The following tools were used to build the pdf version of my dissertation:

        $ xelatex -version
        XeTeX 3.1415926-2.5-0.9999.3-2013080616 (TeX Live 2013)
        kpathsea version 6.1.1
        Copyright 2013 SIL International and Jonathan Kew.
        There is NO warranty.  Redistribution of this software is
        covered by the terms of both the XeTeX copyright and
        the Lesser GNU General Public License.
        For more information about these matters, see the file
        named COPYING and the XeTeX source.
        Primary author of XeTeX: Jonathan Kew.
        Compiled with ICU version 51.2; using 51.2
        Compiled with zlib version 1.2.8; using 1.2.8
        Compiled with FreeType2 version 2.4.12; using 2.4.12
        Compiled with Graphite2 version 1.2.1; using 1.2.1
        Compiled with HarfBuzz version 0.9.18; using 0.9.18
        Compiled with fontconfig version 2.10.92; using 2.10.92
        Compiled with libpng version 1.6.3; using 1.6.3
        Compiled with poppler version 0.22.5
        $ biber -version
        biber version: 1.7

All included packages were those distributed with the TeXLive 2013 packages of
the Gentoo portage tree.

To build the pdf, latexmk was used:

        $ latexmk -pdf dissertation_dale_lukas_peterson.tex

