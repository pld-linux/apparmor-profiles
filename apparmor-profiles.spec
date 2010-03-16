Summary:	AppArmor profiles
Summary(pl.UTF-8):	Profile AppArmor
Name:		apparmor-profiles
Version:	2.5
Release:	1
Epoch:		1
Group:		Base
Source0:	http://kernel.org/pub/linux/security/apparmor/AppArmor-%{version}/AppArmor-%{version}.tgz
# Source0-md5:	4a747d1a1f85cb272d55b52c7e8a4a02
License:	GPL
URL:		http://apparmor.wiki.kernel.org/
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

%description -l pl.UTF-8
Podstawowe profile AppArmor (zwane także polityką bezpieczeństwa).
AppArmor to mechanizm obowiązkowej kontroli dostępu do plików.
AppArmor ogranicza procesy do zasobów udostępnionych przez
administratora systemu i może ograniczać zakres potencjalnych luk w
bezpieczeństwie. Ten pakiet jest częścią zestawu narzędzi zwanych
SubDomain.

%package abstractions
Summary:	Abstraction AppArmor files
Summary(pl.UTF-8):	Pliki abstrakcji dla AppArmor
Group:		Base
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description abstractions
Abstraction AppArmor files.

%description abstractions -l pl.UTF-8
Pliki abstrakcji dla AppArmor.

%package examples
Summary:	Example AppArmor profiles
Summary(pl.UTF-8):	Przykładowe profile AppArmor
Group:		Base
Requires:	%{name}-abstractions = %{epoch}:%{version}-%{release}

%description examples
Example AppArmor profiles.

%description examples -l pl.UTF-8
Przykładowe profile AppArmor.

%prep
%setup -q -n AppArmor-%{version}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C profiles install \
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
