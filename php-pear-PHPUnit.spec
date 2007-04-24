Summary:	Regression testing framework for unit tests
Name:		php-pear-PHPUnit
Version:	3.0.6
Release:	%mkrel 2
License:	PHP License
Group:		Development/PHP
URL:		http://www.phpunit.de/
Source0:	http://pear.phpunit.de/get/PHPUnit-%{version}.tar.bz2
Requires(post): php-pear hping
Requires(preun): php-pear hping
Requires:	hping2
Requires:	php-cli >= 3:5.2.1
Requires:	php-pear
Requires:	php-xdebug
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
PHPUnit is a regression testing framework used by the developer who
implements unit tests in PHP. This is the version to be used with PHP 5.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/PHPUnit
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Extensions
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Framework
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Framework/ComparisonFailure
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Framework/Constraint
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/Builder
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/Matcher
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/Stub
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Runner
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Samples
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Samples/BankAccount
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Samples/Money
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Tests
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Tests/Extensions
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Tests/Framework
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Tests/Runner
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Tests/Util
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Tests/Util/TestDox
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files
install -d %{buildroot}%{_datadir}/pear/PHPUnit/TextUI
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Util
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Util/Log
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Util/Report
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Util/Report/Coverage
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Util/Report/Coverage/Node
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Util/Report/Template
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Util/Report/Test
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Util/Report/Test/Node
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Util/Skeleton
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Util/TestDox
install -d %{buildroot}%{_datadir}/pear/PHPUnit/Util/TestDox/ResultPrinter
install -d %{buildroot}%{_datadir}/pear/PHPUnit2
install -d %{buildroot}%{_datadir}/pear/PHPUnit2/Extensions
install -d %{buildroot}%{_datadir}/pear/PHPUnit2/Framework
install -d %{buildroot}%{_datadir}/pear/PHPUnit2/Runner
install -d %{buildroot}%{_datadir}/pear/PHPUnit2/TextUI
install -d %{buildroot}%{_datadir}/pear/PHPUnit2/Util
install -d %{buildroot}%{_datadir}/pear/PHPUnit2/Util/Log

