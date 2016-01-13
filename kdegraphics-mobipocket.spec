Summary:	A collection of plugins to handle mobipocket files
Name:		kdegraphics-mobipocket
Version:	15.12.1
Release:	1
Epoch:		2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs-devel
BuildRequires:	pkgconfig(libstreams)
Conflicts:	kdegraiphics4-core < 2:4.6.90
Obsoletes:	mobipocket < 2:4.8.0

%description
A collection of plugins to handle mobipocket files.

%files
%doc COPYING
%{_kde_libdir}/kde4/mobithumbnail.so
%{_kde_libdir}/strigi/strigila_mobi.so
%{_kde_services}/mobithumbnail.desktop

#----------------------------------------------------------------------

%define major 1
%define libqmobipocket %mklibname qmobipocket %{major}

%package -n %{libqmobipocket}
Summary:	QMobipocket library
Group:		System/Libraries

%description -n %{libqmobipocket}
QMobipocket library.

%files -n %{libqmobipocket}
%{_kde_libdir}/libqmobipocket.so.%{major}*

#----------------------------------------------------------------------

%define devqmobipocket %mklibname qmobipocket -d

%package -n %{devqmobipocket}
Summary:	Development files for QMobipocket
Group:		System/Libraries
Requires:	%{libqmobipocket} = %{EVRD}
Provides:	qmobipocket-devel = %{EVRD}

%description -n %{devqmobipocket}
Development files for QMobipocket.

%files -n %{devqmobipocket}
%{_kde_includedir}/qmobipocket/
%{_kde_libdir}/libqmobipocket.so
%{_kde_libdir}/cmake/QMobipocket/

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 -DCMAKE_MINIMUM_REQUIRED_VERSION=2.6
%make

%install
%makeinstall_std -C build

