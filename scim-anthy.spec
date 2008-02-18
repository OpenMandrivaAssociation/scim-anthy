%define version	1.2.4
%define release	%mkrel 3

%define scim_version	1.4.5
%define anthy_version	6606

%define libname %mklibname %{name} 0

Name:		scim-anthy
Summary:	SCIM IMEngine module for anthy
Epoch:		2
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	GPL
URL:		http://sourceforge.jp/projects/scim-imengine/
Source0:	%{name}-%{version}.tar.gz
Patch0:		scim-anthy-modify_romaji_tables.diff
Patch1:		scim-anthy-disable_custom_candidate_window.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:		%{libname} = %{epoch}:%{version}-%{release}
Requires:		anthy >= %{anthy_version}
Requires:		scim >= %{scim_version}
Requires:		kasumi
BuildRequires:		anthy-devel >= %{anthy_version}
BuildRequires:		scim-devel >= %{scim_version}
BuildRequires:		automake libltdl-devel

%description
Scim-anthy is an SCIM IMEngine module for anthy.
It supports Japanese input.


%package -n %{libname}
Summary:	Scim-anthy library
Group:		System/Internationalization

%description -n %{libname}
scim-anthy library.

%prep
%setup -q
%patch0 -p1

%build
autoreconf
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove unneeded files
rm -f %{buildroot}/%scim_plugins_dir/*/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig


%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{_datadir}/scim/icons/*
%dir %{_datadir}/scim/Anthy
%{_datadir}/scim/Anthy/*

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%scim_plugins_dir/IMEngine/*.so
%scim_plugins_dir/SetupUI/*.so
%scim_plugins_dir/Helper/*.so
