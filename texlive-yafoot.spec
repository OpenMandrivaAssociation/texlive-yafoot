# revision 19086
# category Package
# catalog-ctan /macros/latex/contrib/yafoot
# catalog-date 2006-12-16 10:58:44 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-yafoot
Version:	20180303
Release:	2
Summary:	A bundle of miscellaneous footnote packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/yafoot
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yafoot.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yafoot.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yafoot.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Contains three packages: - pfnote to number footnotes per page;
- fnpos to control the position of footnotes; and - dblfnote to
make footnotes double-columned.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/yafoot/dblfnote.sty
%{_texmfdistdir}/tex/latex/yafoot/fnpos.sty
%{_texmfdistdir}/tex/latex/yafoot/pfnote.sty
%doc %{_texmfdistdir}/doc/latex/yafoot/README
%doc %{_texmfdistdir}/doc/latex/yafoot/yafoot-man.pdf
%doc %{_texmfdistdir}/doc/latex/yafoot/yafoot-man.tex
#- source
%doc %{_texmfdistdir}/source/latex/yafoot/yafoot.dtx
%doc %{_texmfdistdir}/source/latex/yafoot/yafoot.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20061216-2
+ Revision: 757738
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20061216-1
+ Revision: 719959
- texlive-yafoot
- texlive-yafoot
- texlive-yafoot

