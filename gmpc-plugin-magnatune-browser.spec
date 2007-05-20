%define		source_name gmpc-magnatune
Summary:	Magnatune.com browser for Gnome Music Player Client
Summary(pl.UTF-8):	Przeglądarka magnatune.com dla odtwarzacza Gnome Music Player Client
Name:		gmpc-plugin-magnatune-browser
Version:	0.15.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
# http://sarine.nl/gmpc-plugins-downloads
Source0:	%{source_name}-%{version}.tar.gz
# Source0-md5:	2a310e9fe95e83a66027954bc2cf94ff
Patch0:		%{name}-plugins_path.patch
URL:		http://gmpc.sarine.nl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gmpc-devel >= 0.15.0
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	libglade2-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Magnatune.com browser for Gnome Music Player Client.

%description -l pl.UTF-8
Przeglądarka magnatune.com dla odtwarzacza Gnome Music Player Client.

%prep
%setup -qn %{source_name}-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gmpc

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/gmpc/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gmpc/*.so
%{_datadir}/gmpc/plugins/magnatune
