%define Werror_cflags	%nil
%define	name	torcs
%define	oname	TORCS
%define	libname	%mklibname %{name}
%define	version	1.3.5
%define	release	1.1
%define	Summary	The Open Racing Car Simulator

Name:		%{name}
Version:	%{version}
Release:%{release}
Summary:	%{Summary}
License:	GPLv2
Group:		Games/Arcade
Source0:	%{oname}-%{version}-src.tgz
Source1:	%{oname}-%{version}-src-robots-base.tgz
Source2:	%{oname}-1.3.0-src-robots-berniw.tar.bz2
Source3:	%{oname}-1.3.0-src-robots-bt.tar.bz2
Source4:	%{oname}-1.3.0-src-robots-olethros.tar.bz2

URL:		http://torcs.sourceforge.net/
Provides:	%{oname}
Requires:	%{name}-data = %{version}
Requires:	%{name}-data-cars-extra 
Requires:	%{name}-robots-berniw %{name}-robots-bt %{name}-robots-olethros

BuildRequires:	imagemagick 
BuildRequires:	pkgconfig(glu) 
BuildRequires:	pkgconfig(sdl) 
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libpng) 
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	mesa-common-devel 
BuildRequires:	plib-devel 
BuildRequires:	pkgconfig(freealut) 
BuildRequires:	pkgconfig(openal) 
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(ice)
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xmu)


Provides:	%{libname}
Obsoletes:	%{libname}

%description
A 3D racing car simulator using OpenGL.

%package	robots-base
Group:		Games/Arcade
Requires:	%{name} >= %{version}
Summary:	Basic robots for %{name}
Provides:	%{name}-robots

%description	robots-base
Base robots for %{oname}
%package	robots-berniw
Group:		Games/Arcade
Requires:	%{name} >= %{version}
Summary:	Berniw robots for %{name}
Provides:	%{name}-robots

%description	robots-berniw
Berniw robots for %{oname}
by Bernhard Wymann <berniw@bluewin.ch>

%package	robots-bt
Group:		Games/Arcade
Requires:	%{name} >= %{version}
Summary:	Bt robots for %{name}
Provides:	%{name}-robots

%description	robots-bt
bt robots for %{oname}

%package	robots-olethros
Group:		Games/Arcade
Requires:	%{name} >= %{version}
Summary:	Olethros robots for %{name}
Provides:	%{name}-robots

%description	robots-olethros
bt robots for %{oname}
by Christos Dimitrakakis <dimitrak@idiap.ch>


%prep
%setup -q -b1 -b2 -b3 -b4

%build
LDFLAGS="%{ldflags} -lstdc++"
./configure	--bindir=%{_gamesbindir} \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--x-libraries=%{_xorglibdir}
	
#avoid paralel build
make

%install
%{makeinstall_std}

mkdir $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{oname}
Comment=%{Summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=Game;ArcadeGame;
EOF

%{__install} -d $RPM_BUILD_ROOT{%{_miconsdir},%{_liconsdir}}
convert -size 16x16 icon.png $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
%{__install} icon.png $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
convert -size 48x48 icon.png $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

# fix rpmlint E, to be seen for W
chmod -R 755 $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}
chmod -R 755 $RPM_BUILD_ROOT%{_libdir}/%{name}

%files
%doc COPYING README 
%{_gamesbindir}/*
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/[!d]*
%{_datadir}/applications/mandriva-%{name}.desktop
%dir %{_gamesdatadir}/%{name}/drivers
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_libdir}/%{name}

%files robots-base
%doc COPYING README 
%{_gamesdatadir}/%{name}/drivers/damned*
%{_gamesdatadir}/%{name}/drivers/human/*              
%{_gamesdatadir}/%{name}/drivers/inferno/*
%{_gamesdatadir}/%{name}/drivers/inferno2/*
%{_gamesdatadir}/%{name}/drivers/lliaw/*
%{_gamesdatadir}/%{name}/drivers/sparkle/*
%{_gamesdatadir}/%{name}/drivers/tita/*

%files robots-berniw
%doc COPYING README 
%{_gamesdatadir}/%{name}/drivers/berniw*

%files robots-bt
%doc COPYING README 
%{_gamesdatadir}/%{name}/drivers/bt

%files robots-olethros
%doc COPYING README 
%{_gamesdatadir}/%{name}/drivers/olethros


