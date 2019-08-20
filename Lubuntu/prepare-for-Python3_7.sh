#!/bin/bash

echo "Preparing the system for compiling Python3.7 without sudo rights."

# aptitude install -y    build-essential 
# aptitude install -y    libssl-dev 
# aptitude install -y    zlib1g-dev 
# aptitude install -y    libbz2-dev 
# aptitude install -y    libreadline-dev 
# aptitude install -y    libsqlite3-dev 
# aptitude install -y    wget 
# aptitude install -y    make 
# aptitude install -y    curl 
# aptitude install -y    llvm 
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
apt-get build-dep python3-lxml

######### for sip (PyQt5)
# aptitude install -y flex
# aptitude install -y bison
######################## https://askubuntu.com/questions/612314/how-to-install-pyqt-for-python-3-in-ubuntu-14-10
# aptitude install -y qt5-default
# aptitude install -y python3-pyqt5
# aptitude install -y pyqt5-dev-tools
# aptitude install -y qttools5-dev-tools
############# usage: qtchooser -run-tool=designer -qt=5
