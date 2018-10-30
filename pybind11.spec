#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pybind11
Version  : 2.2.4
Release  : 1
URL      : https://github.com/pybind/pybind11/archive/v2.2.4.tar.gz
Source0  : https://github.com/pybind/pybind11/archive/v2.2.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pybind11-data = %{version}-%{release}
Requires: pybind11-license = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : glibc-dev
BuildRequires : pytest
BuildRequires : python3

%description
![pybind11 logo](https://github.com/pybind/pybind11/raw/master/docs/pybind11-logo.png)

%package data
Summary: data components for the pybind11 package.
Group: Data

%description data
data components for the pybind11 package.


%package dev
Summary: dev components for the pybind11 package.
Group: Development
Requires: pybind11-data = %{version}-%{release}
Provides: pybind11-devel = %{version}-%{release}

%description dev
dev components for the pybind11 package.


%package license
Summary: license components for the pybind11 package.
Group: Default

%description license
license components for the pybind11 package.


%prep
%setup -q -n pybind11-2.2.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1540935348
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1540935348
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pybind11
cp LICENSE %{buildroot}/usr/share/package-licenses/pybind11/LICENSE
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/cmake/*

%files dev
%defattr(-,root,root,-)
/usr/include/pybind11/attr.h
/usr/include/pybind11/buffer_info.h
/usr/include/pybind11/cast.h
/usr/include/pybind11/chrono.h
/usr/include/pybind11/common.h
/usr/include/pybind11/complex.h
/usr/include/pybind11/detail/class.h
/usr/include/pybind11/detail/common.h
/usr/include/pybind11/detail/descr.h
/usr/include/pybind11/detail/init.h
/usr/include/pybind11/detail/internals.h
/usr/include/pybind11/detail/typeid.h
/usr/include/pybind11/eigen.h
/usr/include/pybind11/embed.h
/usr/include/pybind11/eval.h
/usr/include/pybind11/functional.h
/usr/include/pybind11/iostream.h
/usr/include/pybind11/numpy.h
/usr/include/pybind11/operators.h
/usr/include/pybind11/options.h
/usr/include/pybind11/pybind11.h
/usr/include/pybind11/pytypes.h
/usr/include/pybind11/stl.h
/usr/include/pybind11/stl_bind.h

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pybind11/LICENSE
