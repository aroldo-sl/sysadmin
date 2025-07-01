#!/usr/bin/env bash
./configure --prefix=$HOME/.local \
	--with-cairo \
	--with-xwidgets \
	--with-x-toolkit=gtk3 \
	--with-tree-sitter \
	--with-modules \
	--with-mailutils \
	--with-imagemagick \
	--with-gnutls \
	--with-xml2 \
	--with-xpm \
	--with-jpeg \
	--with-png \
	--with-tiff \
	--with-gif \
	--with-xft \
	--with-xpm 

