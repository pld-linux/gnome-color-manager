Summary:	Color management tools for GNOME
Name:		gnome-color-manager
Version:	3.10.1
Release:	3
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-color-manager/3.10/%{name}-%{version}.tar.xz
# Source0-md5:	7a15c12b32604430d84759204555e6eb
URL:		http://projects.gnome.org/gnome-color-manager/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	clutter-devel >= 1.12.0
BuildRequires:	clutter-gtk-devel
BuildRequires:	colord-devel >= 0.1.34
BuildRequires:	colord-gtk-devel >= 0.1.20
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils
BuildRequires:	exiv2-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gnome-common
BuildRequires:	gnome-desktop-devel >= 3.0.0
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	intltool >= 0.40.0
BuildRequires:	lcms2-devel >= 2.2
BuildRequires:	libcanberra-gtk3-devel >= 0.10
BuildRequires:	libexif-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	mash-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	tar >= 1:1.22
BuildRequires:	vte-devel >= 0.28.0
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	colord >= 0.1.34
Requires:	dconf
Requires:	hicolor-icon-theme
Requires:	polkit-gnome
Suggests:	shared-color-profiles
Obsoletes:	gnome-color-manager-devel
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
%attr(755,root,root) %{_bindir}/gcm-viewer
%attr(755,root,root) %{_libexecdir}/gcm-helper-exiv
%{_datadir}/appdata/gcm-viewer.appdata.xml
%{_datadir}/gnome-color-manager
%{_desktopdir}/gcm-calibrate.desktop
%{_desktopdir}/gcm-import.desktop
%{_desktopdir}/gcm-picker.desktop
%{_desktopdir}/gcm-viewer.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_mandir}/man1/*.1*
