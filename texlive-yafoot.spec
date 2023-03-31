Name:		texlive-yafoot
Version:	48568
Release:	2
Summary:	A bundle of miscellaneous footnote packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/yafoot
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yafoot.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yafoot.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yafoot.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
