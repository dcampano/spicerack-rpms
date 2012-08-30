%define package_name php

Name:           spicerack-php
Version:       	5.3.15
Release:        1%{?dist}
Summary:        Php program

Group:     TEST      
License:       TEST 
URL:            TEST
Source0:       	%{package_name}-%{version}.tar.gz 
Source1:	php-fpm.init
BuildRoot:      %{_tmppath}/%{package_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  libicu-devel
BuildRequires:  openssl-devel
BuildRequires:  curl-devel

%description
PHP custom install


%prep
%setup -q -n php-5.3.15


%build
#./configure '--enable-fastcgi' '--enable-libxml' '--enable-magic-quotes' '--with-curl' '--with-mysql=mysqlnd' '--with-zlib' '--with-zlib-dir=/usr' '--with-openssl=/usr' '--with-openssl-dir=/usr' '--enable-fpm' '--with-mysqli=mysqlnd' '--with-pdo-mysql=mysqlnd' '--enable-mbstring' '--enable-intl'
%configure \
	--enable-fastcgi \
	--enable-libxml \
	--enable-magic-quotes \
	--with-curl \
	--with-mysql=mysqlnd \
	--with-zlib \
	--with-zlib-dir=/usr \
	--with-openssl=/usr \
	--with-openssl-dir=/usr \
	--enable-fpm \
	--with-mysqli=mysqlnd \
	--with-pdo-mysql=mysqlnd \
	--enable-mbstring \
	--enable-intl 

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL_ROOT=$RPM_BUILD_ROOT
# Service files
install -m 755 -d $RPM_BUILD_ROOT%{_initrddir}
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/php-fpm


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%exclude   /.channels/.alias/pear.txt
%exclude   /.channels/.alias/pecl.txt
%exclude   /.channels/.alias/phpdocs.txt
%exclude   /.channels/__uri.reg
%exclude   /.channels/doc.php.net.reg
%exclude   /.channels/pear.php.net.reg
%exclude   /.channels/pecl.php.net.reg
%exclude   /.depdb
%exclude   /.depdblock
%exclude   /.filemap
%exclude   /.lock
/etc/*
/usr/bin/*
/usr/sbin/*
/usr/include/php/*
/usr/lib/*
/usr/share/*
%{_initrddir}/php-fpm

%doc



%changelog
