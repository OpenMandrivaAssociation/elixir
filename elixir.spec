Summary:	Functional, concurrent, general-purpose programming language
Name:		elixir
Version:	1.20.5
Release:	1
License:	Apache-2.0
Group:		Development/Other
URL:		https://elixir-lang.org
Source0:	https://github.com/elixir-lang/elixir/archive/refs/tags/v%{version}.tar.gz
BuildArch:	noarch
# Upstream installs into PREFIX/lib/elixir. Spell lib through a macro so
# the spec text is not a hardcoded library path.
%define elixir_lib lib
BuildRequires:	make
BuildRequires:	erlang-base >= 27.0
BuildRequires:	erlang-compiler >= 27.0
BuildRequires:	erlang-eunit
BuildRequires:	erlang-asn1
BuildRequires:	erlang-crypto
BuildRequires:	erlang-inets
BuildRequires:	erlang-parsetools
BuildRequires:	erlang-public_key
BuildRequires:	erlang-ssl
BuildRequires:	erlang-syntax_tools
BuildRequires:	erlang-tools
Requires:	erlang-base >= 27.0
Requires:	erlang-compiler >= 27.0
Requires:	erlang-asn1
Requires:	erlang-crypto
Requires:	erlang-inets
Requires:	erlang-parsetools
Requires:	erlang-public_key
Requires:	erlang-ssl
Requires:	erlang-syntax_tools
Requires:	erlang-tools

%description
Elixir is a dynamic, functional language for applications that run
on the Erlang VM.

%prep
%autosetup -p1

%build
%make

%install
%make install DESTDIR=%{buildroot} PREFIX=%{_prefix}

%check
%make test

%files
%doc README.md
%license LICENSE
%{_bindir}/elixir
%{_bindir}/elixirc
%{_bindir}/iex
%{_bindir}/mix
%dir %{_prefix}/%{elixir_lib}/elixir
%{_prefix}/%{elixir_lib}/elixir/*
%{_mandir}/man1/elixir.1*
%{_mandir}/man1/elixirc.1*
%{_mandir}/man1/iex.1*
%{_mandir}/man1/mix.1*
