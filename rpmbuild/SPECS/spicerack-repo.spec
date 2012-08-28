Name:           spicerack-repo
Version:       	1.0
Release:	1%{?dist}
Summary:       	Sets up Spicerack Repository files 
BuildArch: noarch

Group:     TEST      
License:       TEST 
URL:            TEST

%description
Sets up the Spicerack Repository files

%clean

%files
%defattr(-,root,root,-)
/etc/yum.repos.d/spicerack.repo

%doc



%changelog
