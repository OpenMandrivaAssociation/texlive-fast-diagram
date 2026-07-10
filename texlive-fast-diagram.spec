%global tl_name fast-diagram
%global tl_revision 29264

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Easy generation of FAST diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/fast-diagram
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fast-diagram.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fast-diagram.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides simple means of producing FAST diagrams, using
TikZ/pgf tools. FAST diagrams are useful for functional analysis
techniques in design methods.

