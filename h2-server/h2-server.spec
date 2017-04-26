%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress

Name: h2-server
Version: 0.0.1
Release: 1
Summary: H2 database network server

Group: Development/Tools
License: GPL
URL: http://marangoni.io
Source: %{name}-%{version}.tar.gz
#Source: %{expand:%{name}-%{version}-%{release}}

BuildArch: noarch
BuildRoot: %{_topdir}/BUILD/%{name}-%{version}-root

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}

%build
# Empty section.

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}

# in builddir
cp -a * %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/h2database/variables.conf
%{_sharedstatedir}/h2database/data
%defattr(744,root,root)
%{_sharedstatedir}/h2database/bin/*
/lib/systemd/system/h2database.service
%dir %{_sharedstatedir}/h2database/data
