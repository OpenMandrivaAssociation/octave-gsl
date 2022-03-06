%global octpkg gsl

Summary:	Octave bindings for the GNU Scientific Library
Name:		octave-%{octpkg}
Version:	2.1.1
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 2.9.7
BuildRequires:	pkgconfig(gsl)

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Octave bindings to the GNU Scientific Library.

This package is part of community Octave-Forge collection.

%files
%license COPYING
%doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

%build
export CC=gcc
export CXX=g++
export LDFLAGS="%ldflags -lgsl -lgslcblas"
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

