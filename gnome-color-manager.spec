Summary:	GNOME solution for scanning
Name:		gnome-color-manager
Version:	2.29.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-color-manager/2.29/%{name}-%{version}.tar.bz2
# Source0-md5:	2f28c20e952a807b062010d641aaa788
URL:		http://projects.gnome.org/gnome-color-manager/
BuildRequires:	GConf2-devel >= 2.22.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.73
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.14.0
BuildRequires:	gnome-common
BuildRequires:	gnome-desktop-devel >= 2.14.0
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	gtk-doc >= 1.7
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libunique-devel >= 1.0.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	udev-glib-devel
BuildRequires:	vte-devel >= 0.22.2
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
Requires(post,postun):	hicolor-icon-theme
Requires(post,preun):	GConf2
Requires:	gtk+2 >= 2:2.14.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Color Manager is a session framework for the GNOME desktop
environment that makes it easy to manage easy to manage, install and
generate color profiles.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%gconf_schema_install gnome-color-manager.schemas

%preun
%gconf_schema_uninstall gnome-color-manager.schemas

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gcm-apply
%attr(755,root,root) %{_bindir}/gcm-dump-edid
%attr(755,root,root) %{_bindir}/gcm-dump-profile
%attr(755,root,root) %{_bindir}/gcm-import
%attr(755,root,root) %{_bindir}/gcm-inspect
%attr(755,root,root) %{_bindir}/gcm-prefs
%attr(755,root,root) %{_bindir}/gcm-session
%{_sysconfdir}/gconf/schemas/gnome-color-manager.schemas
%{_sysconfdir}/xdg/autostart/gcm-apply.desktop
%{_datadir}/dbus-1/services/org.gnome.ColorManager.service
%{_datadir}/gnome-color-manager
%{_desktopdir}/gcm-import.desktop
%{_desktopdir}/gcm-prefs.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_mandir}/man1/*.1*
