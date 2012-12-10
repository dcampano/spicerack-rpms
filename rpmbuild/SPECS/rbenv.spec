%define _prefix /opt/rbenv

Name: rbenv
Summary: rbenv
Version: 0.3.0
Release: 1%{?dist}
License: MIT
Group: Development/Tools
BuildArch: noarch
URL: https://github.com/sstephenson/rbenv
Source0: http://tejas.fedorapeople.org/rbenv/%{name}-%{version}.tar.gz
Source1: rbenv.sh
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
rbenv

%prep
%setup -q -n rbenv-master

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/etc/profile.d
install -m 755 -p %{SOURCE1} %{buildroot}/etc/profile.d/rbenv.sh

mkdir -p %{buildroot}%{_prefix}/libexec
install -p libexec/* %{buildroot}%{_prefix}/libexec/

mkdir -p %{buildroot}%{_prefix}/bin
cp -P bin/* %{buildroot}%{_prefix}/bin/

mkdir -p %{buildroot}%{_prefix}/shims
mkdir -p %{buildroot}%{_prefix}/versions

mkdir -p %{buildroot}%{_prefix}/completions
mv completions/* %{buildroot}%{_prefix}/completions

%post
echo You probably want to execute the following line to add rbenv to your shell
echo echo "'eval \"\$(rbenv init -)\"'" \>\> ~/.bash_profile

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}/*
/etc/profile.d/rbenv.sh

%changelog
* Mon Dec 10 2012 Davy Campano <dcampano@gmail.com> - 0.0.1-1
- Initial Spec
