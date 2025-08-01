#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%define		pdir	Geo
%define		pnam	Shapelib
Summary:	Geo::Shapelib - Perl extension for reading and writing shapefiles as defined by ESRI(r)
Summary(pl.UTF-8):	Geo::Shapelib - rozszerzenie Perla o obsługę r/w plików ESRI(r) SHP
Name:		perl-Geo-Shapelib
Version:	0.22
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Geo/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b6c3cba5e5ea4faaa591d9e66d7216c1
URL:		http://search.cpan.org/dist/Geo-Shapelib/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	shapelib-devel
%if %{with tests}
BuildRequires:	perl-Tree-R
%endif
Requires:	perl-Tree-R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a library for reading, creating, and writing shapefiles as
defined by ESRI(r) using Perl. The Perl code uses Frank Warmerdam's
Shapefile C Library (http://shapelib.maptools.org/). The library is
included in this distribution.

%description -l pl.UTF-8
Biblioteka ta umożliwia wczytywanie, tworzenie oraz zapisywanie tzw.
shapefiles zdefiniowanych przez ESRI(r) z poziomu Perla. Kod
wykorzystuje bibliotekę C Shapefile Franka Warmerdama
(http://shapelib.maptools.org/). Biblioteka ta jest załączona w
pakiecie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	--shapelib="%{_libdir}/libshp.so"

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%{perl_vendorarch}/Geo/Shapelib.pm
%dir %{perl_vendorarch}/auto/Geo/Shapelib
%attr(755,root,root) %{perl_vendorarch}/auto/Geo/Shapelib/Shapelib.so
%{perl_vendorarch}/auto/Geo/Shapelib/autosplit.ix
%{_mandir}/man3/*
