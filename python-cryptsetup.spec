%define 	module	cryptsetup
Summary:	Python bindings for cryptsetup
Name:		python-%{module}
Version:	0.1.4
Release:	1
License:	GPL v2+
Group:		Libraries/Python
# To generate source do
# git clone git://git.fedorahosted.org/python-cryptsetup.git
# make archive
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/python-cryptsetup/%{name}-%{version}.tar.gz/9455d264032342e322bbcce7ce5697d9/%{name}-%{version}.tar.gz
# Source0-md5:	9455d264032342e322bbcce7ce5697d9
URL:		http://git.fedorahosted.org/git/?p=python-cryptsetup.git
BuildRequires:	cryptsetup-devel >= 1.2.0
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	cryptsetup >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python module to ease the manipulation with LUKS devices.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc selftest.py
%dir %{py_sitedir}/pycryptsetup
%{py_sitedir}/pycryptsetup/*.py[co]
%attr(755,root,root) %{py_sitedir}/cryptsetup.so
%{py_sitedir}/pycryptsetup-%{version}-py*.egg-info
