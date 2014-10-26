%define		rname	gtksourceview

Summary:	Text widget that extends the standard GTK+
Name:		gtksourceview2
Version:	2.10.5
Release:	2
License:	GPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/gtksourceview/2.10/%{rname}-%{version}.tar.bz2
# Source0-md5:	1219ad1694df136f126507466aeb41aa
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pcre-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkSourceView is a text widget that extends the standard GTK+ 2.x text
widget gtksourceview. It improves gtksourceview by implementing syntax
highlighting and other features typical of a source editor.

%package devel
Summary:	Header files for gtksourceview
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for gtksourceview.

%package apidocs
Summary:	gtksourceview API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gtksourceview API documentation.

%prep
%setup -qn %{rname}-%{version}

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_CXX_WARNINGS.*//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules		\
	--disable-static		\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{rname}-2.0

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files -f %{rname}-2.0.lang
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libgtksourceview-2.0.so.?
%attr(755,root,root) %{_libdir}/libgtksourceview-2.0.so.*.*.*
%{_datadir}/%{rname}-2.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtksourceview-2.0.so
%{_includedir}/%{rname}-2.0
%{_pkgconfigdir}/gtksourceview-2.0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{rname}-2.0

