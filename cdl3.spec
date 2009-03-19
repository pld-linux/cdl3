Summary:	CDL3 System - compiler
Summary(pl.UTF-8):	Kompilator systemu CDL3
Name:		cdl3
Version:	1.2.7
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	ftp://ftp.cs.kun.nl/pub/cdl3/%{name}-%{version}.tar.gz
# Source0-md5:	d028bf290af22ec8c90ea11ca9a88fda
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CDL3 is an implementation language based on affix grammars. It rides
the borderline between syntactic formalism and programming language,
and tries to combine the good properties of both. The control
structure and data structures have been choosen such that it is
extremely easy to write deterministic parsers and transducers in CDL3.
In this sense, CDL3 is a Compiler Description Language (hence the
acronym). Its applicability is, however, not limited to compiler
construction. The language is wellsuited, more in general, for all
applications that can be characterized as syntax-directed:
communication between processes (human and machine) adhering to
well-established protocols, or interpreter-like systems, interactively
obeying a set of commands.

%description -l pl.UTF-8
CDL3 to język implementacyjny oparty na gramatykach affiksowych.
Przekracza granicę pomiędzy formalizmem składniowym a językiem
programowania i próbuje połączyć dobre cechy obu rzeczy. Struktura
sterująca i struktury danych zostały tak dobrane, aby było bardzo
łatwo pisać w CDL3 deterministyczne analizatory i translatory. W tym
sensie CDL3 jest językiem opisu kompilatorów (Compiler Description
Language - stąd akronim). Jego zastosowanie nie jest jednak
ograniczone do konstruowania kompilatorów. Język jest dobrze
dopasowany, bardziej ogólnie, do wszystkich zastosowań, które można
scharakteryzować jako zorientowane na składnię: komunikacji między
procesami (człowiekiem i maszyną) zgodnie z dobrze ustalonymi
protokołami lub systemy w stylu interpreterów, interaktywnie reagujące
na zestaw poleceń.

%package examples
Summary:        CDL3 - example of use
Summary(pl.UTF-8):      CDL3 - przykłady wykorzystania
Group:          Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description examples
CDL3 - example of use.

%description examples -l pl.UTF-8
CDL3 - przykłady wykorzystania.

%prep
%setup -q
%{__sed} -i -e 's,CLK_TCK,CLOCKS_PER_SEC,g' rts/cdl3rts.c

%build
cp -f /usr/share/automake/config.sub .
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/cdl3/include/*.h $RPM_BUILD_ROOT%{_includedir}
mv -f $RPM_BUILD_ROOT%{_datadir}/cdl3/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO docs/*.ps docs/*.k3
%attr(755,root,root) %{_bindir}/cdlc
%{_includedir}/*
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_mandir}/man[137n]/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
