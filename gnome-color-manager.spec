Summary:	Color management tools for GNOME
Name:		gnome-color-manager
Version:	2.91.90
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-color-manager/2.91/%{name}-%{version}.tar.bz2
# Source0-md5:	dda18a8c6a07bf54276ee481dab83091
URL:		http://projects.gnome.org/gnome-color-manager/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.9
BuildRequires:	cups-devel
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils
BuildRequires:	exiv2-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gnome-common
BuildRequires:	gnome-control-center-devel >= 2.91.90
BuildRequires:	gnome-doc-utils
BuildRequires:	gnome-settings-daemon-devel >= 2.91.90
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	intltool >= 0.35.0
BuildRequires:	lcms2-devel
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
BuildRequires:	vte-devel >= 0.27.0
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	dconf
Requires:	hicolor-icon-theme
Requires:	polkit-gnome
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Color Manager is a session framework for the GNOME desktop
environment that makes it easy to manage easy to manage, install and
generate color profiles.

%package devel
Summary:	GNOME Color Manager development files
Summary(pl.UTF-8):	Pliki programistyczne GNOME Color Manager
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.26.0
Requires:	lcms2-devel
Requires:	libusb-devel
Requires:	udev-glib-devel

%description devel
GNOME Color Manager development files.

%description devel -l pl.UTF-8
Pliki programistyczne GNOME Color Manager.

%package apidocs
Summary:	color-glib library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki color-glib
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
color-glib library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki color-glib.

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
	--disable-schemas-compile \
	--disable-static \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_libdir}/gnome-settings-daemon-{2,3}.0

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/control-center-1/panels/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnome-settings-daemon-3.0/*.la

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
%attr(755,root,root) %{_bindir}/gcm-apply
%attr(755,root,root) %{_bindir}/gcm-import
%attr(755,root,root) %{_bindir}/gcm-inspect
%attr(755,root,root) %{_bindir}/gcm-picker
%attr(755,root,root) %{_bindir}/gcm-viewer
%attr(755,root,root) %{_bindir}/gcm-session
%attr(755,root,root) %{_libdir}/libcolor-glib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcolor-glib.so.1
%attr(755,root,root) %{_libexecdir}/gcm-helper-exiv
%attr(755,root,root) %{_libdir}/control-center-1/panels/libcolor.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libcolor.so
%{_libdir}/gnome-settings-daemon-3.0/color.gnome-settings-plugin
%attr(755,root,root) %{_sbindir}/gcm-install-system-wide
%attr(755,root,root) /lib/udev/gcm-udev-ddc
/lib/udev/rules.d/55-gcm-i2c.rules
/lib/udev/rules.d/95-gcm-colorimeters.rules
/lib/udev/rules.d/95-gcm-devices.rules
%{_sysconfdir}/xdg/autostart/gcm-apply.desktop
%{_datadir}/GConf/gsettings/org.gnome.color-manager.gschema.migrate
%{_datadir}/dbus-1/services/org.gnome.ColorManager.service
%{_datadir}/glib-2.0/schemas/org.gnome.color-manager.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.color.gschema.xml
%{_datadir}/gnome-color-manager
%{_datadir}/polkit-1/actions/org.gnome.color.policy
%{_desktopdir}/gcm-import.desktop
%{_desktopdir}/gcm-prefs.desktop
%{_desktopdir}/gcm-viewer.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_mandir}/man1/*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcolor-glib.so
%{_datadir}/dbus-1/interfaces/org.gnome.ColorManager.xml
%{_includedir}/libcolor-glib
%{_pkgconfigdir}/libcolor-glib.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libcolor-glib
