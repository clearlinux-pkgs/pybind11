#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pybind11
Version  : 2.4.3
Release  : 6
URL      : https://files.pythonhosted.org/packages/aa/91/deb6743e79e22ab01502296570b39b8404f10cc507a6692d612a7fee8d51/pybind11-2.4.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/aa/91/deb6743e79e22ab01502296570b39b8404f10cc507a6692d612a7fee8d51/pybind11-2.4.3.tar.gz
Summary  : A lightweight header-only library that exposes C++ types in Python and vice versa
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pybind11-license = %{version}-%{release}
Requires: pybind11-python = %{version}-%{release}
Requires: pybind11-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pytest
BuildRequires : python3-dev

%description
# pybind11 — Seamless operability between C++11 and Python
[![Documentation Status](https://readthedocs.org/projects/pybind11/badge/?version=master)](http://pybind11.readthedocs.org/en/master/?badge=master)
[![Documentation Status](https://readthedocs.org/projects/pybind11/badge/?version=stable)](http://pybind11.readthedocs.org/en/stable/?badge=stable)
[![Gitter chat](https://img.shields.io/gitter/room/gitterHQ/gitter.svg)](https://gitter.im/pybind/Lobby)
[![Build Status](https://travis-ci.org/pybind/pybind11.svg?branch=master)](https://travis-ci.org/pybind/pybind11)
[![Build status](https://ci.appveyor.com/api/projects/status/riaj54pn4h08xy40?svg=true)](https://ci.appveyor.com/project/wjakob/pybind11)

%package dev
Summary: dev components for the pybind11 package.
Group: Development
Provides: pybind11-devel = %{version}-%{release}
Requires: pybind11 = %{version}-%{release}
Requires: pybind11 = %{version}-%{release}

%description dev
dev components for the pybind11 package.


%package license
Summary: license components for the pybind11 package.
Group: Default

%description license
license components for the pybind11 package.


%package python
Summary: python components for the pybind11 package.
Group: Default
Requires: pybind11-python3 = %{version}-%{release}

%description python
python components for the pybind11 package.


%package python3
Summary: python3 components for the pybind11 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pybind11 package.


%prep
%setup -q -n pybind11-2.4.3
cd %{_builddir}/pybind11-2.4.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576607316
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pybind11
cp %{_builddir}/pybind11-2.4.3/LICENSE %{buildroot}/usr/share/package-licenses/pybind11/a33b61f04391a38904373d020e7fbabf211383f6
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/python3.8/pybind11/attr.h
/usr/include/python3.8/pybind11/buffer_info.h
/usr/include/python3.8/pybind11/cast.h
/usr/include/python3.8/pybind11/chrono.h
/usr/include/python3.8/pybind11/common.h
/usr/include/python3.8/pybind11/complex.h
/usr/include/python3.8/pybind11/detail/class.h
/usr/include/python3.8/pybind11/detail/common.h
/usr/include/python3.8/pybind11/detail/descr.h
/usr/include/python3.8/pybind11/detail/init.h
/usr/include/python3.8/pybind11/detail/internals.h
/usr/include/python3.8/pybind11/detail/typeid.h
/usr/include/python3.8/pybind11/eigen.h
/usr/include/python3.8/pybind11/embed.h
/usr/include/python3.8/pybind11/eval.h
/usr/include/python3.8/pybind11/functional.h
/usr/include/python3.8/pybind11/iostream.h
/usr/include/python3.8/pybind11/numpy.h
/usr/include/python3.8/pybind11/operators.h
/usr/include/python3.8/pybind11/options.h
/usr/include/python3.8/pybind11/pybind11.h
/usr/include/python3.8/pybind11/pytypes.h
/usr/include/python3.8/pybind11/stl.h
/usr/include/python3.8/pybind11/stl_bind.h

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pybind11/a33b61f04391a38904373d020e7fbabf211383f6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
