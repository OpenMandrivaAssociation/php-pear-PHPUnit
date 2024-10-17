%define  upstream_name PHPUnit
%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

%define __noautoreq /usr/bin/php

Name:		php-pear-%{upstream_name}
Version:	3.7.31
Release:	2
Summary:	Regression testing framework for unit tests

License:	BSD License
Group:		Development/PHP
URL:		https://www.phpunit.de/
Source0:	http://pear.phpunit.de/get/PHPUnit-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear >= 1.9.4
Requires:	php-channel-phpunit
Requires:	php-pear-File_Iterator >= 1.3.0
Requires:	php-pear-Text_Template >= 1.1.1
Requires:	php-pear-PHP_CodeCoverage >= 1.2.1
Requires:	php-pear-PHP_CodeCoverage <= 1.2.99
Requires:	php-pear-PHP_Timer >= 1.0.2
Requires:	php-pear-PHP_Timer <= 1.0.99
Requires:	php-pear-PHPUnit_MockObject >= 1.2.0
Requires:	php-pear-Symfony2_Yaml >= 2.0.0
Requires:	php-pear-Symfony2_Yaml <= 2.99.99
BuildArch:	noarch
BuildRequires:	php-pear >= 1.9.4
BuildRequires:	php-channel-phpunit


%description
The PHP Unit Testing framework.

%prep
%setup -c -T
pear -v -c pearrc \
        -d php_dir=%{peardir} \
        -d doc_dir=/docs \
        -d bin_dir=%{_bindir} \
        -d data_dir=%{peardir}/data \
        -d test_dir=%{peardir}/tests \
        -d ext_dir=%{_libdir} \
        -s

%build

%install
pear -c pearrc install --nodeps --packagingroot %{buildroot} %{SOURCE0}
        
# Clean up unnecessary files
rm pearrc
rm %{buildroot}/%{peardir}/.filemap
rm %{buildroot}/%{peardir}/.lock
rm -rf %{buildroot}/%{peardir}/.registry
rm -rf %{buildroot}%{peardir}/.channels
rm %{buildroot}%{peardir}/.depdb
rm %{buildroot}%{peardir}/.depdblock

mv %{buildroot}/docs .


# Install XML package description
mkdir -p %{buildroot}%{xmldir}
tar -xzf %{SOURCE0} package.xml
cp -p package.xml %{buildroot}%{xmldir}/PHPUnit.xml


%post
pear install --nodeps --soft --force --register-only %{xmldir}/PHPUnit.xml

%postun
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only pear.phpunit.de/PHPUnit
fi

%files
%doc docs/PHPUnit/*
%{peardir}/*
%{_bindir}/phpunit
%{xmldir}/PHPUnit.xml


