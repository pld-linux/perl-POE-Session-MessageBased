#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	Session-MessageBased
Summary:	POE::Session::MessageBased - a message-based (not @_ based) POE::Session
Summary(pl):	POE::Session::MessageBased - oparte na komunikatach (nie @_) POE::Session
Name:		perl-POE-Session-MessageBased
Version:	0.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	49c7e1e8a3e1e749b96ce7e53829e8f4
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-POE >= 0.25
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Session::MessageBased exists mainly to replace @_[KERNEL, etc.]
with message objects that encapsulate various aspects of each event.
It also exists as an example of a subclassed POE::Session, in case
someone wants to create new callback or Session semantics.

%description -l pl
POE::Session::MessageBased istnieje g³ównie po to, by zast±piæ
@_[KERNEL itp.] obiektami komunikatów, które s± opakowaniem ró¿nych
aspektów ka¿dego zdarzenia. Istnieje tak¿e jako przyk³ad podklasy
POE::Session, na wypadek gdyby kto¶ chcia³ stworzyæ now± semantykê
callbacka lub sesji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

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
