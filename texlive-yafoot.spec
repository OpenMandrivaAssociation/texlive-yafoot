%global tl_name yafoot
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	A bundle of miscellaneous footnote packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/yafoot
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yafoot.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yafoot.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yafoot.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Contains three packages: - pfnote to number footnotes per page; - fnpos
to control the position of footnotes; and - dblfnote to make footnotes
double-columned.

