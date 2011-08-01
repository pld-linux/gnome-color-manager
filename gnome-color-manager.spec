Summary:	Color management tools for GNOME
Name:		gnome-color-manager
Version:	3.1.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-color-manager/3.1/%{name}-%{version}.tar.bz2
# Source0-md5:	30684b49a17812cb7fe2f3def872caa9
URL:		http://projects.gnome.org/gnome-color-manager/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.9
BuildRequires:	colord-devel
BuildRequires:	cups-devel
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils
BuildRequires:	exiv2-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gnome-common
BuildRequires:	gnome-control-center-devel >= 3.0.0
BuildRequires:	gnome-doc-utils
BuildRequires:	gnome-settings-daemon-devel >= 3.0.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	intltool >= 0.35.0
BuildRequires:	lcms2-devel >= 2.2
BuildRequires:	libcanberra-gtk3-devel >= 0.10
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libusb-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	sane-backends-devel
BuildRequires:	udev-glib-devel
BuildRequires:	vte-devel >= 0.28.0
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	colord
Requires:	dconf
Requires:	hicolor-icon-theme
Requires:	polkit-gnome
Suggests:	shared-color-profiles
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Color Manager is a session framework for the GNOME desktop
environment that makes it easy to manage easy to manage, install and
generate color profiles.

%prep
%setup -q

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-schemas-compile \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_icon_cache hicolor
%update_desktop_database_post
%glib_compile_schemas

%postun
/sbin/ldconfig
%update_icon_cache hicolor
%update_desktop_database_postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gcm-calibrate
%attr(755,root,root) %{_bindir}/gcm-import
%attr(755,root,root) %{_bindir}/gcm-inspect
%attr(755,root,root) %{_bindir}/gcm-picker
%attr(755,root,root) %{_bindir}/gcm-session
%attr(755,root,root) %{_bindir}/gcm-viewer
%attr(755,root,root) %{_libexecdir}/gcm-helper-exiv
%{_sysconfdir}/xdg/autostart/gcm-session.desktop
%{_datadir}/gnome-color-manager
%{_datadir}/dbus-1/interfaces/org.gnome.ColorManager.xml
%{_datadir}/dbus-1/services/org.gnome.ColorManager.service
%{_desktopdir}/gcm-calibrate.desktop
%{_desktopdir}/gcm-import.desktop
%{_desktopdir}/gcm-picker.desktop
%{_desktopdir}/gcm-viewer.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_mandir}/man1/*.1*
