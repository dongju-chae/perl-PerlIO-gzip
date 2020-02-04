Name:       perl-PerlIO-gzip
Version:    0.20
Release:    1
Summary:    A layer for the PerlIO system to transparently gzip/gunzip files.
Group:      Development/Libraries
License:    GPL-2.0+ or Artistic
URL:        http://search.cpan.org/dist/PerlIO-gzip
Source0:    %{name}-%{version}.tar.gz
Source1001: perl-PerlIO-gzip.manifest
BuildRequires:  perl
BuildRequires:  zlib-devel

%description
This module provides a PerlIO layer that manipulates files in the format used by the gzip program. Compression and Decompression are implemented, but not together. If you attempt to open a file for reading and writing the open will fail.

%prep
%setup -q -n perl-PerlIO-gzip-%{version}
cp %{SOURCE1001} .

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
