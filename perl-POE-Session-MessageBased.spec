#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	Session-MessageBased
Summary:	POE::Session::MessageBased - a message-based (not @_ based) POE::Session
#Summary(pl):	
Name:		perl-POE-Session-MessageBased
Version:	0.01
Release:	1
# same as perl
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	49c7e1e8a3e1e749b96ce7e53829e8f4
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{!?_without_tests:1}0
BuildRequires:	perl-POE >= 0.25
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Session::MessageBased exists mainly to replace @_[KERNEL, etc.]
with message objects that encapsulate various aspects of each event.
It also exists as an example of a subclassed POE::Session, in case
someone wants to create new callback or Session semantics.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
%{perl_vendorlib}/%{pdir}/*/*.pm
%{_mandir}/man3/*
