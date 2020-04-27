Summary:	Color management tools for GNOME
Summary(pl.UTF-8):	Narzędzia do zarządzania kolorami dla GNOME
Name:		gnome-color-manager
Version:	3.36.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-color-manager/3.36/%{name}-%{version}.tar.xz
# Source0-md5:	c5360705a68e88455b1801200e9aaa2e
URL:		https://gitlab.gnome.org/GNOME/gnome-color-manager
BuildRequires:	colord-devel >= 1.3.1
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils
BuildRequires:	exiv2-devel
BuildRequires:	gettext-tools >= 0.19.7
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	lcms2-devel >= 2.2
BuildRequires:	libcanberra-gtk3-devel >= 0.10
BuildRequires:	libexif-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel >= 4
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.46.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.32.0
Requires:	colord >= 1.3.1
Requires:	glib2 >= 1:2.32.0
Requires:	hicolor-icon-theme
Requires:	lcms2 >= 2.2
Requires:	libcanberra-gtk3 >= 0.10
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

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

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
%doc AUTHORS MAINTAINERS README
%attr(755,root,root) %{_bindir}/gcm-import
%attr(755,root,root) %{_bindir}/gcm-inspect
%attr(755,root,root) %{_bindir}/gcm-picker
%attr(755,root,root) %{_bindir}/gcm-viewer
%{_datadir}/gnome-color-manager
%{_datadir}/metainfo/org.gnome.ColorProfileViewer.appdata.xml
%{_desktopdir}/gcm-import.desktop
%{_desktopdir}/gcm-picker.desktop
%{_desktopdir}/org.gnome.ColorProfileViewer.desktop
%{_iconsdir}/hicolor/*x*/apps/gnome-color-manager.png
%{_iconsdir}/hicolor/scalable/apps/gnome-color-manager.svg
%{_mandir}/man1/gcm-import.1*
%{_mandir}/man1/gcm-inspect.1*
%{_mandir}/man1/gcm-picker.1*
%{_mandir}/man1/gcm-viewer.1*
