Summary:	Functional, concurrent, general-purpose programming language
Name:		elixir
Version:	1.20.5
Release:	1
License:	Apache-2.0
Group:		Development/Other
URL:		https://elixir-lang.org
Source0:	https://github.com/elixir-lang/elixir/archive/refs/tags/v%{version}.tar.gz
# Keep the trailing partial line from System.cmd when :lines is set.
Patch0:		elixir-1.20.5-port-line-flush.patch
BuildArch:	noarch
# Upstream installs into PREFIX/lib/elixir. Spell lib through a macro so
# the spec text is not a hardcoded library path.
%define elixir_lib lib
BuildRequires:	make
# Mix test helper runs git to build local fixtures.
BuildRequires:	git
BuildRequires:	erlang-base >= 27.0
BuildRequires:	erlang-compiler >= 27.0
BuildRequires:	erlang-eunit
# Test suite only. RecordTest reads xmerl/include/xmerl.hrl.
# DialyzerTest calls :dialyzer.run/1.
# Mix profile and release tests load the runtime_tools application.
BuildRequires:	erlang-xmerl
BuildRequires:	erlang-dialyzer
BuildRequires:	erlang-runtime_tools
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
# File.cd!/2 changes the working directory for the whole VM. The mix
# suite calls it from many tests at once. On aarch64 that race deletes
# the working directory and the rest of the suite fails. noarch, so this
# cannot be an arch conditional in the spec.
case $(uname -m) in
aarch64)
	sed -i 's/ExUnit.start(ex_unit_opts)/ExUnit.start(Keyword.put(ex_unit_opts, :max_cases, 1))/' lib/mix/test/test_helper.exs
	;;
esac
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
