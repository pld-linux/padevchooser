Summary:	PulseAudio Device Chooser
Summary(pl):	PulseAudio Device Chooser - narzêdzie do wyboru urz±dzeñ
Name:		padevchooser
Version:	0.9.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://0pointer.de/lennart/projects/padevchooser/%{name}-%{version}.tar.gz
# Source0-md5:	434292c135b9a2e95f386b239fb7b465
Patch0:		%{name}-desktop.patch
URL:		http://0pointer.de/lennart/projects/padevchooser/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	libglade-devel >= 2.0
BuildRequires:	libnotify-devel
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 0.9.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PulseAudio Device Chooser (padevchooser) is a simple GTK+ tool which
registers an icon in the tray area and allows quick access to some
features of the PulseAudio sound server. Specifically it can do for
you:
 - Notify about new sink/sources becoming available on the LAN
 - Quickly change the default PulseAudio sink/source/server assigned
   to the current X11 display, selecting devices available on the LAN
 - Start the auxiliary tools: PulseAudio Volume Control, PulseAudio
   Volume Meter, PulseAudio Manager

%description -l pl
PulseAudio Device Chooser (padevchooser) to proste narzêdzie GTK+
rejestruj±ce ikonê na pasku i pozwalaj±ce na szybki dostêp do
niektórych mo¿liwo¶ci serwera d¼wiêku PulseAudio. W szczególno¶ci
potrafi:
 - powiadomiæ o nowych ¼ród³ach dostêpnych w sieci lokalnej
 - szybko zmieniæ domy¶lne ¼ród³o/serwer PulseAudio przypisane do
   ekranu X11 wybieraj±c urz±dzenia dostêpne w sieci lokalnej
 - uruchomiæ dodatkowe narzêdzia: mikser (PulseAudio Volume Control),
   miernik g³o¶no¶ci (PulseAudio Volume Meter) i zarz±dcê (PulseAudio
   Manager).

%prep
%setup -q
%patch0 -p1

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
