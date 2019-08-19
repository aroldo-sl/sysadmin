#!/bin/bash

echo "Installing basic packages in Lubuntu 18.10"

# apt-get  install -y aptitude
# aptitude install -y build-essential
# aptitude install -y make 
# aptitude install -y llvm 
# aptitude install -y emacs
# aptitude install -y most
# aptitude install -y wget 
# aptitude install -y curl 
# aptitude install -y mercurial
# aptitude install -y mercurial-keyring
# aptitude install -y gnome-system-tools
# aptitude install -y thunderbird
# aptitude install -y chromium-browser
# aptitude install -y git
# aptitude install -y libjpeg8-dev
# aptitude install -y zlib1g-dev
# aptitude install -y pil

# ############################# Python-3.6
# aptitude install -y    libssl-dev 
# aptitude install -y    zlib1g-dev 
# aptitude install -y    libbz2-dev 
# aptitude install -y    libreadline-dev 
# aptitude install -y    libsqlite3-dev 
# aptitude install -y    libncurses5-dev 
# aptitude install -y    libncursesw5-dev 
# aptitude install -y    xz-utils 
# aptitude install -y    tk-dev 
# aptitude install -y    libffi-dev 
# aptitude install -y    liblzma-dev 
# aptitude install -y    python3-dev 
# aptitude install -y    python-six
# aptitude install -y    python3.6-dev    
# aptitude install -y    libpython3.6
# aptitude install -y    libpython3.6-dbg
# aptitude install -y    libpython3.6-dev
# aptitude install -y    libxml2-dev
# aptitude install -y    libxslt-dev
# aptitude install -y    pandoc
# ######## for sip (PyQt5)
# aptitude install -y flex
# aptitude install -y bison
# ####################### https://askubuntu.com/questions/612314/how-to-install-pyqt-for-python-3-in-ubuntu-14-10
# aptitude install -y qt5-default
# aptitude install -y python3-pyqt5
# aptitude install -y pyqt5-dev-tools
# aptitude install -y qttools5-dev-tools
# ############ usage: qtchooser -run-tool=designer -qt=5

# ################# Epson L555
# apt-get -f install
# aptitude install -y lsb-core
# aptitude install -y lsb-printing
# dpkg -i epson-inkjet-printer-201207w_1.0.0-1lsb3.2_amd64.deb
# aptitude install printer-driver-escpr

# ########################## PyInstaller

# # apt-add-repository  http://ftp.linux-foundation.org/pub/lsb/repositories/debian lsb-4.0 main
# # aptitude update
# aptitude install lsb lsb-build-cc

# ############# dvdbackup
# aptitude install -y dvdbackup
# aptitude install -y libdvdcss2
# aptitude install -y dvdauthor
# ######### failed:aptitude install -y libvdcss-dev

# ############## for Emacs
# aptitude install -y xsel


###########################
# aptitude install -y alsamixer


#############################
aptitude install -y chromium-browser
