#
# Conditional build:
%bcond_without	static_libs	# static libraries
#
Summary:	Multiprocess IPC library
Summary(pl.UTF-8):	Biblioteka komunikacji międzyprocesowej
Name:		libmultiprocess
Version:	0
%define	gitref	9f4dac644acfd79e532a7da54b5e1363d555a5cc
%define	snap	20220110
%define	rel	4
Release:	0.%{snap}.%{rel}
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/chaincodelabs/libmultiprocess/releases
Source0:	https://github.com/chaincodelabs/libmultiprocess/archive/%{gitref}/%{name}-%{snap}.tar.gz
# Source0-md5:	0380ba289853ee950e6b4415552f57ca
Patch0:		%{name}-cmake.patch
URL:		https://github.com/chaincodelabs/libmultiprocess
BuildRequires:	capnproto-c++-devel
BuildRequires:	cmake >= 3.0
BuildRequires:	libstdc++-devel >= 6:7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmultiprocess is a C++ library and code generator making it easy to
call functions and reference objects in different processes.

%description -l pl.UTF-8
libmultiprocess to biblioteka i generator kodu C++, ułatwiająca
wywoływanie funkcji i obiektów referencyjnych w różnych procesach.

%package devel
Summary:	Header files for libmultiprocess library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libmultiprocess
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	capnproto-c++-devel
Requires:	libstdc++-devel >= 6:7

%description devel
Header files for libmultiprocess library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libmultiprocess.

%prep
%setup -q -n %{name}-%{gitref}
%patch -P0 -p1

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_LIBDIR=%{_lib}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README.md
%attr(755,root,root) %{_libdir}/libmultiprocess.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmultiprocess.so.0

%files devel
%defattr(644,root,root,755)
%doc doc/{design,usage}.md
%attr(755,root,root) %{_bindir}/mpgen
%attr(755,root,root) %{_libdir}/libmultiprocess.so
%{_includedir}/mp
%{_includedir}/mpgen.mk
%{_pkgconfigdir}/libmultiprocess.pc
%{_libdir}/cmake/Multiprocess
