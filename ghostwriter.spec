%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20230824

Name: ghostwriter
Version: 23.08.0
Release: %{?git:0.%{git}.}1
Group: Office
License: GPLv3+ and CC-BY and CC-BY-SA and MPLv1.1 and BSD and LGPLv3 and MIT and ISC
Summary: Cross-platform, aesthetic, distraction-free Markdown editor
URL: https://github.com/wereturtle/%{name}
%if 0%{?git:1}
Source0: https://github.com/wereturtle/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%else
Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
BuildRequires: qmake5
BuildRequires: cmake ninja
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Concurrent)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Help)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5WebEngine)
BuildRequires: cmake(Qt5WebEngineWidgets)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5XmlPatterns)
BuildRequires: cmake(KF5Sonnet)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: hunspell-devel
BuildRequires: pkgconfig(appstream-glib)

Provides: bundled(cmark-gfm) = 0.29.0
Provides: bundled(fontawesome-fonts) = 5.10.2
Provides: bundled(nodejs-mathjax-full) = 3.1.2
Provides: bundled(nodejs-react) = 17.0.1
Provides: bundled(QtAwesome) = 5

Requires: hicolor-icon-theme
Requires: qt5-qtwebengine

Recommends: cmark%{?_isa}
Recommends: multimarkdown%{?_isa}

%description
Ghostwriter is a text editor for Markdown, which is a plain text markup
format created by John Gruber. For more information about Markdown, please
visit John Gruberâ€™s website at http://www.daringfireball.net.

Ghostwriter provides a relaxing, distraction-free writing environment,
whether your masterpiece be that next blog post, your school paper,
or your novel.

%prep
%autosetup -n %{name}-%{?git:master}%{!?git:%{version}} -p1
rm -rf 3rdparty/hunspell
%cmake_kde5 \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name} --with-qt --with-man

%files -f %{name}.lang
%{_bindir}/ghostwriter
%{_datadir}/applications/org.kde.ghostwriter.desktop
%{_datadir}/icons/hicolor/*/apps/ghostwriter.*
%{_datadir}/metainfo/org.kde.ghostwriter.metainfo.xml
%{_mandir}/man1/ghostwriter.1*
