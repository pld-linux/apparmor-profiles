%define		_ver 2.0
%define		_svnrel 6376
Summary:	AppArmor profiles
Summary(pl):	Profile AppArmor
Name:		apparmor-profiles
Version:	%{_ver}.%{_svnrel}
Release:	0.1
Group:		Base
Source0:	http://forge.novell.com/modules/xfcontent/private.php/apparmor/Development%20-%20April%20Snapshot/%{name}-%{_ver}-%{_svnrel}.tar.gz
License:	GPL
URL:		http://forge.novell.com/modules/xfmod/project/?apparmor
Requires:	apparmor-parser
Provides:	subdomain-profiles
Obsoletes:	subdomain-profiles
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		extras_dir	%{_sysconfdir}/apparmor/profiles/extras
%define		profiles_dir	%{_sysconfdir}/apparmor.d

%description
Base AppArmor profiles (aka security policy). AppArmor is a file
mandatory access control mechanism. AppArmor confines processes to the
resources allowed by the systems administrator and can constrain the
scope of potential security vulnerabilities. This package is part of a
suite of tools that used to be named SubDomain.

%description -l pl
Podstawowe profile AppArmor (zwane tak�e polityk� bezpiecze�stwa).
AppArmor to mechanizm obowi�zkowej kontroli dost�pu do plik�w.
AppArmor ogranicza procesy do zasob�w udost�pnionych przez
administratora systemu i mo�e ogranicza� zakres potencjalnych luk w
bezpiecze�stwie. Ten pakiet jest cz�ci� zestawu narz�dzi zwanych
SubDomain.

%prep
%setup -q -n %{name}-%{_ver}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	EXTRASDIR=$RPM_BUILD_ROOT%{extras_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_sysconfdir}/apparmor
%dir %{_sysconfdir}/apparmor/profiles
%dir %{extras_dir}
%config(noreplace) %verify(not md5 mtime size) %{extras_dir}/*
%dir %{_sysconfdir}/apparmor.d
%dir %{_sysconfdir}/apparmor.d/abstractions
%dir %{_sysconfdir}/apparmor.d/program-chunks
%dir %{_sysconfdir}/apparmor.d/tunables
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/*.*
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/*/*
