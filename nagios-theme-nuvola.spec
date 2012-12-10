Name:		nagios-theme-nuvola
Version:	1.0.3
Release:	%mkrel 7
Summary:	Nagios Nuvola Style
License:	LGPL / Free (dtree)
Group:		Networking/Other
URL:		http://www.nagiosexchange.org/cgi-bin/page.cgi?g=Detailed%2F1723.html;d=1
Source0:	nagios-nuvola-%{version}.tar.gz
Patch0:		nagios-nuvola-1.0.3-favicon.patch
BuildRequires:	sed >= 4.0
Requires:	nagios-www >= 2.9
Provides:	nagios-theme
Conflicts:	nagios-theme-default
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Complete Nagios Style (Menu, Icons, Stylesheets, Images) for Nagios 2.0.

Style had been updated to version 1.0 with the free DTree menu.

This is a complete image pack, menu and stylesheets for Nagios 2.0. Icons are
from the Nuvola KDE theme (http://www.icon-king.com/)

%prep
%setup -q -c
%patch0 -p1

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/nagios/www
cp -a html/* %{buildroot}%{_datadir}/nagios/www

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt
# well. should add it to /etc/nagios, but that means need  to enable FollowSymLinks directive in apache
%config(noreplace) %{_datadir}/nagios/www/config.js
%{_datadir}/nagios/www/*.html
%{_datadir}/nagios/www/images/*
%{_datadir}/nagios/www/stylesheets/*
%{_datadir}/nagios/www/side


%changelog
* Sat Dec 11 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-7mdv2011.0
+ Revision: 620472
- the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.0.3-6mdv2010.0
+ Revision: 440235
- rebuild

* Sun Jan 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.3-5mdv2009.1
+ Revision: 324527
- rediff favicon patch
- drop text patch, unknown purpose
- adapt to new nagios web files location
- don't duplicate spec-helper job
- spec cleanup

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-4mdv2009.0
+ Revision: 253559
- rebuild

* Mon Feb 11 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2mdv2008.1
+ Revision: 165279
- fix deps

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Apr 17 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-1mdv2008.0
+ Revision: 13805
- Import nagios-theme-nuvola



* Wed Apr 11 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-1mdv2007.1
- initial Mandriva package (pld import)
