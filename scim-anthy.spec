%define version	1.2.6
%define release	%mkrel 1

%define scim_version	1.4.5
%define anthy_version	6606

%define libname %mklibname %{name} 0

Name:		scim-anthy
Summary:	SCIM IMEngine module for anthy
Epoch:		2
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	GPLv2+
URL:		http://sourceforge.jp/projects/scim-imengine/
Source0:	%{name}-%{version}.tar.gz
Patch0:		scim-anthy-modify_romaji_tables.diff
Patch1:		scim-anthy-disable_custom_candidate_window.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Obsoletes:		%{libname}
Requires:		anthy >= %{anthy_version}
Requires:		scim-client = %{scim_api}
Requires:		kasumi
BuildRequires:		anthy-devel >= %{anthy_version}
BuildRequires:		scim-devel >= %{scim_version}
BuildRequires:		automake libltdl-devel
BuildRequires:		gettext-devel

%description
Scim-anthy is an SCIM IMEngine module for anthy.
It supports Japanese input.

%prep
%setup -q
%patch0 -p1

%build

set -x
autopoint --force
aclocal -I m4
autoheader
libtoolize -c --automake 
automake --add-missing --copy --include-deps
autoconf

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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{_datadir}/scim/icons/*
%dir %{_datadir}/scim/Anthy
%{_datadir}/scim/Anthy/*
%scim_plugins_dir/IMEngine/*.so
%scim_plugins_dir/SetupUI/*.so
%scim_plugins_dir/Helper/*.so
