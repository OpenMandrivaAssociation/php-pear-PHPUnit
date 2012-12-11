%define  upstream_name PHPUnit
%define peardir %(pear config-get php_dir 2> /dev/null || echo %{_datadir}/pear)
%define xmldir  /var/lib/pear

Summary: 	The PHP Unit Testing framework
Name: 		php-pear-%{upstream_name}
Version: 	3.6.10
Release: 	%mkrel 2
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
Requires:	php-pear-PHPUnit_MockObject >= 1.1.0
Requires:	php-symfony-YAML >= 1.0.2
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


%changelog
* Fri Mar 23 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 3.6.10-2mdv2012.0
+ Revision: 786394
- fix dependency
- disable PHPUnit_MockObject dependency for now to get things through BS
- fix typo in dependency

* Tue Mar 13 2012 Thomas Spuhler <tspuhler@mandriva.org> 3.6.10-1
+ Revision: 784525
- upgrade to 3.6.10
  pearize specfile

* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 3.6.3-2
+ Revision: 742180
- fix major breakage by careless packager

* Wed Nov 16 2011 Oden Eriksson <oeriksson@mandriva.com> 3.6.3-1
+ Revision: 730861
- 3.6.3
- fix deps
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 3.3.17-3mdv2011.0
+ Revision: 613752
- the mass rebuild of 2010.1 packages

* Sat Nov 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.3.17-2mdv2010.1
+ Revision: 468060
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.3.17-1mdv2010.0
+ Revision: 446478
- update to new version 3.3.17

* Fri Jul 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.3.16-1mdv2010.0
+ Revision: 394097
- update to new version 3.3.16

* Tue Feb 17 2009 Oden Eriksson <oeriksson@mandriva.com> 3.3.9-1mdv2009.1
+ Revision: 341719
- 3.3.9

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 3.3.8-2mdv2009.1
+ Revision: 322630
- rebuild

* Mon Dec 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.3.8-1mdv2009.1
+ Revision: 320935
- new version
- don't duplicate spec-helper job
- cleanup file list

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 3.1.9-2mdv2009.0
+ Revision: 237047
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 06 2007 Oden Eriksson <oeriksson@mandriva.com> 3.1.9-1mdv2008.1
+ Revision: 106412
- require the php-channel-phpunit package that registers the pear.phpunit.de channel
- another attempt to build the package
- fix build (take #2)
- fix build
- 3.1.9
- simplify the install and fix #33148

* Fri Jun 01 2007 Oden Eriksson <oeriksson@mandriva.com> 3.0.6-4mdv2008.0
+ Revision: 33604
- don't require php-xdebug

* Wed May 02 2007 Oden Eriksson <oeriksson@mandriva.com> 3.0.6-3mdv2008.0
+ Revision: 20497
- fix deps (duh...)

* Tue Apr 24 2007 Oden Eriksson <oeriksson@mandriva.com> 3.0.6-2mdv2008.0
+ Revision: 17790
- fix deps

* Wed Apr 18 2007 Oden Eriksson <oeriksson@mandriva.com> 3.0.6-1mdv2008.0
+ Revision: 14671
- Import php-pear-PHPUnit



* Wed Apr 18 2007 Oden Eriksson <oeriksson@mandriva.com> 3.0.6-1mdv2008.0
- initial Mandriva package
