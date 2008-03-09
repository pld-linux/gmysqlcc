Summary:	MySQL client for GNOME
Summary(pl.UTF-8):	Graficzny klient baz MySQL dla środowiska GNOME
Name:		gmysqlcc
Version:	0.3.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://projects.thepozer.net/versions/download/19?attachment_id=25
# Source0-md5:	cdfd5f1e4da8bbde45a52ba6a02f8313
URL:		http://projects.thepozer.net/projects/show/gmysqlcc
BuildRequires:	gtk+2-devel
BuildRequires:	mysql-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Gmyclient is a powerful graphical MySQL client to use under GNOME.
Gmyclient is designed to be a simple, quick, and powerful way to
access your MySQL database.It provides you a powerful way to
create/edit all MySQL database objects most easy and simple way.

%description -l pl.UTF-8
Gmyclient jest graficznym klientem MySQL przeznaczonym dla środowiska
GNOME. Gmyclienta zaprojektowano tak, by zapewniał łatwy, szybki i w
pełni funkcjonalny dostęp do baz danych MySQL. Umożliwia on tworzenie
i edycję baz MySQL.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
