%define module objgraph
Name:		python-objgraph
Version:	3.6.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/o/%{module}/%{module}-%{version}.tar.gz
Summary:	Draws Python object reference graphs with graphviz
URL:		https://pypi.org/project/objgraph/
License:	MIT
Group:		Development/Python

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
BuildRequires:	python-sphinx
BuildRequires:	graphviz
BuildRequires:	graphviz-gtk

Requires:	python-graphviz
Requires:	graphviz
Requires:	graphviz-gtk
Suggests:	%{name}-doc = %{version}-%{release}
Suggests:	python-xdot

%description
%{module} is a module that lets you visually explore Python object graphs.

%package -n %{name}-doc
Summary: Documentation files for python-%{module}

%description -n %{name}-doc
Documentation files for python-%{module}.

######################################
%prep
%autosetup -p1 -n %{module}-%{version}

######################################
%build
# make clean and build docs before py_build
make clean images docs
%py_build

######################################
%install
%py3_install

echo $(pwd)
install -dpm 0755 %{buildroot}%{_docdir}/%{name}/html
install -dpm 0755 %{buildroot}%{_docdir}/%{name}/html/_images
install -dpm 0755 %{buildroot}%{_docdir}/%{name}/html/_sources
install -dpm 0755 %{buildroot}%{_docdir}/%{name}/html/_static
install -Dpm 0644 docs/_build/html/_images/* %{buildroot}%{_docdir}/%{name}/html/_images
install -Dpm 0644 docs/_build/html/_sources/* %{buildroot}%{_docdir}/%{name}/html/_sources
install -Dpm 0644 docs/_build/html/_static/* %{buildroot}%{_docdir}/%{name}/html/_static
install -Dpm 0644 docs/_build/html/*.* %{buildroot}%{_docdir}/%{name}/html

######################################
%files
%{py_sitedir}/%{module}.py
%{py_sitedir}/%{module}-%{version}*/*
%license LICENSE
%doc README.rst

%files -n %{name}-doc
%{_docdir}/%{name}/html/*
