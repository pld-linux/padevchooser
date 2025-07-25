%define		subver	svn20070925
%define		rel		3
Summary:	PulseAudio Device Chooser
Summary(pl.UTF-8):	PulseAudio Device Chooser - narzędzie do wyboru urządzeń
Name:		padevchooser
Version:	0.9.4
Release:	0.%{subver}.%{rel}
License:	GPL v2+
Group:		X11/Applications/Sound
#Source0:	http://0pointer.de/lennart/projects/padevchooser/%{name}-%{version}.tar.gz
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/padevchooser/%{name}-%{version}.%{subver}.tar.gz/164cc955445b3165d49f3de48e9551cf/%{name}-%{version}.%{subver}.tar.gz
# Source0-md5:	164cc955445b3165d49f3de48e9551cf
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-libnotify.patch
URL:		http://0pointer.de/lennart/projects/padevchooser/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	gnome-desktop2-devel
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	libglade2-devel >= 1:2.0
BuildRequires:	libgnomeui-devel
BuildRequires:	libnotify-devel
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 0.9.2
Requires:	avahi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PulseAudio Device Chooser (padevchooser) is a simple GTK+ tool which
registers an icon in the tray area and allows quick access to some
features of the PulseAudio sound server. Specifically it can do for
you:
 - Notify about new sink/sources becoming available on the LAN
 - Quickly change the default PulseAudio sink/source/server assigned to
   the current X11 display, selecting devices available on the LAN
 - Start the auxiliary tools: PulseAudio Volume Control, PulseAudio
   Volume Meter, PulseAudio Manager, PulseAudio Preferences

%description -l pl.UTF-8
PulseAudio Device Chooser (padevchooser) to proste narzędzie GTK+
rejestrujące ikonę na pasku i pozwalające na szybki dostęp do
niektórych możliwości serwera dźwięku PulseAudio. W szczególności
potrafi:
 - powiadomić o nowych źródłach dostępnych w sieci lokalnej
 - szybko zmienić domyślne źródło/serwer PulseAudio przypisane do
   ekranu X11 wybierając urządzenia dostępne w sieci lokalnej
 - uruchomić dodatkowe narzędzia: mikser (PulseAudio Volume Control),
   miernik głośności (PulseAudio Volume Meter), zarządcę (PulseAudio
   Manager) i ustawienia (PulseAudio Preferences).

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%configure \
	--disable-lynx
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/padevchooser
%{_datadir}/padevchooser
%{_desktopdir}/padevchooser.desktop
