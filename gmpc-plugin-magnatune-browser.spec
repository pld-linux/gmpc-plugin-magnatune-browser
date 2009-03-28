%define		source_name gmpc-magnatune
Summary:	Magnatune.com browser for Gnome Music Player Client
Summary(pl.UTF-8):	Przeglądarka magnatune.com dla odtwarzacza Gnome Music Player Client
Name:		gmpc-plugin-magnatune-browser
Version:	0.18.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/musicpd/%{source_name}-%{version}.tar.gz
# Source0-md5:	4fbe3e85f5be2f6840c414528630f908
URL:		http://gmpcwiki.sarine.nl/index.php?title=Magnatune
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gmpc-devel >= 0.18.0
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	libglade2-devel
BuildRequires:	libmpd-devel >= 0.18.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Magnatune.com browser for Gnome Music Player Client.

%description -l pl.UTF-8
Przeglądarka magnatune.com dla odtwarzacza Gnome Music Player Client.

%prep
%setup -qn %{source_name}-%{version}

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

rm $RPM_BUILD_ROOT%{_libdir}/gmpc/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gmpc/plugins/*.so
%{_datadir}/gmpc/plugins/magnatune
