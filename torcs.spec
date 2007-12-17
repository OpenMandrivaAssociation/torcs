%define	name	torcs
%define	oname	TORCS
%define	libname	%mklibname %{name}
%define	version	1.3.0
%define	release	4
%define	Summary	The Open Racing Car Simulator

Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
Summary:	%{Summary}
License:	GPL
Group:		Games/Arcade
Source0:	%{oname}-%{version}-src.tar.bz2
Source1:	%{oname}-%{version}-src-robots-base.tar.bz2
Source2:	%{oname}-%{version}-src-robots-berniw.tar.bz2
Source3:	%{oname}-%{version}-src-robots-bt.tar.bz2
Source4:	%{oname}-%{version}-src-robots-olethros.tar.bz2
URL:		http://torcs.sourceforge.net/
Provides:	%{oname}
Requires:	%{name}-data = %{version} %{name}-robots-base
Requires:	%{name}-data-cars-extra %{name}-robots-berniw %{name}-robots-bt %{name}-robots-olethros
BuildRequires:	ImageMagick mesaglu-devel SDL-devel zlib-devel png-devel
BuildRequires:	mesa-common-devel plib-devel freealut-devel openal-devel libxrandr-devel
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
Summary:	bt robots for %{name}
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
%configure	--bindir=%{_gamesbindir}
%make || %make

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{makeinstall_std}


mkdir $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{oname}
Comment=%{Summary}
Exec=soundwrapper %{_gamesbindir}/%{name}
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

%post
%{update_menus}
 
%postun
%{clean_menus} 

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,755)
%doc INSTALL.linux README.linux
%{_gamesbindir}/*
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/[!d]*
%{_datadir}/applications/mandriva-%{name}.desktop
%dir %{_gamesdatadir}/%{name}/drivers
%{_gamesdatadir}/%{name}/drivers/human
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_libdir}/%{name}

%files robots-base
%defattr(-,root,root,755)
%{_gamesdatadir}/%{name}/drivers/cylos1
%{_gamesdatadir}/%{name}/drivers/damned
%{_gamesdatadir}/%{name}/drivers/inferno
%{_gamesdatadir}/%{name}/drivers/inferno2
%{_gamesdatadir}/%{name}/drivers/lliaw
%{_gamesdatadir}/%{name}/drivers/tanhoj
%{_gamesdatadir}/%{name}/drivers/tita
%{_gamesdatadir}/%{name}/drivers/sparkle

%files robots-berniw
%defattr(-,root,root,755)
%{_gamesdatadir}/%{name}/drivers/berniw*

%files robots-bt
%defattr(-,root,root,755)
%{_gamesdatadir}/%{name}/drivers/bt

%files robots-olethros
%defattr(-,root,root,755)
%{_gamesdatadir}/%{name}/drivers/olethros


