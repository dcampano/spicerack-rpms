%define name		php
%define release		1
%define version 	5.3.5
%define buildroot %{_topdir}/%{name}-%{version}-root

BuildRoot:	%{buildroot}
Summary: 		GNU wget
License: 		GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz
Prefix: 		/usr
Group: 			Development/Tools

%description
The GNU wget program downloads files from the Internet using the command-line.

%prep
%setup -q

%configure
make

%install
make install INSTALL_ROOT=$RPM_BUILD_ROOT
