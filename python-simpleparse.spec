# TODO:
# - tests
%define 	module		simpleparse
%define 	cap_name	SimpleParse
Summary:	Python package providing a simple parser generator for use with the mxTextTool
Summary(pl.UTF-8):	Pakiet zawierający prosty generator parserów dla mxTextTool
Name:		python-%{module}
Version:	2.1.1
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	https://pypi.python.org/packages/source/S/SimpleParse/%{cap_name}-%{version}.tar.gz
# Source0-md5:	d67aaceca86acc763d6eebee919cc8aa
URL:		http://simpleparse.sourceforge.net/
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
Requires:	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SimpleParse allows you to generate tagging tables for use with the
text-tagging engine directly from your EBNF grammar.

%description -l pl.UTF-8
SimpleParse pozwala na generowanie tabeli tagujących do użytku z
silnikiem tagującym tekst bezpośrednio z gramatyk EBNF.

%prep
%setup -q -n %{cap_name}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

python setup.py install \
        --skip-build \
        --optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc  doc examples
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%dir %{py_sitedir}/%{module}/common
%{py_sitedir}/%{module}/common/*.py[co]
%dir %{py_sitedir}/%{module}/examples
%{py_sitedir}/%{module}/examples/*.py[co]
%dir %{py_sitedir}/%{module}/stt
%{py_sitedir}/%{module}/stt/*.py[co]
%dir %{py_sitedir}/%{module}/stt/TextTools
%{py_sitedir}/%{module}/stt/TextTools/*.py[co]
%dir %{py_sitedir}/%{module}/stt/TextTools/Constants
%{py_sitedir}/%{module}/stt/TextTools/Constants/*.py[co]
%dir %{py_sitedir}/%{module}/stt/TextTools/mxTextTools
%{py_sitedir}/%{module}/stt/TextTools/mxTextTools/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/stt/TextTools/mxTextTools/mxTextTools.so
%dir %{py_sitedir}/%{module}/tests
%{py_sitedir}/%{module}/tests/*.py[co]
%dir %{py_sitedir}/%{module}/xmlparser
%{py_sitedir}/%{module}/xmlparser/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitedir}/SimpleParse-*.egg-info
%endif
