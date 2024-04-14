#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Summary:	A collection of plugins to handle mobipocket files
Name:		plasma6-kdegraphics-mobipocket
Version:	24.02.2
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
%if 0%{?git:1}
Source0:	https://invent.kde.org/graphics/kdegraphics-mobipocket/-/archive/%{gitbranch}/kdegraphics-mobipocket-%{gitbranchd}.tar.bz2#/kdegraphics-mobipocket-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/kdegraphics-mobipocket-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	ninja

%description
A collection of plugins to handle mobipocket files.

%files
%doc COPYING

#----------------------------------------------------------------------

%define libqmobipocket %mklibname QMobipocket6

%package -n %{libqmobipocket}
Summary:	QMobipocket library
Group:		System/Libraries

%description -n %{libqmobipocket}
QMobipocket library.

%files -n %{libqmobipocket}
%{_libdir}/libQMobipocket6.so*

#----------------------------------------------------------------------

%define devqmobipocket %mklibname QMobipocket6 -d

%package -n %{devqmobipocket}
Summary:	Development files for QMobipocket
Group:		System/Libraries
Requires:	%{libqmobipocket} = %{EVRD}
Provides:	qmobipocket-devel = %{EVRD}

%description -n %{devqmobipocket}
Development files for QMobipocket.

%files -n %{devqmobipocket}
%{_includedir}/QMobipocket6/
%{_libdir}/cmake/QMobipocket6/

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n kdegraphics-mobipocket-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-DQT_MAJOR_VERSION=6 \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
