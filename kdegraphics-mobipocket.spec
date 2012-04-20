Name: kdegraphics-mobipocket
Summary: A collection of plugins to handle mobipocket files
Version: 4.8.2
Release: 1
Epoch: 2
Group: Graphical desktop/KDE
License: GPLv2
URL: http://www.kde.org
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.xz
BuildRequires: kdelibs4-devel >= 2:%{version}
BuildRequires: okular-devel
Conflicts: kdegraphics4-core < 2:4.6.90
Obsoletes: mobipocket < 2:4.8.0
Provides:  mobipocket = %{epoch}:%{version}:%{release}

%description
A collection of plugins to handle mobipocket files.

%files
%_kde_libdir/kde4/mobithumbnail.so
%_kde_libdir/kde4/okularGenerator_mobi.so
%_kde_libdir/strigi/strigila_mobi.so
%_kde_services/mobithumbnail.desktop
%_kde_applicationsdir/okularApplication_mobi.desktop
%_kde_services/libokularGenerator_mobi.desktop
%_kde_services/okularMobi.desktop

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 -DKDE4_ENABLE_FINAL=ON
%make

%install
rm -fr %buildroot
%makeinstall_std -C build

