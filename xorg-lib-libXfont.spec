Summary:	X font library used by the X server
Summary(pl):	U¿ywana przez X serwer biblioteka fontów X
Name:		xorg-lib-libXfont
Version:	0.99.0
Release:	0.03
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXfont-%{version}.tar.bz2
# Source0-md5:	7566ddf06a209656c0e4814d5739e8c1
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-lib-libfontenc-devel
BuildRequires:	xorg-lib-xtrans-devel
BuildRequires:	xorg-proto-fontcacheproto-devel
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-util-util-macros
Obsoletes:	libXfont
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
X font library used by the X server.

%description -l pl
U¿ywana przez X serwer biblioteka fontów X.

%package devel
Summary:	Header files libXfont development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXfont
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-proto-fontcacheproto-devel
Requires:	xorg-proto-fontsproto-devel
Requires:	freetype-devel
Requires:	xorg-lib-libfontenc-devel
Requires:	xorg-lib-xtrans-devel
Obsoletes:	libXfont-devel

%description devel
X font library used by the X server.

This package contains the header files needed to develop programs that
use these libXfont.

%description devel -l pl
U¿ywana przez X serwer biblioteka fontów X.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXfont.

%package static
Summary:	Static libXfont libraries
Summary(pl):	Biblioteki statyczne libXfont
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXfont-static

%description static
X font library used by the X server.

This package contains the static libXfont library.

%description static -l pl
U¿ywana przez X serwer biblioteka fontów X.

Pakiet zawiera statyczn± bibliotekê libXfont.

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
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/libXfont.so.*.*.*
%attr(755,root,root) %{_libdir}/libfontcache.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXfont.so
%attr(755,root,root) %{_libdir}/libfontcache.so
%{_libdir}/libXfont.la
%{_libdir}/libfontcache.la
%{_includedir}/X11/fonts/*.h
%{_pkgconfigdir}/xfont.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXfont.a
%{_libdir}/libfontcache.a
