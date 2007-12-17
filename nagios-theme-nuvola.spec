Summary:	Nagios Nuvola Style
Name:		nagios-theme-nuvola
Version:	1.0.3
Release:	%mkrel 1
License:	LGPL / Free (dtree)
Group:		Networking/Other
URL:		http://tinyurl.com/a946b
Source0:	nagios-nuvola-%{version}.tar.gz
Patch0:		nagios-nuvola-favicon.patch
Patch1:		nagios-nuvola-texts.patch
BuildRequires:	sed >= 4.0
Requires:	nagios-www >= 2.9
Provides:	nagios-theme
Obsoletes:	nagios-theme
BuildArch:	noarch

%define		_nagiosdir	%{_datadir}/nagios

%description
Complete Nagios Style (Menu, Icons, Stylesheets, Images) for Nagios 2.0.

Style had been updated to version 1.0 with the free DTree menu.

This is a complete image pack, menu and stylesheets for Nagios 2.0. Icons are
from the Nuvola KDE theme (http://www.icon-king.com/)

%prep

%setup -q -c

# undos the sources
find . -type f '(' -name '*.html' -o -name '*.js' -o -name '*.css' ')' -print0 | xargs -0 sed -i -e 's,\r$,,'

%patch0 -p1
%patch1 -p1

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_nagiosdir}
cp -a html/* %{buildroot}%{_nagiosdir}

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc *.txt
# well. should add it to /etc/nagios, but that means need  to enable FollowSymLinks directive in apache
%config(noreplace) %verify(not md5 mtime size) %{_nagiosdir}/config.js
%{_nagiosdir}/*.html
%{_nagiosdir}/images/*
%{_nagiosdir}/stylesheets/*
%{_nagiosdir}/side
