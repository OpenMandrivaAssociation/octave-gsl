%global octpkg gsl

Summary:	Octave bindings to the GNU Scientific Library
Name:		octave-gsl
Version:	2.1.1
Release:	3
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/gsl/
Source0:	https://downloads.sourceforge.net/octave/gsl-%{version}.tar.gz
# (upstream) https://savannah.gnu.org/bugs/index.php?59159
Patch0:		octave-gsl-2.1.1-clang.patch

BuildRequires:  octave-devel >= 2.9.7
BuildRequires:	gomp-devel
BuildRequires:	pkgconfig(gsl)

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Octave bindings to the GNU Scientific Library.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
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

