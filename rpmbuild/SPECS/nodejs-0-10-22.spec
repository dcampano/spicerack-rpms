%define nodever         0.10.22
%define _prefix /opt/nodejs/%{nodever}

Name:           nodejs-%{nodever}
Version:        1.0
Release:        1%{?dist}
License:        Ruby License/GPL - see COPYING
URL:            http://www.ruby-lang.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:   glibc-devel gcc-c++
Source0:        https://nodejs.org/dist/v%{nodever}/node-v%{nodever}.tar.gz
Summary:        Provides nodejs version %nodever
Group:          Development/Languages

%description
Nodejs

%prep
%setup -n node-v%{nodever}

%build
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"
export LDFLAGS="-Wl,-rpath,%{_prefix}/lib -L%{_prefix}/lib"
./configure --prefix=%{_prefix}

make %{?_smp_mflags}

%install
# installing binaries ...
make install DESTDIR=$RPM_BUILD_ROOT

#we don't want to keep the src directory
rm -rf $RPM_BUILD_ROOT/usr/src

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_prefix}/*

