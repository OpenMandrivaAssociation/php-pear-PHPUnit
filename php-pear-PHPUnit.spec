%define  upstream_name PHPUnit
%define _requires_exceptions pear(TestConfiguration.php)

Name:		php-pear-%{upstream_name}
Version:	3.3.17
Release:	%mkrel 2
Summary:	Regression testing framework for unit tests
License:	PHP License
Group:		Development/PHP
URL:		http://www.phpunit.de/
Source0:	http://pear.phpunit.de/get/PHPUnit-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-cli >= 3:5.2.1
Requires:	php-pear
Requires:	php-channel-phpunit
BuildArch:	noarch
BuildRequires:	php-pear
BuildRequires:	php-channel-phpunit
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
PHPUnit is a regression testing framework used by the developer who
implements unit tests in PHP. This is the version to be used with PHP 5.

%prep
%setup -q -c 
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%build

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%{_bindir}/phpunit
%{_datadir}/pear/PHPUnit
%{_datadir}/pear/packages/PHPUnit.xml
