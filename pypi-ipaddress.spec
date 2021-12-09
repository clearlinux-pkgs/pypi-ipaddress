#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-ipaddress
Version  : 1.0.23
Release  : 1
URL      : https://files.pythonhosted.org/packages/b9/9a/3e9da40ea28b8210dd6504d3fe9fe7e013b62bf45902b458d1cdc3c34ed9/ipaddress-1.0.23.tar.gz
Source0  : https://files.pythonhosted.org/packages/b9/9a/3e9da40ea28b8210dd6504d3fe9fe7e013b62bf45902b458d1cdc3c34ed9/ipaddress-1.0.23.tar.gz
Summary  : IPv4/IPv6 manipulation library
Group    : Development/Tools
License  : Python-2.0
Requires: pypi-ipaddress-license = %{version}-%{release}
Requires: pypi-ipaddress-python = %{version}-%{release}
Requires: pypi-ipaddress-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
ipaddress
=========
Python 3.3+'s [ipaddress](http://docs.python.org/dev/library/ipaddress) for Python 2.6, 2.7, 3.2.

%package license
Summary: license components for the pypi-ipaddress package.
Group: Default

%description license
license components for the pypi-ipaddress package.


%package python
Summary: python components for the pypi-ipaddress package.
Group: Default
Requires: pypi-ipaddress-python3 = %{version}-%{release}

%description python
python components for the pypi-ipaddress package.


%package python3
Summary: python3 components for the pypi-ipaddress package.
Group: Default
Requires: python3-core
Provides: pypi(ipaddress)

%description python3
python3 components for the pypi-ipaddress package.


%prep
%setup -q -n ipaddress-1.0.23
cd %{_builddir}/ipaddress-1.0.23

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639042763
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ipaddress
cp %{_builddir}/ipaddress-1.0.23/LICENSE %{buildroot}/usr/share/package-licenses/pypi-ipaddress/3f92966b8a60875dca8d9e1d6b63ac7eb9e4178e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-ipaddress/3f92966b8a60875dca8d9e1d6b63ac7eb9e4178e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*