Summary:	Color management tools for GNOME
Summary(pl.UTF-8):	Narzędzia do zarządzania kolorami dla GNOME
Name:		gnome-color-manager
Version:	3.20.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-color-manager/3.20/%{name}-%{version}.tar.xz
# Source0-md5:	e9900077c337b6cb9879ef21bbf29a1f
# rpm glob again has some problem with absolute symlinks (dead at the time of packaging);
# use relative ones (they don't go across /)
Patch0:		%{name}-symlinks.patch
# dead, wiki.gnome.org GnomeColorManager page is in Attic too
#URL:		http://projects.gnome.org/gnome-color-manager/
URL:		https://github.com/GNOME/gnome-color-manager
BuildRequires:	appstream-glib-devel
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	colord-devel >= 1.3.1
BuildRequires:	colord-gtk-devel >= 0.1.20
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils
BuildRequires:	exiv2-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gnome-common
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	intltool >= 0.40.0
BuildRequires:	lcms2-devel >= 2.2
BuildRequires:	libcanberra-gtk3-devel >= 0.10
BuildRequires:	libexif-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	tar >= 1:1.22
BuildRequires:	vte-devel >= 0.28.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.32.0
Requires:	colord >= 1.3.1
Requires:	colord-gtk >= 0.1.20
Requires:	glib2 >= 1:2.32.0
Requires:	hicolor-icon-theme
Requires:	lcms2 >= 2.2
Requires:	libcanberra-gtk3 >= 0.10
Requires:	vte >= 0.28.0
Suggests:	shared-color-profiles
Obsoletes:	gnome-color-manager-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Color Manager is a session framework for the GNOME desktop
environment that makes it easy to manage easy to manage, install and
generate color profiles.

%description -l pl.UTF-8
GNOME Color Manager to szkielet sesyjny dla środowiska graficznego
GNOME ułatwiający zarządzanie, instalowanie i generowanie profili
kolorów.

%prep
%setup -q
%patch0 -p1

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

%find_lang %{name} --with-gnome

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
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
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
%{_iconsdir}/hicolor/*x*/apps/gnome-color-manager.png
%{_iconsdir}/hicolor/*/mimetypes/application-vnd.iccprofile.png
%{_iconsdir}/hicolor/scalable/apps/gnome-color-manager.svg
%{_iconsdir}/hicolor/scalable/mimetypes/application-vnd.iccprofile.svg
%{_mandir}/man1/gcm-calibrate.1*
%{_mandir}/man1/gcm-import.1*
%{_mandir}/man1/gcm-inspect.1*
%{_mandir}/man1/gcm-picker.1*
%{_mandir}/man1/gcm-viewer.1*
