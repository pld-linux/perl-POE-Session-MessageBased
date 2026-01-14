#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	POE
%define		pnam	Session-MessageBased
Summary:	POE::Session::MessageBased - a message-based (not @_ based) POE::Session
Summary(pl.UTF-8):	POE::Session::MessageBased - oparte na komunikatach (nie @_) POE::Session
Name:		perl-POE-Session-MessageBased
Version:	0.111
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2f5ea8c09558656f5dac12112f0d8afc
URL:		http://search.cpan.org/dist/POE-Session-MessageBased/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-POE >= 1.007
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Session::MessageBased exists mainly to replace @_[KERNEL, etc.]
with message objects that encapsulate various aspects of each event.
It also exists as an example of a subclassed POE::Session, in case
someone wants to create new callback or Session semantics.

%description -l pl.UTF-8
POE::Session::MessageBased istnieje głównie po to, by zastąpić
@_[KERNEL itp.] obiektami komunikatów, które są opakowaniem różnych
aspektów każdego zdarzenia. Istnieje także jako przykład podklasy
POE::Session, na wypadek gdyby ktoś chciał stworzyć nową semantykę
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
