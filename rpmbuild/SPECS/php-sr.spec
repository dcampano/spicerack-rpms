Name:           php
Version:       	5.3.10
Release:        1%{?dist}
Summary:        Php program

Group:     TEST      
License:       TEST 
URL:            TEST
Source0:       	%{name}-%{version}.tar.gz 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
PHP custom install


%prep
%setup -q


%build
./configure --prefix=/opt/php5 '--enable-fastcgi' '--enable-libxml' '--enable-magic-quotes' '--with-curl' '--with-mysql=mysqlnd' '--with-zlib' '--with-zlib-dir=/usr' '--with-openssl=/usr' '--with-openssl-dir=/usr' '--enable-fpm' '--with-mysqli=mysqlnd' '--with-pdo-mysql=mysqlnd' '--enable-mbstring' '--enable-intl'
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL_ROOT=$RPM_BUILD_ROOT


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
/opt/php5/bin/pear
/opt/php5/bin/peardev
/opt/php5/bin/pecl
/opt/php5/bin/phar
/opt/php5/bin/phar.phar
/opt/php5/bin/php
/opt/php5/bin/php-config
/opt/php5/bin/phpize
/opt/php5/etc/pear.conf
/opt/php5/etc/php-fpm.conf.default
/opt/php5/include/*
/opt/php5/lib/*
/opt/php5/man/*
/opt/php5/sbin/*
/opt/php5/share/php/fpm/status.html

%doc



%changelog
