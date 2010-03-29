Summary:	Color management tools for GNOME
Name:		gnome-color-manager
Version:	2.30.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-color-manager/2.30/%{name}-%{version}.tar.bz2
# Source0-md5:	ef6262e7946c714c0919907ad8ce8078
URL:		http://projects.gnome.org/gnome-color-manager/
BuildRequires:	GConf2-devel >= 2.22.0
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
BuildRequires:	cups-devel
BuildRequires:	dbus-glib-devel >= 0.73
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.14.0
BuildRequires:	gnome-common
BuildRequires:	gnome-desktop-devel >= 2.14.0
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	intltool >= 0.35.0
BuildRequires:	lcms-devel
BuildRequires:	libcanberra-gtk-devel >= 0.10
BuildRequires:	libnotify-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libunique-devel >= 1.0.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	sane-backends-devel
BuildRequires:	udev-glib-devel
BuildRequires:	vte-devel >= 0.22.2
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	hicolor-icon-theme
Requires(post,preun):	GConf2
Requires:	gtk+2 >= 2:2.14.0
Requires:	polkit-gnome
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Color Manager is a session framework for the GNOME desktop
environment that makes it easy to manage easy to manage, install and
generate color profiles.

%prep
%setup -q

%build
mkdir m4
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database_post
%gconf_schema_install gnome-color-manager.schemas

%preun
%gconf_schema_uninstall gnome-color-manager.schemas

%postun
%update_icon_cache hicolor
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gcm-apply
%attr(755,root,root) %{_bindir}/gcm-dump-edid
%attr(755,root,root) %{_bindir}/gcm-dump-profile
%attr(755,root,root) %{_bindir}/gcm-fix-profile
%attr(755,root,root) %{_bindir}/gcm-import
%attr(755,root,root) %{_bindir}/gcm-inspect
%attr(755,root,root) %{_bindir}/gcm-prefs
%attr(755,root,root) %{_bindir}/gcm-session
%attr(755,root,root) %{_sbindir}/gcm-install-system-wide
/lib/udev/rules.d/95-gcm-colorimeters.rules
/lib/udev/rules.d/95-gcm-devices.rules
%{_sysconfdir}/gconf/schemas/gnome-color-manager.schemas
%{_sysconfdir}/xdg/autostart/gcm-apply.desktop
%{_datadir}/dbus-1/services/org.gnome.ColorManager.service
%{_datadir}/gnome-color-manager
%{_datadir}/polkit-1/actions/org.gnome.color.policy
%{_desktopdir}/gcm-import.desktop
%{_desktopdir}/gcm-prefs.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_mandir}/man1/*.1*
