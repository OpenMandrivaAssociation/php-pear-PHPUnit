%define  upstream_name PHPUnit
%define _requires_exceptions pear(TestConfiguration.php)

Summary:	Regression testing framework for unit tests
Name:		php-pear-%{upstream_name}
Version:	3.6.3
Release:	%mkrel 1
License:	BSD
Group:		Development/PHP
URL:		http://www.phpunit.de/
Source0:	http://pear.phpunit.de/get/PHPUnit-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-cli >= 3:5.2.1
Requires:	php-pear >= 1:1.9.4
Requires:	php-channel-phpunit
BuildArch:	noarch
BuildRequires:	php-pear
BuildRequires:	php-channel-phpunit
Suggests:	php-dom php-json php-pdo php-pdo_sqlite php-simplexml php-tokenizer
Suggests:	php-pear-File_Iterator >= 1.3.0
Suggests:	php-pear-PHP_CodeCoverage >= 1.1.0
Suggests:	php-pear-PHP_Invoker >= 1.0.0
Suggests:	php-pear-PHP_Timer >= 1.0.1
Suggests:	php-pear-PHPUnit_MockObject >= 1.1.0
Suggests:	php-pear-Text_Template >= 1.1.1
Suggests:	php-symfony-YAML >= 1.0.2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
PHPUnit is a regression testing framework used by the developer who implements
unit tests in PHP.

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
%doc %{upstream_name}-%{version}/ChangeLog.markdown
%doc %{upstream_name}-%{version}/LICENSE
%doc %{upstream_name}-%{version}/README.markdown
%{_bindir}/phpunit
%{_datadir}/pear/PHPUnit
%{_datadir}/pear/packages/PHPUnit.xml
