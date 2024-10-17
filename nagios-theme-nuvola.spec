Name:		nagios-theme-nuvola
Version:	1.0.3
Release:	9
Summary:	Nagios Nuvola Style
License:	LGPL / Free (dtree)
Group:		Networking/Other
URL:		https://exchange.nagios.org/directory/Addons/Frontends-(GUIs-and-CLIs)/Web-Interfaces/Themes-and-Skins/Nuvola-Style/details
Source0:	nagios-nuvola-%{version}.tar.gz
Patch0:		nagios-nuvola-1.0.3-favicon.patch
BuildRequires:	sed >= 4.0
Requires:	nagios-www >= 2.9
Provides:	nagios-theme
Conflicts:	nagios-theme-default
BuildArch:	noarch

%description
Complete Nagios Style (Menu, Icons, Stylesheets, Images) for Nagios 2.0.

Style had been updated to version 1.0 with the free DTree menu.

This is a complete image pack, menu and stylesheets for Nagios 2.0. Icons are
from the Nuvola KDE theme (http://www.icon-king.com/)

%prep
%setup -q -c
%patch0 -p1

%install
install -d %{buildroot}%{_datadir}/nagios/www
cp -a html/* %{buildroot}%{_datadir}/nagios/www

%files
%doc *.txt
# well. should add it to /etc/nagios, but that means need  to enable FollowSymLinks directive in apache
%config(noreplace) %{_datadir}/nagios/www/config.js
%{_datadir}/nagios/www/*.html
%{_datadir}/nagios/www/images/*
%{_datadir}/nagios/www/stylesheets/*
%{_datadir}/nagios/www/side
