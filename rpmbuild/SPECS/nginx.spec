Name:          	nginx 
Version:       	1.2.3
Release:        1%{?dist}
Summary:        Nginx Webserver

Group:     TEST      
License:       TEST 
URL:            TEST
Source0:       	http://nginx.org/download/%{name}-%{version}.tar.gz 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:     pcre-devel
BuildRequires:     openssl-devel
BuildRequires:     GeoIP-devel


%description
Nginx Custom build


%prep
%setup -q


%build
./configure --prefix=/opt/nginx --with-http_stub_status_module --with-http_geoip_module --with-http_ssl_module --with-http_realip_module
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL_ROOT=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%config   /opt/nginx/conf/fastcgi.conf
   /opt/nginx/conf/fastcgi.conf.default
%config   /opt/nginx/conf/fastcgi_params
   /opt/nginx/conf/fastcgi_params.default
   /opt/nginx/conf/koi-utf
   /opt/nginx/conf/koi-win
%config   /opt/nginx/conf/mime.types
   /opt/nginx/conf/mime.types.default
%config   /opt/nginx/conf/nginx.conf
   /opt/nginx/conf/nginx.conf.default
   /opt/nginx/conf/win-utf
   /opt/nginx/html/50x.html
   /opt/nginx/html/index.html
   /opt/nginx/sbin/nginx
%config   /opt/nginx/conf/scgi_params
   /opt/nginx/conf/scgi_params.default
%config   /opt/nginx/conf/uwsgi_params
   /opt/nginx/conf/uwsgi_params.default

%doc



%changelog
