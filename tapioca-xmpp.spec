# TODO: real desc
Summary:	Tapioca - VoIP framework
Summary(pl):	Tapioca - szkielet VoIP
Name:		tapioca-xmpp
Version:	0.3.9
Release:	1
License:	LGPL
Group:		Networking/Instant messaging
Source0:	http://dl.sourceforge.net/tapioca-voip/%{name}-%{version}.tar.gz
# Source0-md5:	8d810351eb5b30e70b202e067da450c1
Patch0:		%{name}-doxygen.patch
URL:		http://sourceforge.net/projects/tapioca-voip/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-devel >= 0.36
BuildRequires:	dbus-glib-devel >= 0.36
BuildRequires:	glib2-devel
BuildRequires:	libjingle-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	tapioca-libs-devel
Requires:	tapioca
Buildroot:	%{_tmppath}/%{name}-buildroot 

%description
Tapioca is a framework for Voice over IP (VoIP) and Instant Messaging
(IM). Its main goal is to provide an easy way for developing and using
VoIP and IM services in any kind of application. It was designed to be
cross-platform, lightweight, thread-safe, having mobile devices and
applications in mind.

%description -l pl
Tapioca to szkielet do VoIP (Voice over IP) i IM (Instant Messaging,
czyli komunikatorów). G³ównym jego celem jest zapewnienie ³atwego
sposobu tworzenia i u¿ywania us³ug VoIP i IM w dowolnym rodzaju
aplikacji. Zosta³ zaprojektowany jako wieloplatformowy, lekki,
bezpieczny dla w±tków, a tak¿e z my¶l± o urz±dzeniach i aplikacjach
przeno¶nych.

%prep
%setup -q
%patch0 -p0

perl -pi -e "s|/lib\b|/%{_lib}|g" configure.*

%build
rm -rf autom4te.cache
%{__aclocal} -I m4
%{__libtoolize}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/dbus-1/services/org.tapioca.Xmpp.service
%{_datadir}/tapioca-0.3/xmpp.ini
