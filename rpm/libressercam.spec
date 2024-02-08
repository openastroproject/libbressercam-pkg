%define debug_package %{nil}

Name:           libbressercam
Version:        1.55.24621
Release:        0
Summary:        Bresser camera support library
License:	GPLv2+
Prefix:         %{_prefix}
Provides:       libbressercam = %{version}-%{release}
Obsoletes:      libbressercam < 1.55.24621
Source:         libbressercam-%{version}.tar.gz
Patch0:         pkg-config.patch
Patch1:         udev-rules.patch

%description
libbressercam is a user-space driver for Bresser astronomy cameras.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       libbressercam-devel = %{version}-%{release}
Obsoletes:      libbressercam-devel < 1.55.24621

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build

sed -e "s!@LIBDIR@!%{_libdir}!g" -e "s!@VERSION@!%{version}!g" < \
    libbressercam.pc.in > libbressercam.pc

%install
mkdir -p %{buildroot}%{_libdir}/pkgconfig
mkdir -p %{buildroot}/etc/udev/rules.d
mkdir -p %{buildroot}%{_includedir}

case %{_arch} in
  x86_64)
    cp x64/libbressercam.so %{buildroot}%{_libdir}/libbressercam.so.%{version}
		cp bressercam.h %{buildroot}%{_includedir}
    ;;
  *)
    echo "unknown target architecture %{_arch}"
    exit 1
    ;;
esac

ln -sf %{name}.so.%{version} %{buildroot}%{_libdir}/%{name}.so.1
cp *.pc %{buildroot}%{_libdir}/pkgconfig
cp 70-bresser-cameras.rules %{buildroot}/etc/udev/rules.d

%post
/sbin/ldconfig
/sbin/udevadm control --reload-rules

%postun
/sbin/ldconfig
/sbin/udevadm control --reload-rules

%files
%{_libdir}/*.so.*
%{_sysconfdir}/udev/rules.d/*.rules

%files devel
%{_includedir}/bressercam.h
%{_libdir}/pkgconfig/*.pc

%changelog
* Thu Feb 8 2024 James Fidell <james@openastroproject.org> - 1.55.24621-0
- Initial RPM release
* Sat Jan 6 2024 James Fidell <james@openastroproject.org> - 1.55.24239-0
- Initial RPM release