install -m0644 PHPUnit-%{version}/PHPUnit/Extensions/ExceptionTestCase.php %{buildroot}%{_datadir}/pear/PHPUnit/Extensions/ExceptionTestCase.php
install -m0644 PHPUnit-%{version}/PHPUnit/Extensions/OutputTestCase.php %{buildroot}%{_datadir}/pear/PHPUnit/Extensions/OutputTestCase.php
install -m0644 PHPUnit-%{version}/PHPUnit/Extensions/PerformanceTestCase.php %{buildroot}%{_datadir}/pear/PHPUnit/Extensions/PerformanceTestCase.php
install -m0644 PHPUnit-%{version}/PHPUnit/Extensions/RepeatedTest.php %{buildroot}%{_datadir}/pear/PHPUnit/Extensions/RepeatedTest.php
install -m0644 PHPUnit-%{version}/PHPUnit/Extensions/SeleniumTestCase.php %{buildroot}%{_datadir}/pear/PHPUnit/Extensions/SeleniumTestCase.php
install -m0644 PHPUnit-%{version}/PHPUnit/Extensions/TestDecorator.php %{buildroot}%{_datadir}/pear/PHPUnit/Extensions/TestDecorator.php
install -m0644 PHPUnit-%{version}/PHPUnit/Extensions/TestSetup.php %{buildroot}%{_datadir}/pear/PHPUnit/Extensions/TestSetup.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/ComparisonFailure/Array.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/ComparisonFailure/Array.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/ComparisonFailure/Object.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/ComparisonFailure/Object.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/ComparisonFailure/Scalar.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/ComparisonFailure/Scalar.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/ComparisonFailure/String.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/ComparisonFailure/String.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/ComparisonFailure/Type.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/ComparisonFailure/Type.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/Constraint/And.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/Constraint/And.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/Constraint/ArrayHasKey.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/Constraint/ArrayHasKey.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/Constraint/FileExists.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/Constraint/FileExists.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/Constraint/GreaterThan.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/Constraint/GreaterThan.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/Constraint/IsAnything.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/Constraint/IsAnything.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/Constraint/IsEqual.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/Constraint/IsEqual.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/Constraint/IsIdentical.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/Constraint/IsIdentical.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/Constraint/IsInstanceOf.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/Constraint/IsInstanceOf.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/Constraint/IsType.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/Constraint/IsType.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/Constraint/LessThan.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/Constraint/LessThan.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/Constraint/Not.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/Constraint/Not.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/Constraint/ObjectHasAttribute.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/Constraint/ObjectHasAttribute.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/Constraint/Or.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/Constraint/Or.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/Constraint/PCREMatch.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/Constraint/PCREMatch.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/Constraint/StringContains.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/Constraint/StringContains.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/Constraint/TraversableContains.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/Constraint/TraversableContains.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/Constraint/Xor.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/Constraint/Xor.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/MockObject/Builder/Identity.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/Builder/Identity.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/MockObject/Builder/InvocationMocker.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/Builder/InvocationMocker.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/MockObject/Builder/Match.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/Builder/Match.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/MockObject/Builder/MethodNameMatch.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/Builder/MethodNameMatch.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/MockObject/Builder/Namespace.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/Builder/Namespace.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/MockObject/Builder/ParametersMatch.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/Builder/ParametersMatch.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/MockObject/Builder/Stub.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/Builder/Stub.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/MockObject/Matcher/AnyInvokedCount.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/Matcher/AnyInvokedCount.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/MockObject/Matcher/AnyParameters.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/Matcher/AnyParameters.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/MockObject/Matcher/Invocation.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/Matcher/Invocation.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/MockObject/Matcher/InvokedAtIndex.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/Matcher/InvokedAtIndex.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/MockObject/Matcher/InvokedAtLeastOnce.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/Matcher/InvokedAtLeastOnce.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/MockObject/Matcher/InvokedCount.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/Matcher/InvokedCount.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/MockObject/Matcher/InvokedRecorder.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/Matcher/InvokedRecorder.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/MockObject/Matcher/MethodName.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/Matcher/MethodName.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/MockObject/Matcher/Parameters.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/Matcher/Parameters.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/MockObject/Matcher/StatelessInvocation.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/Matcher/StatelessInvocation.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/MockObject/Stub/ConsecutiveCalls.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/Stub/ConsecutiveCalls.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/MockObject/Stub/MatcherCollection.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/Stub/MatcherCollection.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/MockObject/Stub/Return.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/Stub/Return.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/MockObject/Invocation.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/Invocation.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/MockObject/InvocationMocker.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/InvocationMocker.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/MockObject/Invokable.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/Invokable.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/MockObject/Matcher.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/Matcher.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/MockObject/Mock.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/Mock.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/MockObject/MockObject.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/MockObject.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/MockObject/Stub.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/Stub.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/MockObject/Verifiable.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/MockObject/Verifiable.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/Assert.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/Assert.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/AssertionFailedError.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/AssertionFailedError.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/ComparisonFailure.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/ComparisonFailure.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/Constraint.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/Constraint.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/Error.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/Error.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/ExpectationFailedException.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/ExpectationFailedException.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/IncompleteTest.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/IncompleteTest.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/IncompleteTestError.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/IncompleteTestError.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/SelfDescribing.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/SelfDescribing.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/SkippedTest.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/SkippedTest.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/SkippedTestError.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/SkippedTestError.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/Test.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/Test.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/TestCase.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/TestCase.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/TestFailure.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/TestFailure.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/TestListener.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/TestListener.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/TestResult.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/TestResult.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/TestSuite.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/TestSuite.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework/Warning.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework/Warning.php
install -m0644 PHPUnit-%{version}/PHPUnit/Runner/BaseTestRunner.php %{buildroot}%{_datadir}/pear/PHPUnit/Runner/BaseTestRunner.php
install -m0644 PHPUnit-%{version}/PHPUnit/Runner/IncludePathTestCollector.php %{buildroot}%{_datadir}/pear/PHPUnit/Runner/IncludePathTestCollector.php
install -m0644 PHPUnit-%{version}/PHPUnit/Runner/StandardTestSuiteLoader.php %{buildroot}%{_datadir}/pear/PHPUnit/Runner/StandardTestSuiteLoader.php
install -m0644 PHPUnit-%{version}/PHPUnit/Runner/TestCollector.php %{buildroot}%{_datadir}/pear/PHPUnit/Runner/TestCollector.php
install -m0644 PHPUnit-%{version}/PHPUnit/Runner/TestSuiteLoader.php %{buildroot}%{_datadir}/pear/PHPUnit/Runner/TestSuiteLoader.php
install -m0644 PHPUnit-%{version}/PHPUnit/Runner/Version.php %{buildroot}%{_datadir}/pear/PHPUnit/Runner/Version.php
install -m0644 PHPUnit-%{version}/PHPUnit/Samples/BankAccount/BankAccount.php %{buildroot}%{_datadir}/pear/PHPUnit/Samples/BankAccount/BankAccount.php
install -m0644 PHPUnit-%{version}/PHPUnit/Samples/BankAccount/BankAccountTest.php %{buildroot}%{_datadir}/pear/PHPUnit/Samples/BankAccount/BankAccountTest.php
install -m0644 PHPUnit-%{version}/PHPUnit/Samples/Money/IMoney.php %{buildroot}%{_datadir}/pear/PHPUnit/Samples/Money/IMoney.php
install -m0644 PHPUnit-%{version}/PHPUnit/Samples/Money/Money.php %{buildroot}%{_datadir}/pear/PHPUnit/Samples/Money/Money.php
install -m0644 PHPUnit-%{version}/PHPUnit/Samples/Money/MoneyBag.php %{buildroot}%{_datadir}/pear/PHPUnit/Samples/Money/MoneyBag.php
install -m0644 PHPUnit-%{version}/PHPUnit/Samples/Money/MoneyTest.php %{buildroot}%{_datadir}/pear/PHPUnit/Samples/Money/MoneyTest.php
install -m0644 PHPUnit-%{version}/PHPUnit/Samples/FailureTest.php %{buildroot}%{_datadir}/pear/PHPUnit/Samples/FailureTest.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/Extensions/AllTests.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/Extensions/AllTests.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/Extensions/ExceptionTestCaseTest.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/Extensions/ExceptionTestCaseTest.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/Extensions/ExtensionTest.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/Extensions/ExtensionTest.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/Extensions/OutputTestCaseTest.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/Extensions/OutputTestCaseTest.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/Extensions/PerformanceTestCaseTest.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/Extensions/PerformanceTestCaseTest.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/Extensions/RepeatedTestTest.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/Extensions/RepeatedTestTest.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/Extensions/SeleniumTestCaseTest.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/Extensions/SeleniumTestCaseTest.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/Framework/AllTests.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/Framework/AllTests.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/Framework/AssertTest.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/Framework/AssertTest.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/Framework/ComparisonFailureTest.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/Framework/ComparisonFailureTest.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/Framework/ConstraintTest.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/Framework/ConstraintTest.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/Framework/MockObjectTest.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/Framework/MockObjectTest.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/Framework/SuiteTest.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/Framework/SuiteTest.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/Framework/TestCaseTest.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/Framework/TestCaseTest.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/Framework/TestImplementorTest.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/Framework/TestImplementorTest.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/Framework/TestListenerTest.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/Framework/TestListenerTest.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/Runner/AllTests.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/Runner/AllTests.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/Runner/BaseTestRunnerTest.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/Runner/BaseTestRunnerTest.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/Util/TestDox/AllTests.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/Util/TestDox/AllTests.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/Util/TestDox/NamePrettifierTest.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/Util/TestDox/NamePrettifierTest.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/Util/AllTests.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/Util/AllTests.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/AnInterface.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/AnInterface.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/ClassWithNonPublicAttributes.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/ClassWithNonPublicAttributes.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/DoubleTestCase.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/DoubleTestCase.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/Error.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/Error.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/Failure.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/Failure.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/InheritedTestCase.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/InheritedTestCase.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/MockRunner.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/MockRunner.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/NoArgTestCaseTest.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/NoArgTestCaseTest.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/NonStatic.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/NonStatic.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/NoTestCaseClass.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/NoTestCaseClass.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/NoTestCases.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/NoTestCases.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/NotPublicTestCase.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/NotPublicTestCase.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/NotVoidTestCase.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/NotVoidTestCase.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/OneTestCase.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/OneTestCase.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/OutputTestCase.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/OutputTestCase.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/OverrideTestCase.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/OverrideTestCase.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/SampleClass.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/SampleClass.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/SetupFailure.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/SetupFailure.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/Sleep.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/Sleep.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/Struct.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/Struct.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/Success.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/Success.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/TearDownFailure.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/TearDownFailure.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/TestIterator.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/TestIterator.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/ThrowExceptionTestCase.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/ThrowExceptionTestCase.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/ThrowNoExceptionTestCase.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/ThrowNoExceptionTestCase.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/TornDown.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/TornDown.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/TornDown2.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/TornDown2.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/TornDown3.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/TornDown3.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/TornDown4.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/TornDown4.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/TornDown5.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/TornDown5.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/TornDown6.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/TornDown6.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/_files/WasRun.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/_files/WasRun.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/AllTests.php %{buildroot}%{_datadir}/pear/PHPUnit/Tests/AllTests.php
install -m0644 PHPUnit-%{version}/PHPUnit/Tests/TestConfiguration.php.dist %{buildroot}%{_datadir}/pear/PHPUnit/Tests/TestConfiguration.php
install -m0644 PHPUnit-%{version}/PHPUnit/TextUI/Command.php %{buildroot}%{_datadir}/pear/PHPUnit/TextUI/Command.php
install -m0644 PHPUnit-%{version}/PHPUnit/TextUI/ResultPrinter.php %{buildroot}%{_datadir}/pear/PHPUnit/TextUI/ResultPrinter.php
install -m0644 PHPUnit-%{version}/PHPUnit/TextUI/TestRunner.php %{buildroot}%{_datadir}/pear/PHPUnit/TextUI/TestRunner.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Log/GraphViz.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/Log/GraphViz.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Log/JSON.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/Log/JSON.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Log/PEAR.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/Log/PEAR.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Log/TAP.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/Log/TAP.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Log/XML.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/Log/XML.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Report/Coverage/Node/Directory.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/Report/Coverage/Node/Directory.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Report/Coverage/Node/File.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/Report/Coverage/Node/File.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Report/Coverage/Factory.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/Report/Coverage/Factory.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Report/Coverage/Node.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/Report/Coverage/Node.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Report/Template/butter.png %{buildroot}%{_datadir}/pear/PHPUnit/Util/Report/Template/butter.png
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Report/Template/chameleon.png %{buildroot}%{_datadir}/pear/PHPUnit/Util/Report/Template/chameleon.png
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Report/Template/coverage_directory.html %{buildroot}%{_datadir}/pear/PHPUnit/Util/Report/Template/coverage_directory.html
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Report/Template/coverage_file.html %{buildroot}%{_datadir}/pear/PHPUnit/Util/Report/Template/coverage_file.html
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Report/Template/coverage_item.html %{buildroot}%{_datadir}/pear/PHPUnit/Util/Report/Template/coverage_item.html
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Report/Template/coverage_item_details.html %{buildroot}%{_datadir}/pear/PHPUnit/Util/Report/Template/coverage_item_details.html
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Report/Template/coverage_item_details_header.html %{buildroot}%{_datadir}/pear/PHPUnit/Util/Report/Template/coverage_item_details_header.html
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Report/Template/glass.png %{buildroot}%{_datadir}/pear/PHPUnit/Util/Report/Template/glass.png
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Report/Template/scarlet_red.png %{buildroot}%{_datadir}/pear/PHPUnit/Util/Report/Template/scarlet_red.png
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Report/Template/snow.png %{buildroot}%{_datadir}/pear/PHPUnit/Util/Report/Template/snow.png
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Report/Template/style.css %{buildroot}%{_datadir}/pear/PHPUnit/Util/Report/Template/style.css
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Report/Template/testsuite.html %{buildroot}%{_datadir}/pear/PHPUnit/Util/Report/Template/testsuite.html
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Report/Template/testsuite_item.html %{buildroot}%{_datadir}/pear/PHPUnit/Util/Report/Template/testsuite_item.html
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Report/Test/Node/Test.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/Report/Test/Node/Test.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Report/Test/Node/TestSuite.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/Report/Test/Node/TestSuite.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Report/Test/Factory.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/Report/Test/Factory.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Report/Test/Node.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/Report/Test/Node.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Report/GraphViz.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/Report/GraphViz.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Skeleton/IncompleteTestMethod.tpl %{buildroot}%{_datadir}/pear/PHPUnit/Util/Skeleton/IncompleteTestMethod.tpl
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Skeleton/TestClass.tpl %{buildroot}%{_datadir}/pear/PHPUnit/Util/Skeleton/TestClass.tpl
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Skeleton/TestMethod.tpl %{buildroot}%{_datadir}/pear/PHPUnit/Util/Skeleton/TestMethod.tpl
install -m0644 PHPUnit-%{version}/PHPUnit/Util/TestDox/ResultPrinter/HTML.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/TestDox/ResultPrinter/HTML.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/TestDox/ResultPrinter/Text.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/TestDox/ResultPrinter/Text.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/TestDox/NamePrettifier.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/TestDox/NamePrettifier.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/TestDox/ResultPrinter.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/TestDox/ResultPrinter.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Array.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/Array.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/ErrorHandler.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/ErrorHandler.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Fileloader.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/Fileloader.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Filesystem.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/Filesystem.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Filter.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/Filter.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/FilterIterator.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/FilterIterator.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Getopt.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/Getopt.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Printer.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/Printer.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Report.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/Report.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Skeleton.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/Skeleton.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Template.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/Template.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Test.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/Test.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Timer.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/Timer.php
install -m0644 PHPUnit-%{version}/PHPUnit/Util/Type.php %{buildroot}%{_datadir}/pear/PHPUnit/Util/Type.php
install -m0644 PHPUnit-%{version}/PHPUnit/Framework.php %{buildroot}%{_datadir}/pear/PHPUnit/Framework.php
install -m0644 PHPUnit-%{version}/PHPUnit2/Extensions/ExceptionTestCase.php %{buildroot}%{_datadir}/pear/PHPUnit2/Extensions/ExceptionTestCase.php
install -m0644 PHPUnit-%{version}/PHPUnit2/Extensions/PerformanceTestCase.php %{buildroot}%{_datadir}/pear/PHPUnit2/Extensions/PerformanceTestCase.php
install -m0644 PHPUnit-%{version}/PHPUnit2/Extensions/RepeatedTest.php %{buildroot}%{_datadir}/pear/PHPUnit2/Extensions/RepeatedTest.php
install -m0644 PHPUnit-%{version}/PHPUnit2/Extensions/TestDecorator.php %{buildroot}%{_datadir}/pear/PHPUnit2/Extensions/TestDecorator.php
install -m0644 PHPUnit-%{version}/PHPUnit2/Extensions/TestSetup.php %{buildroot}%{_datadir}/pear/PHPUnit2/Extensions/TestSetup.php
install -m0644 PHPUnit-%{version}/PHPUnit2/Framework/Assert.php %{buildroot}%{_datadir}/pear/PHPUnit2/Framework/Assert.php
install -m0644 PHPUnit-%{version}/PHPUnit2/Framework/AssertionFailedError.php %{buildroot}%{_datadir}/pear/PHPUnit2/Framework/AssertionFailedError.php
install -m0644 PHPUnit-%{version}/PHPUnit2/Framework/ComparisonFailure.php %{buildroot}%{_datadir}/pear/PHPUnit2/Framework/ComparisonFailure.php
install -m0644 PHPUnit-%{version}/PHPUnit2/Framework/Error.php %{buildroot}%{_datadir}/pear/PHPUnit2/Framework/Error.php
install -m0644 PHPUnit-%{version}/PHPUnit2/Framework/IncompleteTest.php %{buildroot}%{_datadir}/pear/PHPUnit2/Framework/IncompleteTest.php
install -m0644 PHPUnit-%{version}/PHPUnit2/Framework/IncompleteTestError.php %{buildroot}%{_datadir}/pear/PHPUnit2/Framework/IncompleteTestError.php
install -m0644 PHPUnit-%{version}/PHPUnit2/Framework/Test.php %{buildroot}%{_datadir}/pear/PHPUnit2/Framework/Test.php
install -m0644 PHPUnit-%{version}/PHPUnit2/Framework/TestCase.php %{buildroot}%{_datadir}/pear/PHPUnit2/Framework/TestCase.php
install -m0644 PHPUnit-%{version}/PHPUnit2/Framework/TestListener.php %{buildroot}%{_datadir}/pear/PHPUnit2/Framework/TestListener.php
install -m0644 PHPUnit-%{version}/PHPUnit2/Framework/TestResult.php %{buildroot}%{_datadir}/pear/PHPUnit2/Framework/TestResult.php
install -m0644 PHPUnit-%{version}/PHPUnit2/Framework/TestSuite.php %{buildroot}%{_datadir}/pear/PHPUnit2/Framework/TestSuite.php
install -m0644 PHPUnit-%{version}/PHPUnit2/Framework/Warning.php %{buildroot}%{_datadir}/pear/PHPUnit2/Framework/Warning.php
install -m0644 PHPUnit-%{version}/PHPUnit2/Runner/BaseTestRunner.php %{buildroot}%{_datadir}/pear/PHPUnit2/Runner/BaseTestRunner.php
install -m0644 PHPUnit-%{version}/PHPUnit2/Runner/IncludePathTestCollector.php %{buildroot}%{_datadir}/pear/PHPUnit2/Runner/IncludePathTestCollector.php
install -m0644 PHPUnit-%{version}/PHPUnit2/Runner/StandardTestSuiteLoader.php %{buildroot}%{_datadir}/pear/PHPUnit2/Runner/StandardTestSuiteLoader.php
install -m0644 PHPUnit-%{version}/PHPUnit2/Runner/TestCollector.php %{buildroot}%{_datadir}/pear/PHPUnit2/Runner/TestCollector.php
install -m0644 PHPUnit-%{version}/PHPUnit2/Runner/TestSuiteLoader.php %{buildroot}%{_datadir}/pear/PHPUnit2/Runner/TestSuiteLoader.php
install -m0644 PHPUnit-%{version}/PHPUnit2/Runner/Version.php %{buildroot}%{_datadir}/pear/PHPUnit2/Runner/Version.php
install -m0644 PHPUnit-%{version}/PHPUnit2/TextUI/ResultPrinter.php %{buildroot}%{_datadir}/pear/PHPUnit2/TextUI/ResultPrinter.php
install -m0644 PHPUnit-%{version}/PHPUnit2/TextUI/TestRunner.php %{buildroot}%{_datadir}/pear/PHPUnit2/TextUI/TestRunner.php
install -m0644 PHPUnit-%{version}/PHPUnit2/Util/Log/PEAR.php %{buildroot}%{_datadir}/pear/PHPUnit2/Util/Log/PEAR.php
install -m0644 PHPUnit-%{version}/PHPUnit2/Util/Log/XML.php %{buildroot}%{_datadir}/pear/PHPUnit2/Util/Log/XML.php
install -m0644 PHPUnit-%{version}/PHPUnit2/Util/Filter.php %{buildroot}%{_datadir}/pear/PHPUnit2/Util/Filter.php

