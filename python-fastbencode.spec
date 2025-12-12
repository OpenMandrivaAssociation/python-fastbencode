%global           pypi_name fastbencode
%define debug_package %nil

Name:             python-%{pypi_name}
Version:          0.3.1
Release:          2

Summary:          Implementation of bencode with optional fast C extensions
License:          BSD
Group:            Development/Python

URL:              https://pypi.org/project/fastbencode/
Source0:	https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3egg(setuptools)
BuildRequires:	python3dist(setuptools-scm)
BuildRequires:	python3dist(cython)

%description
fastbencode is an implementation of the bencode serialization
format originally used by BitTorrent.

The package includes both a pure-Python version and an optional
C extension based on Cython. Both provide the same functionality,
but the C extension provides significantly better performance.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
#rm -rf %{pypi_name}.egg-info

%build
%py_build


%install
%py_install

%files -n python-%{pypi_name}
#doc README.rst
%{python_sitearch}/%{pypi_name}
%{python_sitearch}/%{pypi_name}-%{version}.dist-info


