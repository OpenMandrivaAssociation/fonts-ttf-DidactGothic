%define pkgname DidactGothic

Summary:	Sans-serif font
Name:		fonts-ttf-DidactGothic
Version:	20110825
Release:	2
License:	OFL
Group:		System/Fonts/True type
URL:		http://io.debian.net/~danielj/
Source0:	http://io.debian.net/~danielj/DidactGothic/%{pkgname}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	freetype-tools
BuildRequires:	dos2unix

%description
Didact Gothic is a sans-serif font designed to present each letter in the form
most often used in elementary classrooms. This makes it very suitable
for literacy efforts.

The font supports all of Basic Latin, Latin-1 Supplement, and most of Latin
Extended-A. It supports almost all Latin-alphabet European languages.
It also supports the major Cyrillic scripts, including non-Slavic languages,
as well as modern and polytonic Greek.

%prep
%setup -q -c -n %{pkgname}-%{version}
chmod -x *
dos2unix OFL.txt

%build

%install
%__mkdir_p %{buildroot}%{_xfontdir}/TTF/DidactGothic

%__install -m 644 *.ttf %{buildroot}%{_xfontdir}/TTF/DidactGothic
ttmkfdir %{buildroot}%{_xfontdir}/TTF/DidactGothic -o %{buildroot}%{_xfontdir}/TTF/DidactGothic/fonts.dir
%__ln_s fonts.dir %{buildroot}%{_xfontdir}/TTF/DidactGothic/fonts.scale

%__mkdir_p %{buildroot}%_sysconfdir/X11/fontpath.d/
%__ln_s ../../..%{_xfontdir}/TTF/DidactGothic \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-DidactGothic:pri=50

%files
%doc FONTLOG.txt OFL.txt
%dir %{_xfontdir}/TTF/DidactGothic
%{_xfontdir}/TTF/DidactGothic/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/DidactGothic/fonts.dir
%{_xfontdir}/TTF/DidactGothic/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-DidactGothic:pri=50


%changelog
* Fri Dec 09 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 20110825-1mdv2011.0
+ Revision: 739440
- imported package fonts-ttf-DidactGothic

