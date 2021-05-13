apt -y install \
  vim \
  curl \
  gcc \
  make \
  cmake \
  git \
  btrfs-progs \
  golang-go \
  go-md2man \
  iptables \
  libassuan-dev \
  libc6-dev \
  libdevmapper-dev \
  libglib2.0-dev \
  libgpgme-dev \
  libgpg-error-dev \
  libostree-dev \
  libprotobuf-dev \
  libprotobuf-c-dev \
  libseccomp-dev \
  libselinux1-dev \
  libsystemd-dev \
  pkg-config \
  runc \
  uidmap \
  libapparmor-dev

export GOPATH=~/go
git clone https://go.googlesource.com/go $GOPATH
cd $GOPATH
git checkout tags/go1.10.8  # optional
cd src
./all.bash
export PATH=$GOPATH/bin:$PATH

