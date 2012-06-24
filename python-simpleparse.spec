%include	/usr/lib/rpm/macros.python
%define 	module simpleparse
%define 	cap_name SimpleParse
Summary:	Python package providing a simple parser generator for use with the mxTextTool
Summary(pl.UTF-8):   Pakiet zawierający prosty generator parserów dla mxTextTool
Name:		python-%{module}
Version:	2.0.1a3
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/%{module}/%{cap_name}-%{version}.zip
# Source0-md5:	dffa19a7a21d342d56c3d1bf391c2c2d
URL:		http://simpleparse.sourceforge.net/
Requires:	python-mx-TextTools >= 2.1-0b5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SimpleParse allows you to generate tagging tables for use with the
text-tagging engine directly from your EBNF grammar.

%description -l pl.UTF-8
SimpleParse pozwala na generowanie tabeli tagujących do użytku z
silnikiem tagującym tekst bezpośrendnio z gramatyk EBNF.

%prep
%setup -q -n %{cap_name}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

python setup.py install \
        --root=$RPM_BUILD_ROOT --optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%doc %{module}/doc %{module}/examples
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%dir %{py_sitedir}/%{module}/common
%{py_sitedir}/%{module}/common/*.py[co]
%dir %{py_sitedir}/%{module}/xml
%{py_sitedir}/%{module}/xml/*.py[co]
