Summary:	AppArmor profiles
Summary(pl.UTF-8):	Profile AppArmor
Name:		apparmor-profiles
Version:	4.0.2
Release:	2
Epoch:		1
License:	GPL v2
Group:		Base
Source0:	https://launchpad.net/apparmor/4.0/%{version}/+download/apparmor-%{version}.tar.gz
# Source0-md5:	3ec5038b504044f714708eb074c09fce
URL:		https://wiki.apparmor.net/
Requires:	apparmor-parser
Provides:	subdomain-profiles
Obsoletes:	subdomain-profiles < 2.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		extras_dir	%{_datadir}/apparmor/extra-profiles
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
%setup -q -n apparmor-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/apparmor.d/cache

%{__make} -C profiles install \
	DESTDIR=$RPM_BUILD_ROOT \
	EXTRASDIR=$RPM_BUILD_ROOT%{extras_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{profiles_dir}
%dir %{profiles_dir}/abstractions
%dir %{profiles_dir}/abi
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abi/3.0
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abi/4.0
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abi/kernel-5.4-outoftree-network
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abi/kernel-5.4-vanilla
%dir %{profiles_dir}/cache
%dir %{profiles_dir}/local
%dir %{profiles_dir}/tunables
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/tunables/alias
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/tunables/apparmorfs
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/tunables/dovecot
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/tunables/etc
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/tunables/global
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/tunables/home
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/tunables/kernelvars
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/tunables/multiarch
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/tunables/ntpd
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/tunables/proc
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/tunables/run
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/tunables/securityfs
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/tunables/share
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/tunables/sys
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/tunables/xdg-user-dirs
%dir %{profiles_dir}/tunables/home.d
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/tunables/home.d/site.local
%dir %{profiles_dir}/tunables/multiarch.d
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/tunables/multiarch.d/site.local
%dir %{profiles_dir}/tunables/xdg-user-dirs.d
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/tunables/xdg-user-dirs.d/site.local

%files abstractions
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/apache2-common
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/aspell
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/audio
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/authentication
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/base
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/bash
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/consoles
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/crypto
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/cups-client
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/dbus
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/dbus-accessibility
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/dbus-accessibility-strict
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/dbus-network-manager-strict
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/dbus-session
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/dbus-session-strict
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/dbus-strict
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/dconf
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/dovecot-common
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/dri-common
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/dri-enumerate
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/enchant
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/exo-open
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/fcitx
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/fcitx-strict
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/fonts
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/freedesktop.org
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/gio-open
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/gnome
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/gnupg
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/groff
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/gtk
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/gvfs-open
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/hosts_access
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ibus
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/kde
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/kde-globals-write
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/kde-icon-cache-write
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/kde-language-write
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/kde-open5
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/kerberosclient
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ldapclient
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/libpam-systemd
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/likewise
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/mdns
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/mesa
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/mir
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/mozc
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/mysql
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/nameservice
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/nis
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/nss-systemd
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/nvidia
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/opencl
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/opencl-common
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/opencl-intel
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/opencl-mesa
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/opencl-nvidia
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/opencl-pocl
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/openssl
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/orbit2
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/p11-kit
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/perl
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/php
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/php-worker
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/php5
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/postfix-common
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/private-files
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/private-files-strict
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/python
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/qt5
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/qt5-compose-cache-write
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/qt5-settings-write
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/recent-documents-write
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ruby
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/samba
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/samba-rpcd
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/smbpass
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/snap_browsers
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ssl_certs
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ssl_keys
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/svn-repositories
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/transmission-common
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/trash
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ubuntu-bittorrent-clients
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ubuntu-browsers
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ubuntu-console-browsers
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ubuntu-console-email
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ubuntu-email
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ubuntu-feed-readers
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ubuntu-gnome-terminal
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ubuntu-helpers
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ubuntu-konsole
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ubuntu-media-players
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ubuntu-unity7-base
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ubuntu-unity7-launcher
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ubuntu-unity7-messaging
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ubuntu-xterm
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/user-download
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/user-mail
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/user-manpages
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/user-tmp
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/user-write
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/video
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/vulkan
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/wayland
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/web-data
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/winbind
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/wutmp
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/X
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/xad
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/xdg-desktop
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/xdg-open
%dir %{profiles_dir}/abstractions/apparmor_api
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/apparmor_api/change_profile
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/apparmor_api/examine
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/apparmor_api/find_mountpoint
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/apparmor_api/introspect
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/apparmor_api/is_enabled
%dir %{profiles_dir}/abstractions/ubuntu-browsers.d
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ubuntu-browsers.d/chromium-browser
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ubuntu-browsers.d/java
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ubuntu-browsers.d/kde
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ubuntu-browsers.d/mailto
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ubuntu-browsers.d/multimedia
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ubuntu-browsers.d/plugins-common
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ubuntu-browsers.d/productivity
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ubuntu-browsers.d/text-editors
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ubuntu-browsers.d/ubuntu-integration
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ubuntu-browsers.d/ubuntu-integration-xul
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/abstractions/ubuntu-browsers.d/user-files

%files examples
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/1password
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/balena-etcher
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/bin.ping
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/brave
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/buildah
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/busybox
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/cam
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/ch-checkns
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/chrome
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/chromium
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/ch-run
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/code
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/crun
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/devhelp
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/Discord
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/element-desktop
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/epiphany
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/evolution
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/firefox
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/flatpak
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/foliate
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/geary
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/github-desktop
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/goldendict
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/ipa_verify
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/kchmviewer
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/keybase
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/lc-compliance
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/libcamerify
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/linux-sandbox
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/loupe
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/lsb_release
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/lxc-attach
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/lxc-create
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/lxc-destroy
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/lxc-execute
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/lxc-stop
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/lxc-unshare
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/lxc-usernsexec
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/mmdebstrap
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/MongoDB_Compass
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/msedge
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/nautilus
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/notepadqq
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/nvidia_modprobe
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/obsidian
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/opam
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/opera
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/pageedit
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/php-fpm
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/plasmashell
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/podman
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/polypane
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/privacybrowser
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/qcam
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/qmapshack
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/QtWebEngineProcess
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/qutebrowser
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/rootlesskit
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/rpm
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/rssguard
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/runc
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/samba-*
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/sbin.*
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/sbuild
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/sbuild-abort
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/sbuild-adduser
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/sbuild-apt
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/sbuild-checkpackages
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/sbuild-clean
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/sbuild-createchroot
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/sbuild-destroychroot
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/sbuild-distupgrade
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/sbuild-hold
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/sbuild-shell
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/sbuild-unhold
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/sbuild-update
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/sbuild-upgrade
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/scide
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/signal-desktop
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/slack
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/slirp4netns
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/steam
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/stress-ng
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/surfshark
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/systemd-coredump
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/thunderbird
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/toybox
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/transmission
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/trinity
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/tup
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/tuxedo-control-center
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/unix-chkpwd
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/unprivileged_userns
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/userbindmount
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/usr.lib.*
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/usr.sbin.*
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/uwsgi-core
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/vdens
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/virtiofsd
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/vivaldi-bin
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/vpnns
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/wike
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/wpcom
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/zgrep
%dir %{profiles_dir}/apache2.d
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/apache2.d/phpsysinfo
%config(noreplace) %verify(not md5 mtime size) %{profiles_dir}/local/README
# XXX: top dir shared with apparmor-utils
%dir %{_datadir}/apparmor
%dir %{extras_dir}
%{extras_dir}/README
%{extras_dir}/bin.netstat
%{extras_dir}/chromium_browser
%{extras_dir}/etc.cron.daily.*
%{extras_dir}/firefox
%attr(755,root,root) %{extras_dir}/firefox.sh
%{extras_dir}/bwrap-userns-restrict
%{extras_dir}/postfix-*
%{extras_dir}/rpcbind
%{extras_dir}/sbin.*
%{extras_dir}/unshare-userns-restrict
%{extras_dir}/usr.bin.*
%{extras_dir}/usr.lib.*
%{extras_dir}/usr.lib64.GConf.2.gconfd-2
%{extras_dir}/usr.NX.bin.nxclient
%{extras_dir}/usr.sbin.*
