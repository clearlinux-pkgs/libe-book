#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libe-book
Version  : 0.1.3
Release  : 6
URL      : https://dev-www.libreoffice.org/src/libe-book-0.1.3.tar.xz
Source0  : https://dev-www.libreoffice.org/src/libe-book-0.1.3.tar.xz
Summary  : Library for parsing various reflowable ebook formats
Group    : Development/Tools
License  : MPL-2.0-no-copyleft-exception
Requires: libe-book-bin = %{version}-%{release}
Requires: libe-book-lib = %{version}-%{release}
Requires: libe-book-license = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : doxygen
BuildRequires : gperf
BuildRequires : pkgconfig(cppunit)
BuildRequires : pkgconfig(icu-i18n)
BuildRequires : pkgconfig(liblangtag)
BuildRequires : pkgconfig(librevenge-0.0)
BuildRequires : pkgconfig(librevenge-generators-0.0)
BuildRequires : pkgconfig(librevenge-stream-0.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(zlib)

%description
libe-book is a library and a set of tools for reading and converting
various reflowable e-book formats.

%package bin
Summary: bin components for the libe-book package.
Group: Binaries
Requires: libe-book-license = %{version}-%{release}

%description bin
bin components for the libe-book package.


%package dev
Summary: dev components for the libe-book package.
Group: Development
Requires: libe-book-lib = %{version}-%{release}
Requires: libe-book-bin = %{version}-%{release}
Provides: libe-book-devel = %{version}-%{release}
Requires: libe-book = %{version}-%{release}

%description dev
dev components for the libe-book package.


%package doc
Summary: doc components for the libe-book package.
Group: Documentation

%description doc
doc components for the libe-book package.


%package lib
Summary: lib components for the libe-book package.
Group: Libraries
Requires: libe-book-license = %{version}-%{release}

%description lib
lib components for the libe-book package.


%package license
Summary: license components for the libe-book package.
Group: Default

%description license
license components for the libe-book package.


%prep
%setup -q -n libe-book-0.1.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1566839714
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1566839714
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libe-book
cp COPYING %{buildroot}/usr/share/package-licenses/libe-book/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ebook2html
/usr/bin/ebook2raw
/usr/bin/ebook2text

%files dev
%defattr(-,root,root,-)
/usr/include/libe-book-0.1/libe-book/EBOOKDocument.h
/usr/include/libe-book-0.1/libe-book/libe-book.h
/usr/lib64/libe-book-0.1.so
/usr/lib64/pkgconfig/libe-book-0.1.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libe\-book/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libe-book-0.1.so.1
/usr/lib64/libe-book-0.1.so.1.0.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libe-book/COPYING
