Summary:	A collection of plugins to handle mobipocket files
Name:		plasma6-kdegraphics-mobipocket
Version:	24.01.80
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/kdegraphics-mobipocket-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	ninja

%description
A collection of plugins to handle mobipocket files.

%files
%doc COPYING

#----------------------------------------------------------------------

%define libqmobipocket %mklibname qmobipocket

%package -n %{libqmobipocket}
Summary:	QMobipocket library
Group:		System/Libraries

%description -n %{libqmobipocket}
QMobipocket library.

%files -n %{libqmobipocket}
%{_libdir}/libqmobipocket.so*

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
%{_includedir}/QMobipocket/
%{_libdir}/cmake/QMobipocket/

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n kdegraphics-mobipocket-%{version}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
