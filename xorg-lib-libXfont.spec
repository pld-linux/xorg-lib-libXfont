
#
Summary:	X font library used by the X server
Summary(pl):	U¿ywana przez X serwer biblioteka fontów X
Name:		xorg-lib-libXfont
Version:	0.99.0
Release:	0.03
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXfont-%{version}.tar.bz2
# Source0-md5:	7566ddf06a209656c0e4814d5739e8c1
Patch0:		libXfont-freebsd.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-proto-fontcacheproto-devel
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	freetype-devel
BuildRequires:	xorg-lib-libfontenc-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-util-util-macros
BuildRequires:	xorg-lib-xtrans-devel
Obsoletes:	libXfont
BuildRoot:	%{tmpdir}/libXfont-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
X font libary used by the X server.

%description -l pl
U¿ywana przez X serwer biblioteka fontów X.


%package devel
Summary:	Header files libXfont development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXfont
Group:		X11/Development/Libraries
Requires:	xorg-lib-libXfont = %{version}-%{release}
Requires:	xorg-proto-fontcacheproto-devel
Requires:	xorg-proto-fontsproto-devel
Requires:	freetype-devel
Requires:	xorg-lib-libfontenc-devel
Requires:	xorg-lib-xtrans-devel
Obsoletes:	libXfont-devel


%description devel
X font libary used by the X server.

This package contains the header files needed to develop programs that
use these libXfont.

%description devel -l pl
U¿ywana przez X serwer biblioteka fontów X.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXfont.


%package static
Summary:	Static libXfont libraries
Summary(pl):	Biblioteki statyczne libXfont
Group:		Development/Libraries
Requires:	xorg-lib-libXfont-devel = %{version}-%{release}
Obsoletes:	libXfont-static

%description static
X font libary used by the X server.

This package contains the static libXfont library.

%description static -l pl
U¿ywana przez X serwer biblioteka fontów X.

Pakiet zawiera statyczn± bibliotekê libXfont.


%prep
%setup -q -n libXfont-%{version}
%patch0 -p1


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
%attr(755,root,wheel) %{_libdir}/libXfont.so.*
%attr(755,root,wheel) %{_libdir}/libfontcache.so.*


%files devel
%defattr(644,root,root,755)
%{_includedir}/X11/fonts/*.h
%{_libdir}/libXfont.la
%{_libdir}/libfontcache.la
%attr(755,root,wheel) %{_libdir}/libXfont.so
%attr(755,root,wheel) %{_libdir}/libfontcache.so
%{_pkgconfigdir}/xfont.pc


%files static
%defattr(644,root,root,755)
%{_libdir}/libXfont.a
%{_libdir}/libfontcache.a
