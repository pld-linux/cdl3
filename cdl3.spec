Summary:	CDL3 System - compiler
Summary(pl):	Kompilator systemu CDL3
Name:		cdl3
Version:	1.2.3
Release:	0.1
License:	GPL
Group:		Development/Languages
Source0:	ftp://ftp.cs.kun.nl/pub/cdl3/%{name}-%{version}.tar.gz
Patch0:		%{name}-acam.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CDL3 system

%description -l pl
system CDL3

%prep
%setup -q
%patch0 -p 1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake} -a -c
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
