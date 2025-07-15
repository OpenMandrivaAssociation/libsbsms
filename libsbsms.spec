%define		major     2
%define		libname %mklibname sbsms %{major}
%define		develname %mklibname sbsms -d

Summary:	Subband Sinusoidal Modeling Synthesis
Name:		libsbsms
Version:	2.3.0
Release:	1
License:	GPLv2+
Group:	Sound
Url:		https://github.com/claytonotey/libsbsms
Source0:	https://github.com/claytonotey/libsbsms/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	pkgconfig(sndfile)

%description
This is a library for high quality time and pitch scale modification. It is
based on octave subband sinusoidal modeling and resynthesis. It stitches
tracks between subbands, and it has multiple stages of analysis and
resynthesis.
This branch is mostly for maintaning use in Audacity and its descendant.

#------------------------------------------------

%package -n %{libname}
Summary:		Subband Sinusoidal Modeling Synthesis
Group:	System/Libraries

%description -n %{libname}
This is a library for high quality time and pitch scale modification. It is
based on octave subband sinusoidal modeling and resynthesis. It stitches
tracks between subbands, and it has multiple stages of analysis and
resynthesis.
This package contains the main library.

%files -n %{libname}
%doc AUTHORS ChangeLog NEWS README.md TODO
%license LICENSE.txt
%{_libdir}/%{name}.so.%{major}*

#------------------------------------------------

%package -n %{develname}
Summary:		Development package for %{name}
Group:	Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	sbsms-devel = %{version}-%{release}

%description -n %{develname}
Header files for development with %{name}.

%files -n %{develname}
%doc AUTHORS TODO
%{_includedir}/sbsms.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/sbsms.pc
%{_libdir}/cmake/sbsms/

#------------------------------------------------

%prep
%autosetup -p1

sed -i 's|lib/cmake/sbsms|%{_lib}/cmake/sbsms|' CMakeLists.txt


%build
%cmake
%make_build


%install
%make_install -C build
