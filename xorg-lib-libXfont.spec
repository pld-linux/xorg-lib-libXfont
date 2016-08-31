Summary:	X font library used by the X server
Summary(pl.UTF-8):	Używana przez X serwer biblioteka fontów X
Name:		xorg-lib-libXfont
Version:	1.5.2
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXfont-%{version}.tar.bz2
# Source0-md5:	254ee42bd178d18ebc7a73aacfde7f79
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	docbook-dtd44-xml
BuildRequires:	freetype-devel >= 2
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xmlto >= 0.0.22
BuildRequires:	xorg-lib-libfontenc-devel
BuildRequires:	xorg-lib-xtrans-devel
BuildRequires:	xorg-proto-fontsproto-devel >= 2.1.3
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-sgml-doctools >= 1.7
BuildRequires:	xorg-util-util-macros >= 1.10
BuildRequires:	zlib-devel
Obsoletes:	libXfont
Obsoletes:	xorg-app-mkcfm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libXfont provides the core of the legacy X11 font system, handling the
index files (fonts.dir, fonts.alias, fonts.scale), the various font
file formats, and rasterizing them. It is used by the X servers, the X
Font Server (xfs), and some font utilities (bdftopcf for instance),
but should not be used by normal X11 clients. X11 clients access fonts
via either the new API's in libXft, or the legacy API's in libX11.

%description -l pl.UTF-8
libXfont udostępnia główną część starego systemu fontów X11,
obsługującą pliki indeksów (fonts.dir, fonts.alias, fonts.scale),
różne formaty plików fontów oraz rasteryzację ich. Jest używana przez
serwer X, serwer fontów X (xfs - X Font Server) i różne narzędzia
związane z fontami (np. bdftopcf), ale nie powinna być używana przez
normalne aplikacje klienckie X11. Te ostatnie powinny odwoływać się do
fontów przez nowe API w libXft lub stare API w libX11.

%package devel
Summary:	Header files for libXfont library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXfont
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	bzip2-devel
Requires:	freetype-devel >= 2
Requires:	xorg-lib-libfontenc-devel
Requires:	xorg-lib-xtrans-devel
Requires:	xorg-proto-fontsproto-devel >= 2.1.3
Requires:	xorg-proto-xproto-devel
Requires:	zlib-devel
Obsoletes:	libXfont-devel

%description devel
X font library used by the X server.

This package contains the header files needed to develop programs that
use libXfont.

%description devel -l pl.UTF-8
Używana przez X serwer biblioteka fontów X.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXfont.

%package static
Summary:	Static libXfont library
Summary(pl.UTF-8):	Biblioteka statyczna libXfont
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXfont-static

%description static
X font library used by the X server.

This package contains the static libXfont library.

%description static -l pl.UTF-8
Używana przez X serwer biblioteka fontów X.

Pakiet zawiera statyczną bibliotekę libXfont.

%prep
%setup -q -n libXfont-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-bzip2

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libXfont.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libXfont.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXfont.so.1

%files devel
%defattr(644,root,root,755)
%doc doc/*.html
%attr(755,root,root) %{_libdir}/libXfont.so
%{_includedir}/X11/fonts/bdfint.h
%{_includedir}/X11/fonts/bitmap.h
%{_includedir}/X11/fonts/bufio.h
%{_includedir}/X11/fonts/fntfil.h
%{_includedir}/X11/fonts/fntfilio.h
%{_includedir}/X11/fonts/fntfilst.h
%{_includedir}/X11/fonts/fontconf.h
%{_includedir}/X11/fonts/fontencc.h
%{_includedir}/X11/fonts/fontmisc.h
%{_includedir}/X11/fonts/fontshow.h
%{_includedir}/X11/fonts/fontutil.h
%{_includedir}/X11/fonts/fontxlfd.h
%{_includedir}/X11/fonts/ft.h
%{_includedir}/X11/fonts/ftfuncs.h
%{_includedir}/X11/fonts/pcf.h
%{_pkgconfigdir}/xfont.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXfont.a
