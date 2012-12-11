%{!?_texmf: %global _texmf %(eval "echo `kpsewhich -expand-var '$TEXMFMAIN'`")}

%define texpkg      llncs
%define texpkgdir   %{_texmf}/tex/latex/%{texpkg}
%define texpkgdoc   %{_texmf}/doc/latex/%{texpkg}
%define bibpkgdir   %{_texmf}/bibtex/bib/%{texpkg}
%define bstpkgdir   %{_texmf}/bibtex/bst/%{texpkg}
%define bibpkgdoc   %{_texmf}/doc/bibtex/%{texpkg}

Name:           tetex-%{texpkg}
Version:        2.14.2007.12.11
Release:        %mkrel 3
Epoch:          0
Summary:        LaTeX2e package for Springer-Verlag Lecture Notes in Computer Science (LNCS)
Group:          Publishing
License:        Distributable
URL:            http://www.springer.com/
Source0:        ftp://ftp.springer.de/pub/tex/latex/llncs/latex2e/llncs2e.zip
Requires:       tetex-latex
Requires(post): tetex
Requires(postun): tetex
BuildRequires:  tetex-latex
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The LaTeX2e package for Lecture Notes in Computer Science (LNCS) of
Springer-Verlag.

%prep
%setup -q -c -n %{texpkg}
%{__perl} -pi -e 's/\r$//g' *.bst *.cls *.dem *.doc *.ind *.me *.sty *.txt

%build

%install
%{__rm} -rf %{buildroot}

%{__mkdir_p} %{buildroot}{%{texpkgdir},%{texpkgdoc}}
%{__cp} -a llncs.cls %{buildroot}%{texpkgdir}/
%{__cp} -a sprmindx.sty %{buildroot}%{texpkgdir}/
%{__cp} -a llncsdoc.pdf %{buildroot}%{texpkgdoc}/
%{__cp} -a llncsdoc.sty %{buildroot}%{texpkgdoc}/
%{__cp} -a llncs.dem %{buildroot}%{texpkgdoc}/
%{__cp} -a llncs.doc %{buildroot}%{texpkgdoc}/
%{__cp} -a llncs.ind %{buildroot}%{texpkgdoc}/
%{__cp} -a subjidx.ind %{buildroot}%{texpkgdoc}/
%{__cp} -a llncs.dvi %{buildroot}%{texpkgdoc}/

%{__mkdir_p} %{buildroot}{%{bibpkgdir},%{bstpkgdir},%{bibpkgdoc}}
%{__cp} -a splncs.bst %{buildroot}%{bstpkgdir}/

%clean
%{__rm} -rf %{buildroot}


%post
if [ -x %{_bindir}/texhash ] ; then
    %{_bindir}/texhash >/dev/null 2>&1 || :
fi

%postun
if [ -x %{_bindir}/texhash ] ; then
    %{_bindir}/texhash >/dev/null 2>&1 || :
fi

%triggerin -- lyx
if [ $2 -gt 1 ]; then
cd %{_datadir}/lyx && \
  ./configure.py --without-latex-config > /dev/null 2>&1 ||:
fi

%triggerun -- lyx
if [ $2 -eq 0 ]; then
cd %{_datadir}/lyx && \
  ./configure.py --without-latex-config > /dev/null 2>&1 ||:
fi

%files
%defattr(0644,root,root,0755)
%doc history.txt read.me
%{texpkgdir}
%{texpkgdoc}
%{bibpkgdir}
%{bstpkgdir}
%{bibpkgdoc}


%changelog
* Tue Sep 01 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0:2.14.2007.12.11-3mdv2010.0
+ Revision: 423770
- rebuild

* Mon Jun 16 2008 Thierry Vignaud <tvignaud@mandriva.com> 0:2.14.2007.12.11-2mdv2009.0
+ Revision: 220282
- rebuild

* Fri May 02 2008 David Walluck <walluck@mandriva.org> 0:2.14.2007.12.11-1mdv2009.0
+ Revision: 200488
- 2.14.2007.12.11 (2.14 11.12.07)
- check for texhash in scriptlets

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Apr 29 2007 David Walluck <walluck@mandriva.org> 0:2.14-1mdv2008.0
+ Revision: 19064
- Import tetex-llncs



* Sun Apr 29 2007 David Walluck <walluck@mandriva.org> 0:2.14-1mdv2008.0
- release
