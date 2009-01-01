%define _provides_exceptions pear(docs\\|pear(tests
%define _requires_exceptions pear(TestConfiguration.php)

Summary:	Regression testing framework for unit tests
Name:		php-pear-PHPUnit
Version:	3.3.8
Release:	%mkrel 2
License:	PHP License
Group:		Development/PHP
URL:		http://www.phpunit.de/
Source0:	http://pear.phpunit.de/get/PHPUnit-%{version}.tgz
Requires(post): php-pear hping2
Requires(preun): php-pear hping2
Requires:	hping2
Requires:	php-cli >= 3:5.2.1
Requires:	php-pear
Requires:	php-channel-phpunit
#Requires:	php-xdebug
BuildArch:	noarch
BuildRequires:	php-pear
BuildRequires:	php-channel-phpunit
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
PHPUnit is a regression testing framework used by the developer who
implements unit tests in PHP. This is the version to be used with PHP 5.

%prep

%setup -q -c 
cp package.xml PHPUnit-%{version}/PHPUnit.xml

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

%build

%install
rm -rf %{buildroot}

pushd PHPUnit-%{version}
#pear channel-discover pear.phpunit.de
pear install --nodeps --force --ignore-errors --packagingroot %{buildroot} PHPUnit.xml
popd

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/PHPUnit.xml

# fix paths and such
find %{buildroot} -type f | xargs perl -pi -e "s|\@php_dir\@|%{_datadir}/pear|g"
find %{buildroot} -type f | xargs perl -pi -e "s|\@php_bin\@|%{_bindir}/php|g"
find %{buildroot} -type f | xargs perl -pi -e "s|\@package_version\@|%{version}|g"

# cleanup
rm -rf %{buildroot}%{_datadir}/pear/.channels
rm -rf %{buildroot}%{_datadir}/pear/.registry
rm -f %{buildroot}%{_datadir}/pear/.depdb
rm -f %{buildroot}%{_datadir}/pear/.depdblock
rm -f %{buildroot}%{_datadir}/pear/.filemap
rm -f %{buildroot}%{_datadir}/pear/.lock

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/PHPUnit.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/PHPUnit.xml >/dev/null || :
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/PHPUnit.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/PHPUnit.xml >/dev/null || :
	fi
fi

# only do this if we have a working network
if /usr/sbin/hping -c 4 -p 80 --tcpexitcode pear.phpunit.de >/dev/null 2>&1; then
    %{_bindir}/pear channel-update pear.phpunit.de
else
    echo "You might want to run \"%{_bindir}/pear channel-update pear.phpunit.de\" when your network works"
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/PHPUnit.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r PHPUnit >/dev/null || :
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/phpunit
%{_datadir}/pear/tests/PHPUnit
%{_datadir}/pear/docs/PHPUnit
%{_datadir}/pear/PHPUnit
%{_datadir}/pear/packages/PHPUnit.xml
