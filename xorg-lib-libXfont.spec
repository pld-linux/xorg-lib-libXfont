Summary:	X font library used by the X server
Summary(pl.UTF-8):	Używana przez X serwer biblioteka fontów X
Name:		xorg-lib-libXfont
Version:	1.3.2
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXfont-%{version}.tar.bz2
# Source0-md5:	64f510ebf9679f3a97a3d633cbee4f50
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libfontenc-devel
BuildRequires:	xorg-lib-xtrans-devel
BuildRequires:	xorg-proto-fontcacheproto-devel
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-util-util-macros
Obsoletes:	libXfont
Obsoletes:	xorg-app-mkcfm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X font library used by the X server.

%description -l pl.UTF-8
Używana przez X serwer biblioteka fontów X.

%package devel
Summary:	Header files for libXfont library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXfont
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	freetype-devel >= 2
Requires:	xorg-lib-libfontenc-devel
Requires:	xorg-lib-xtrans-devel
Requires:	xorg-proto-fontsproto-devel
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
Summary:	Static libXfont libraries
Summary(pl.UTF-8):	Biblioteki statyczne libXfont
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
	--enable-type1

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libXfont.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXfont.so
%{_libdir}/libXfont.la
%{_includedir}/X11/fonts/*.h
%{_pkgconfigdir}/xfont.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXfont.a
