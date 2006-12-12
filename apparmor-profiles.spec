%define		_ver 2.0
%define		_svnrel 119
Summary:	AppArmor profiles
Summary(pl):	Profile AppArmor
Name:		apparmor-profiles
Version:	%{_ver}.%{_svnrel}
Release:	0.3
Group:		Base
Source0:	http://forgeftp.novell.com/apparmor/Development%20-%20September%20snapshot/%{name}-%{_ver}-%{_svnrel}.tar.gz
# Source0-md5:	7a4501c2bb71fbdf1445e17ca4c58cb5
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
Podstawowe profile AppArmor (zwane tak¿e polityk± bezpieczeñstwa).
AppArmor to mechanizm obowi±zkowej kontroli dostêpu do plików.
AppArmor ogranicza procesy do zasobów udostêpnionych przez
administratora systemu i mo¿e ograniczaæ zakres potencjalnych luk w
bezpieczeñstwie. Ten pakiet jest czê¶ci± zestawu narzêdzi zwanych
SubDomain.

%package abstractions
Summary:	Abstraction AppArmor files
Summary(pl):	Pliki abstrakcji dla AppArmor
Group:		Base
Requires:	%{name} = %{version}-%{release}

%description abstractions
Abstraction AppArmor files.

%description abstractions -l pl
Pliki abstrakcji dla AppArmor.

%package examples
Summary:	Example AppArmor profiles
Summary(pl):	Przyk³adowe profile AppArmor
Group:		Base
Requires:	%{name}-abstractions = %{version}-%{release}

%description examples
Example AppArmor profiles.

%description examples -l pl
Przyk³adowe profile AppArmor.

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
%dir %{_sysconfdir}/apparmor.d
%dir %{_sysconfdir}/apparmor.d/abstractions
%dir %{_sysconfdir}/apparmor.d/program-chunks
%dir %{_sysconfdir}/apparmor.d/tunables
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/tunables/*

%files abstractions
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/*

%files examples
%defattr(644,root,root,755)
%dir %{extras_dir}
%config(noreplace) %verify(not md5 mtime size) %{extras_dir}/*
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/*.*
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/program-chunks/*
