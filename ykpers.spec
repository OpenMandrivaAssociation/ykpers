%global	major 1
%global libname		%mklibname ykpers
%global devname		%mklibname ykpers -d
%global oldlibname	%mklibname ykpers

%bcond_without	json

Summary:	Yubikey Personalization
Name:		ykpers
Version:	1.20.0
Release:	1
Group:		System/Libraries
License:	BSD
URL:		https://developers.yubico.com/yubikey-personalization/
Source0:	https://developers.yubico.com/yubikey-personalization/Releases/%{name}-%{version}.tar.gz
Source1:	https://developers.yubico.com/yubikey-personalization/Releases/%{name}-%{version}.tar.gz.sig
Patch0:		ykpers-args-extern.patch

BuildRequires:	libyubikey-devel
%if %{with json}
BuildRequires:	pkgconfig(json-c)
%endif
BuildRequires:	pkgconfig(libusb)
BuildRequires:	pkgconfig(udev)

%description
The YubiKey Personalization package contains a library and command line tool
used to personalize (i.e., set a AES key) YubiKeys.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	The shared Yubikey Personalization library
Group:		System/Libraries
Obsoletes:	%{oldlibname} < %{EVRD}

%description -n	%{libname}
The YubiKey Personalization package contains a library and command line tool
used to personalize (i.e., set a AES key) YubiKeys.

%files -n %{libname}
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libykpers-*.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for the Yubikey Personalization library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Requires:	%{libname} = %{version}

%description -n	%{devname}
The YubiKey Personalization package contains a library and command line tool
used to personalize (i.e., set a AES key) YubiKeys.

This package contains the development files for the ykpers library.

%files -n %{devname}
%dir %{_includedir}/ykpers-1
%{_includedir}/ykpers-1/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

#----------------------------------------------------------------------------

%package tools
Summary:	Command line tools for ykpers
Group:		System/Libraries

%description tools
The YubiKey Personalization package contains a library and command line tool
used to personalize (i.e., set a AES key) YubiKeys.

This package contains various tools for ykpers.

%files tools
%{_bindir}/ykchalresp
%{_bindir}/ykinfo
%{_bindir}/ykpersonalize
%{_mandir}/man1/*
%{_udevrulesdir}/69-yubikey.rules

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%configure \
	--enable-static=no \
    --with-udevrulesdir=%{_udevrulesdir} \
    --with-backend=libusb \
	--with%{?!with_json:out}-json
%make_build

%install
%make_install

