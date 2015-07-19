# revision 29264
# category Package
# catalog-ctan /graphics/pgf/contrib/fast-diagram
# catalog-date 2013-02-27 20:12:49 +0100
# catalog-license lppl1.3
# catalog-version 1.1
Name:		texlive-fast-diagram
Version:	1.1
Release:	9
Summary:	Easy generation of FAST diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/fast-diagram
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fast-diagram.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fast-diagram.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides simple means of producing FAST diagrams,
using TikZ/pgf tools. FAST diagrams are useful for functional
analysis techniques in design methods.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fast-diagram/fast-diagram.sty
%doc %{_texmfdistdir}/doc/latex/fast-diagram/README
%doc %{_texmfdistdir}/doc/latex/fast-diagram/help.pdf
%doc %{_texmfdistdir}/doc/latex/fast-diagram/help.tex
%doc %{_texmfdistdir}/doc/latex/fast-diagram/sources_help/commandes.tex
%doc %{_texmfdistdir}/doc/latex/fast-diagram/sources_help/exemple.tex
%doc %{_texmfdistdir}/doc/latex/fast-diagram/sources_help/images/antenne.png
%doc %{_texmfdistdir}/doc/latex/fast-diagram/sources_help/images/batterie.png
%doc %{_texmfdistdir}/doc/latex/fast-diagram/sources_help/images/biellettes.png
%doc %{_texmfdistdir}/doc/latex/fast-diagram/sources_help/images/bouton.png
%doc %{_texmfdistdir}/doc/latex/fast-diagram/sources_help/images/moteur.png
%doc %{_texmfdistdir}/doc/latex/fast-diagram/sources_help/images/pedalier.png
%doc %{_texmfdistdir}/doc/latex/fast-diagram/sources_help/images/pignons.png
%doc %{_texmfdistdir}/doc/latex/fast-diagram/sources_help/images/recepteur.png
%doc %{_texmfdistdir}/doc/latex/fast-diagram/sources_help/images/roue.png
%doc %{_texmfdistdir}/doc/latex/fast-diagram/sources_help/images/servomoteur.png
%doc %{_texmfdistdir}/doc/latex/fast-diagram/sources_help/installation.tex
%doc %{_texmfdistdir}/doc/latex/fast-diagram/sources_help/intro.tex
%doc %{_texmfdistdir}/doc/latex/fast-diagram/sources_help/miseEnForme.tex
%doc %{_texmfdistdir}/doc/latex/fast-diagram/sources_help/reglages.tex
%doc %{_texmfdistdir}/doc/latex/fast-diagram/sources_help/tikz.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
