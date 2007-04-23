%define version	1.3.0
%define release	%mkrel 1

%define scim_version	1.4.5
%define anthy_version	6606

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0

Name:		scim-anthy
Summary:	Scim-anthy is an SCIM IMEngine module for anthy
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	GPL
URL:		http://sourceforge.jp/projects/scim-imengine/
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:		%{libname} = %{version}
Requires:		anthy >= %{anthy_version}
Requires:		scim >= %{scim_version}
Requires:		kasumi
BuildRequires:		anthy-devel >= %{anthy_version}
BuildRequires:		scim-devel >= %{scim_version}
BuildRequires:		automake1.8 libltdl-devel

%description
Scim-anthy is an SCIM IMEngine module for anthy.
It supports Japanese input.


%package -n %{libname}
Summary:	Scim-anthy library
Group:		System/Internationalization
Provides:		%{libname_orig} = %{version}

%description -n %{libname}
scim-anthy library.


%prep
%setup -q
cp /usr/share/automake-1.9/mkinstalldirs .

%build
[[ ! -x configure ]] && ./bootstrap
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove unneeded files
rm -f %{buildroot}/%{_libdir}/scim-1.0/*/*/*.{a,la}
rm -f %{buildroot}/%{_libdir}/scim-1.0/*/*/Helper/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig


%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{_datadir}/scim/icons/*
%{_datadir}/scim/Anthy/style/*.sty

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/scim-1.0/*/IMEngine/*.so
%{_libdir}/scim-1.0/*/SetupUI/*.so