install -d %{buildroot}%{_bindir}
install -m0755 PHPUnit-%{version}/pear-phpunit %{buildroot}%{_bindir}/phpunit

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/PHPUnit.xml

# fix paths and such
find %{buildroot} -type f | xargs perl -pi -e "s|\@php_dir\@|%{_datadir}/pear|g"
find %{buildroot} -type f | xargs perl -pi -e "s|\@php_bin\@|%{_bindir}/php|g"
find %{buildroot} -type f | xargs perl -pi -e "s|\@package_version\@|%{version}|g"

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/PHPUnit.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/PHPUnit.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/PHPUnit.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/PHPUnit.xml
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
		%{_bindir}/pear uninstall --nodeps -r PHPUnit
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_bindir}/phpunit
%dir %{_datadir}/pear/PHPUnit
%dir %{_datadir}/pear/PHPUnit/Extensions
%dir %{_datadir}/pear/PHPUnit/Framework
%dir %{_datadir}/pear/PHPUnit/Framework/ComparisonFailure
%dir %{_datadir}/pear/PHPUnit/Framework/Constraint
%dir %{_datadir}/pear/PHPUnit/Framework/MockObject
%dir %{_datadir}/pear/PHPUnit/Framework/MockObject/Builder
%dir %{_datadir}/pear/PHPUnit/Framework/MockObject/Matcher
%dir %{_datadir}/pear/PHPUnit/Framework/MockObject/Stub
%dir %{_datadir}/pear/PHPUnit/Runner
%dir %{_datadir}/pear/PHPUnit/Samples
%dir %{_datadir}/pear/PHPUnit/Samples/BankAccount
%dir %{_datadir}/pear/PHPUnit/Samples/Money
%dir %{_datadir}/pear/PHPUnit/Tests
%dir %{_datadir}/pear/PHPUnit/Tests/Extensions
%dir %{_datadir}/pear/PHPUnit/Tests/Framework
%dir %{_datadir}/pear/PHPUnit/Tests/Runner
%dir %{_datadir}/pear/PHPUnit/Tests/Util
%dir %{_datadir}/pear/PHPUnit/Tests/Util/TestDox
%dir %{_datadir}/pear/PHPUnit/Tests/_files
%dir %{_datadir}/pear/PHPUnit/TextUI
%dir %{_datadir}/pear/PHPUnit/Util
%dir %{_datadir}/pear/PHPUnit/Util/Log
%dir %{_datadir}/pear/PHPUnit/Util/Report
%dir %{_datadir}/pear/PHPUnit/Util/Report/Coverage
%dir %{_datadir}/pear/PHPUnit/Util/Report/Coverage/Node
%dir %{_datadir}/pear/PHPUnit/Util/Report/Template
%dir %{_datadir}/pear/PHPUnit/Util/Report/Test
%dir %{_datadir}/pear/PHPUnit/Util/Report/Test/Node
%dir %{_datadir}/pear/PHPUnit/Util/Skeleton
%dir %{_datadir}/pear/PHPUnit/Util/TestDox
%dir %{_datadir}/pear/PHPUnit/Util/TestDox/ResultPrinter
%dir %{_datadir}/pear/PHPUnit2
%dir %{_datadir}/pear/PHPUnit2/Extensions
%dir %{_datadir}/pear/PHPUnit2/Framework
%dir %{_datadir}/pear/PHPUnit2/Runner
%dir %{_datadir}/pear/PHPUnit2/TextUI
%dir %{_datadir}/pear/PHPUnit2/Util
%dir %{_datadir}/pear/PHPUnit2/Util/Log
%{_datadir}/pear/PHPUnit/Extensions/ExceptionTestCase.php
%{_datadir}/pear/PHPUnit/Extensions/OutputTestCase.php
%{_datadir}/pear/PHPUnit/Extensions/PerformanceTestCase.php
%{_datadir}/pear/PHPUnit/Extensions/RepeatedTest.php
%{_datadir}/pear/PHPUnit/Extensions/SeleniumTestCase.php
%{_datadir}/pear/PHPUnit/Extensions/TestDecorator.php
%{_datadir}/pear/PHPUnit/Extensions/TestSetup.php
%{_datadir}/pear/PHPUnit/Framework/ComparisonFailure/Array.php
%{_datadir}/pear/PHPUnit/Framework/ComparisonFailure/Object.php
%{_datadir}/pear/PHPUnit/Framework/ComparisonFailure/Scalar.php
%{_datadir}/pear/PHPUnit/Framework/ComparisonFailure/String.php
%{_datadir}/pear/PHPUnit/Framework/ComparisonFailure/Type.php
%{_datadir}/pear/PHPUnit/Framework/Constraint/And.php
%{_datadir}/pear/PHPUnit/Framework/Constraint/ArrayHasKey.php
%{_datadir}/pear/PHPUnit/Framework/Constraint/FileExists.php
%{_datadir}/pear/PHPUnit/Framework/Constraint/GreaterThan.php
%{_datadir}/pear/PHPUnit/Framework/Constraint/IsAnything.php
%{_datadir}/pear/PHPUnit/Framework/Constraint/IsEqual.php
%{_datadir}/pear/PHPUnit/Framework/Constraint/IsIdentical.php
%{_datadir}/pear/PHPUnit/Framework/Constraint/IsInstanceOf.php
%{_datadir}/pear/PHPUnit/Framework/Constraint/IsType.php
%{_datadir}/pear/PHPUnit/Framework/Constraint/LessThan.php
%{_datadir}/pear/PHPUnit/Framework/Constraint/Not.php
%{_datadir}/pear/PHPUnit/Framework/Constraint/ObjectHasAttribute.php
%{_datadir}/pear/PHPUnit/Framework/Constraint/Or.php
%{_datadir}/pear/PHPUnit/Framework/Constraint/PCREMatch.php
%{_datadir}/pear/PHPUnit/Framework/Constraint/StringContains.php
%{_datadir}/pear/PHPUnit/Framework/Constraint/TraversableContains.php
%{_datadir}/pear/PHPUnit/Framework/Constraint/Xor.php
%{_datadir}/pear/PHPUnit/Framework/MockObject/Builder/Identity.php
%{_datadir}/pear/PHPUnit/Framework/MockObject/Builder/InvocationMocker.php
%{_datadir}/pear/PHPUnit/Framework/MockObject/Builder/Match.php
%{_datadir}/pear/PHPUnit/Framework/MockObject/Builder/MethodNameMatch.php
%{_datadir}/pear/PHPUnit/Framework/MockObject/Builder/Namespace.php
%{_datadir}/pear/PHPUnit/Framework/MockObject/Builder/ParametersMatch.php
%{_datadir}/pear/PHPUnit/Framework/MockObject/Builder/Stub.php
%{_datadir}/pear/PHPUnit/Framework/MockObject/Matcher/AnyInvokedCount.php
%{_datadir}/pear/PHPUnit/Framework/MockObject/Matcher/AnyParameters.php
%{_datadir}/pear/PHPUnit/Framework/MockObject/Matcher/Invocation.php
%{_datadir}/pear/PHPUnit/Framework/MockObject/Matcher/InvokedAtIndex.php
%{_datadir}/pear/PHPUnit/Framework/MockObject/Matcher/InvokedAtLeastOnce.php
%{_datadir}/pear/PHPUnit/Framework/MockObject/Matcher/InvokedCount.php
%{_datadir}/pear/PHPUnit/Framework/MockObject/Matcher/InvokedRecorder.php
%{_datadir}/pear/PHPUnit/Framework/MockObject/Matcher/MethodName.php
%{_datadir}/pear/PHPUnit/Framework/MockObject/Matcher/Parameters.php
%{_datadir}/pear/PHPUnit/Framework/MockObject/Matcher/StatelessInvocation.php
%{_datadir}/pear/PHPUnit/Framework/MockObject/Stub/ConsecutiveCalls.php
%{_datadir}/pear/PHPUnit/Framework/MockObject/Stub/MatcherCollection.php
%{_datadir}/pear/PHPUnit/Framework/MockObject/Stub/Return.php
%{_datadir}/pear/PHPUnit/Framework/MockObject/Invocation.php
%{_datadir}/pear/PHPUnit/Framework/MockObject/InvocationMocker.php
%{_datadir}/pear/PHPUnit/Framework/MockObject/Invokable.php
%{_datadir}/pear/PHPUnit/Framework/MockObject/Matcher.php
%{_datadir}/pear/PHPUnit/Framework/MockObject/Mock.php
%{_datadir}/pear/PHPUnit/Framework/MockObject/MockObject.php
%{_datadir}/pear/PHPUnit/Framework/MockObject/Stub.php
%{_datadir}/pear/PHPUnit/Framework/MockObject/Verifiable.php
%{_datadir}/pear/PHPUnit/Framework/Assert.php
%{_datadir}/pear/PHPUnit/Framework/AssertionFailedError.php
%{_datadir}/pear/PHPUnit/Framework/ComparisonFailure.php
%{_datadir}/pear/PHPUnit/Framework/Constraint.php
%{_datadir}/pear/PHPUnit/Framework/Error.php
%{_datadir}/pear/PHPUnit/Framework/ExpectationFailedException.php
%{_datadir}/pear/PHPUnit/Framework/IncompleteTest.php
%{_datadir}/pear/PHPUnit/Framework/IncompleteTestError.php
%{_datadir}/pear/PHPUnit/Framework/SelfDescribing.php
%{_datadir}/pear/PHPUnit/Framework/SkippedTest.php
%{_datadir}/pear/PHPUnit/Framework/SkippedTestError.php
%{_datadir}/pear/PHPUnit/Framework/Test.php
%{_datadir}/pear/PHPUnit/Framework/TestCase.php
%{_datadir}/pear/PHPUnit/Framework/TestFailure.php
%{_datadir}/pear/PHPUnit/Framework/TestListener.php
%{_datadir}/pear/PHPUnit/Framework/TestResult.php
%{_datadir}/pear/PHPUnit/Framework/TestSuite.php
%{_datadir}/pear/PHPUnit/Framework/Warning.php
%{_datadir}/pear/PHPUnit/Runner/BaseTestRunner.php
%{_datadir}/pear/PHPUnit/Runner/IncludePathTestCollector.php
%{_datadir}/pear/PHPUnit/Runner/StandardTestSuiteLoader.php
%{_datadir}/pear/PHPUnit/Runner/TestCollector.php
%{_datadir}/pear/PHPUnit/Runner/TestSuiteLoader.php
%{_datadir}/pear/PHPUnit/Runner/Version.php
%{_datadir}/pear/PHPUnit/Samples/BankAccount/BankAccount.php
%{_datadir}/pear/PHPUnit/Samples/BankAccount/BankAccountTest.php
%{_datadir}/pear/PHPUnit/Samples/Money/IMoney.php
%{_datadir}/pear/PHPUnit/Samples/Money/Money.php
%{_datadir}/pear/PHPUnit/Samples/Money/MoneyBag.php
%{_datadir}/pear/PHPUnit/Samples/Money/MoneyTest.php
%{_datadir}/pear/PHPUnit/Samples/FailureTest.php
%{_datadir}/pear/PHPUnit/Tests/Extensions/AllTests.php
%{_datadir}/pear/PHPUnit/Tests/Extensions/ExceptionTestCaseTest.php
%{_datadir}/pear/PHPUnit/Tests/Extensions/ExtensionTest.php
%{_datadir}/pear/PHPUnit/Tests/Extensions/OutputTestCaseTest.php
%{_datadir}/pear/PHPUnit/Tests/Extensions/PerformanceTestCaseTest.php
%{_datadir}/pear/PHPUnit/Tests/Extensions/RepeatedTestTest.php
%{_datadir}/pear/PHPUnit/Tests/Extensions/SeleniumTestCaseTest.php
%{_datadir}/pear/PHPUnit/Tests/Framework/AllTests.php
%{_datadir}/pear/PHPUnit/Tests/Framework/AssertTest.php
%{_datadir}/pear/PHPUnit/Tests/Framework/ComparisonFailureTest.php
%{_datadir}/pear/PHPUnit/Tests/Framework/ConstraintTest.php
%{_datadir}/pear/PHPUnit/Tests/Framework/MockObjectTest.php
%{_datadir}/pear/PHPUnit/Tests/Framework/SuiteTest.php
%{_datadir}/pear/PHPUnit/Tests/Framework/TestCaseTest.php
%{_datadir}/pear/PHPUnit/Tests/Framework/TestImplementorTest.php
%{_datadir}/pear/PHPUnit/Tests/Framework/TestListenerTest.php
%{_datadir}/pear/PHPUnit/Tests/Runner/AllTests.php
%{_datadir}/pear/PHPUnit/Tests/Runner/BaseTestRunnerTest.php
%{_datadir}/pear/PHPUnit/Tests/Util/TestDox/AllTests.php
%{_datadir}/pear/PHPUnit/Tests/Util/TestDox/NamePrettifierTest.php
%{_datadir}/pear/PHPUnit/Tests/Util/AllTests.php
%{_datadir}/pear/PHPUnit/Tests/_files/AnInterface.php
%{_datadir}/pear/PHPUnit/Tests/_files/ClassWithNonPublicAttributes.php
%{_datadir}/pear/PHPUnit/Tests/_files/DoubleTestCase.php
%{_datadir}/pear/PHPUnit/Tests/_files/Error.php
%{_datadir}/pear/PHPUnit/Tests/_files/Failure.php
%{_datadir}/pear/PHPUnit/Tests/_files/InheritedTestCase.php
%{_datadir}/pear/PHPUnit/Tests/_files/MockRunner.php
%{_datadir}/pear/PHPUnit/Tests/_files/NoArgTestCaseTest.php
%{_datadir}/pear/PHPUnit/Tests/_files/NonStatic.php
%{_datadir}/pear/PHPUnit/Tests/_files/NoTestCaseClass.php
%{_datadir}/pear/PHPUnit/Tests/_files/NoTestCases.php
%{_datadir}/pear/PHPUnit/Tests/_files/NotPublicTestCase.php
%{_datadir}/pear/PHPUnit/Tests/_files/NotVoidTestCase.php
%{_datadir}/pear/PHPUnit/Tests/_files/OneTestCase.php
%{_datadir}/pear/PHPUnit/Tests/_files/OutputTestCase.php
%{_datadir}/pear/PHPUnit/Tests/_files/OverrideTestCase.php
%{_datadir}/pear/PHPUnit/Tests/_files/SampleClass.php
%{_datadir}/pear/PHPUnit/Tests/_files/SetupFailure.php
%{_datadir}/pear/PHPUnit/Tests/_files/Sleep.php
%{_datadir}/pear/PHPUnit/Tests/_files/Struct.php
%{_datadir}/pear/PHPUnit/Tests/_files/Success.php
%{_datadir}/pear/PHPUnit/Tests/_files/TearDownFailure.php
%{_datadir}/pear/PHPUnit/Tests/_files/TestIterator.php
%{_datadir}/pear/PHPUnit/Tests/_files/ThrowExceptionTestCase.php
%{_datadir}/pear/PHPUnit/Tests/_files/ThrowNoExceptionTestCase.php
%{_datadir}/pear/PHPUnit/Tests/_files/TornDown.php
%{_datadir}/pear/PHPUnit/Tests/_files/TornDown2.php
%{_datadir}/pear/PHPUnit/Tests/_files/TornDown3.php
%{_datadir}/pear/PHPUnit/Tests/_files/TornDown4.php
%{_datadir}/pear/PHPUnit/Tests/_files/TornDown5.php
%{_datadir}/pear/PHPUnit/Tests/_files/TornDown6.php
%{_datadir}/pear/PHPUnit/Tests/_files/WasRun.php
%{_datadir}/pear/PHPUnit/Tests/AllTests.php
%{_datadir}/pear/PHPUnit/Tests/TestConfiguration.php
%{_datadir}/pear/PHPUnit/TextUI/Command.php
%{_datadir}/pear/PHPUnit/TextUI/ResultPrinter.php
%{_datadir}/pear/PHPUnit/TextUI/TestRunner.php
%{_datadir}/pear/PHPUnit/Util/Log/GraphViz.php
%{_datadir}/pear/PHPUnit/Util/Log/JSON.php
%{_datadir}/pear/PHPUnit/Util/Log/PEAR.php
%{_datadir}/pear/PHPUnit/Util/Log/TAP.php
%{_datadir}/pear/PHPUnit/Util/Log/XML.php
%{_datadir}/pear/PHPUnit/Util/Report/Coverage/Node/Directory.php
%{_datadir}/pear/PHPUnit/Util/Report/Coverage/Node/File.php
%{_datadir}/pear/PHPUnit/Util/Report/Coverage/Factory.php
%{_datadir}/pear/PHPUnit/Util/Report/Coverage/Node.php
%{_datadir}/pear/PHPUnit/Util/Report/Template/butter.png
%{_datadir}/pear/PHPUnit/Util/Report/Template/chameleon.png
%{_datadir}/pear/PHPUnit/Util/Report/Template/coverage_directory.html
%{_datadir}/pear/PHPUnit/Util/Report/Template/coverage_file.html
%{_datadir}/pear/PHPUnit/Util/Report/Template/coverage_item.html
%{_datadir}/pear/PHPUnit/Util/Report/Template/coverage_item_details.html
%{_datadir}/pear/PHPUnit/Util/Report/Template/coverage_item_details_header.html
%{_datadir}/pear/PHPUnit/Util/Report/Template/glass.png
%{_datadir}/pear/PHPUnit/Util/Report/Template/scarlet_red.png
%{_datadir}/pear/PHPUnit/Util/Report/Template/snow.png
%{_datadir}/pear/PHPUnit/Util/Report/Template/style.css
%{_datadir}/pear/PHPUnit/Util/Report/Template/testsuite.html
%{_datadir}/pear/PHPUnit/Util/Report/Template/testsuite_item.html
%{_datadir}/pear/PHPUnit/Util/Report/Test/Node/Test.php
%{_datadir}/pear/PHPUnit/Util/Report/Test/Node/TestSuite.php
%{_datadir}/pear/PHPUnit/Util/Report/Test/Factory.php
%{_datadir}/pear/PHPUnit/Util/Report/Test/Node.php
%{_datadir}/pear/PHPUnit/Util/Report/GraphViz.php
%{_datadir}/pear/PHPUnit/Util/Skeleton/IncompleteTestMethod.tpl
%{_datadir}/pear/PHPUnit/Util/Skeleton/TestClass.tpl
%{_datadir}/pear/PHPUnit/Util/Skeleton/TestMethod.tpl
%{_datadir}/pear/PHPUnit/Util/TestDox/ResultPrinter/HTML.php
%{_datadir}/pear/PHPUnit/Util/TestDox/ResultPrinter/Text.php
%{_datadir}/pear/PHPUnit/Util/TestDox/NamePrettifier.php
%{_datadir}/pear/PHPUnit/Util/TestDox/ResultPrinter.php
%{_datadir}/pear/PHPUnit/Util/Array.php
%{_datadir}/pear/PHPUnit/Util/ErrorHandler.php
%{_datadir}/pear/PHPUnit/Util/Fileloader.php
%{_datadir}/pear/PHPUnit/Util/Filesystem.php
%{_datadir}/pear/PHPUnit/Util/Filter.php
%{_datadir}/pear/PHPUnit/Util/FilterIterator.php
%{_datadir}/pear/PHPUnit/Util/Getopt.php
%{_datadir}/pear/PHPUnit/Util/Printer.php
%{_datadir}/pear/PHPUnit/Util/Report.php
%{_datadir}/pear/PHPUnit/Util/Skeleton.php
%{_datadir}/pear/PHPUnit/Util/Template.php
%{_datadir}/pear/PHPUnit/Util/Test.php
%{_datadir}/pear/PHPUnit/Util/Timer.php
%{_datadir}/pear/PHPUnit/Util/Type.php
%{_datadir}/pear/PHPUnit/Framework.php
%{_datadir}/pear/PHPUnit2/Extensions/ExceptionTestCase.php
%{_datadir}/pear/PHPUnit2/Extensions/PerformanceTestCase.php
%{_datadir}/pear/PHPUnit2/Extensions/RepeatedTest.php
%{_datadir}/pear/PHPUnit2/Extensions/TestDecorator.php
%{_datadir}/pear/PHPUnit2/Extensions/TestSetup.php
%{_datadir}/pear/PHPUnit2/Framework/Assert.php
%{_datadir}/pear/PHPUnit2/Framework/AssertionFailedError.php
%{_datadir}/pear/PHPUnit2/Framework/ComparisonFailure.php
%{_datadir}/pear/PHPUnit2/Framework/Error.php
%{_datadir}/pear/PHPUnit2/Framework/IncompleteTest.php
%{_datadir}/pear/PHPUnit2/Framework/IncompleteTestError.php
%{_datadir}/pear/PHPUnit2/Framework/Test.php
%{_datadir}/pear/PHPUnit2/Framework/TestCase.php
%{_datadir}/pear/PHPUnit2/Framework/TestListener.php
%{_datadir}/pear/PHPUnit2/Framework/TestResult.php
%{_datadir}/pear/PHPUnit2/Framework/TestSuite.php
%{_datadir}/pear/PHPUnit2/Framework/Warning.php
%{_datadir}/pear/PHPUnit2/Runner/BaseTestRunner.php
%{_datadir}/pear/PHPUnit2/Runner/IncludePathTestCollector.php
%{_datadir}/pear/PHPUnit2/Runner/StandardTestSuiteLoader.php
%{_datadir}/pear/PHPUnit2/Runner/TestCollector.php
%{_datadir}/pear/PHPUnit2/Runner/TestSuiteLoader.php
%{_datadir}/pear/PHPUnit2/Runner/Version.php
%{_datadir}/pear/PHPUnit2/TextUI/ResultPrinter.php
%{_datadir}/pear/PHPUnit2/TextUI/TestRunner.php
%{_datadir}/pear/PHPUnit2/Util/Log/PEAR.php
%{_datadir}/pear/PHPUnit2/Util/Log/XML.php
%{_datadir}/pear/PHPUnit2/Util/Filter.php
%{_datadir}/pear/packages/PHPUnit.xml
