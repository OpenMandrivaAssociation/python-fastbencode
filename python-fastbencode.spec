%define debug_package %nil
%define oname fastbencode
%define module fastbencode
%bcond tests 1

Name:		python-fastbencode
Version:	0.3.7
Release:	1
Summary:	Implementation of bencode with optional fast C extensions
License:	BSD
Group:		Development/Python
URL:		https://github.com/breezy-team/fastbencode
Source0:	https://github.com/breezy-team/fastbencode/archive/v%{version}/%{oname}-%{version}.tar.gz
Source1:	%{module}-%{version}-vendor.tar.xz

BuildSystem:	python
BuildRequires:  cargo
BuildRequires:  rust-packaging
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-rust)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(wheel)

%description
fastbencode is an implementation of the bencode serialization
format originally used by BitTorrent.

The package includes both a pure-Python version and an optional
C extension based on Cython. Both provide the same functionality,
but the C extension provides significantly better performance.

%prep
%autosetup -n %{module}-%{version} -p1 -a1

mkdir .cargo
cat >>.cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

EOF

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{ldflags} -lpython%{pyver}"
export CARGO_HOME=$PWD/.cargo
%py_build

%cargo_license_summary
%{cargo_license} > LICENSES.dependencies

%install
%py_install

%if %{with tests}
%check
PYTHONPATH="%{buildroot}%{python_sitearch}:${PWD}" \
%{__python} -m unittest -v
%endif

%files
%doc README.md
%license COPYING LICENSES.dependencies
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}.dist-info


