%define  upstream_name PHPUnit
%define peardir %(pear config-get php_dir 2> /dev/null || echo %{_datadir}/pear)
%define xmldir  /var/lib/pear

Summary: 	The PHP Unit Testing framework
Name: 		php-pear-%{upstream_name}
Version: 	3.6.10
Release: 	%mkrel 1
License: 	BSD
Group: 		Development/PHP
Source0: 	http://pear.phpunit.de/get/PHPUnit-%{version}.tgz
URL: 		http://pear.phpunit.de/package/PHPUnit
BuildRequires: 	php-pear >= 1.4.7
BuildRequires: 	php-channel-phpunit
Requires:	php-pear-File_Iterator >= 1.3.0 
Requires:	php-pear-Text_Template >= 1.1.1
Requires:	php-pear-PHP_CodeCoverage >= 1.1.0
Requires:	php-pear-PHP_Timer >= 1.0.1
Requires:	PHPUnit_MockObject >= 1.1.0
Requires:	php-symphony-YAML >= 1.0.2
Requires:	php-pear >= 1.9.4
Requires: 	php-channel-phpunit
BuildArch: 	noarch

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
rm -rf %{buildroot}
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

%clean
rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/PHPUnit.xml

%postun
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only pear.phpunit.de/PHPUnit
fi

%files
%defattr(-,root,root)
%doc docs/PHPUnit/*
%{_bindir}/phpunit
%{peardir}/*
%{xmldir}/PHPUnit.xml
