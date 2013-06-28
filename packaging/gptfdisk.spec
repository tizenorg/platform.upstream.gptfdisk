Name:           gptfdisk
Version:        0.8.5
Release:        0
Summary:        GPT partitioning and MBR repair software
License:        GPL-2.0
Group:          Base/System
Url:            http://rodsbooks.com/gdisk

Source:         %name-%version.tar.xz
Source1001: 	gptfdisk.manifest
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel
BuildRequires:  xz
BuildRequires:  pkgconfig(icu-io)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(uuid)

%description
Partitioning software for GPT disks and to repair MBR disks. The
gdisk, cgdisk, and sgdisk utilities (in the gdisk package) are
GPT-enabled partitioning tools; the fixparts utility (in the fixparts
package) fixes some problems with MBR disks that can be created by
buggy partitioning software.

%package fixparts
Summary:        A tool for repairing certain types of damage to MBR disks
Group:          Applications/System

%description fixparts
A program that corrects errors that can creep into MBR-partitioned
disks. Removes stray GPT data, fixes mis-sized extended partitions,
and enables changing primary vs. logical partition status. Also
provides a few additional partition manipulation features.

%prep
%setup -q
cp %{SOURCE1001} .

%build
CFLAGS="%optflags" CXXFLAGS="%optflags" make %{?_smp_mflags}

%install
b="%buildroot";
mkdir -p "$b/%_sbindir" "$b/%_mandir/man8";
install -pm0755 fixparts {,c,s}gdisk "$b/%_sbindir/";
install -pm0644 *.8 "$b/%_mandir/man8/";

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license COPYING
%_sbindir/gdisk
%_sbindir/sgdisk
%_sbindir/cgdisk
%_mandir/man8/gdisk.8*
%_mandir/man8/cgdisk.8*
%_mandir/man8/sgdisk.8*

%files fixparts
%manifest %{name}.manifest
%defattr(-,root,root)
%license COPYING 
%_sbindir/fixparts
%_mandir/man8/fixparts.8*

%changelog
