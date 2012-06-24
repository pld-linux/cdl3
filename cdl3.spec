Summary:	CDL3 System - compiler
Summary(pl):	Kompilator systemu CDL3
Name:		cdl3
Version:	1.2.3
Release:	0.1
License:	GPL
Group:		Development/Languages
Source0:	ftp://ftp.cs.kun.nl/pub/cdl3/%{name}-%{version}.tar.gz
# Source0-md5:	60b7a5fed2ac27f4dfe90ff9ae292bce
Patch0:		%{name}-acam.patch
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

%description -l pl
CDL3 to j�zyk implementacyjny oparty na gramatykach affiksowych.
Przekracza granic� pomi�dzy formalizmem sk�adniowym a j�zykiem
programowania i pr�buje po��czy� dobre cechy obu rzeczy. Struktura
steruj�ca i struktury danych zosta�y tak dobrane, aby by�o bardzo
�atwo pisa� w CDL3 deterministyczne analizatory i translatory. W tym
sensie CDL3 jest j�zykiem opisu kompilator�w (Compiler Description
Language - st�d akronim). Jego zastosowanie nie jest jednak
ograniczone do konstruowania kompilator�w. J�zyk jest dobrze
dopasowany, bardziej og�lnie, do wszystkich zastosowa�, kt�re mo�na
scharakteryzowa� jako zorientowane na sk�adni�: komunikacji mi�dzy
procesami (cz�owiekiem i maszyn�) zgodnie z dobrze ustalonymi
protoko�ami lub systemy w stylu interpreter�w, interaktywnie reaguj�ce
na zestaw polece�.

%prep
%setup -q
%patch0 -p1

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO docs/*.ps docs/*.k3
%attr(755,root,root) %{_bindir}/*
%{_includedir}/*
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_mandir}/man[13n]/*
