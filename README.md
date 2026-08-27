# TODOpy

## TODOpy is a simple TO-DO list CLI tool fully written in Python!

It allows you to create, delete, append to, remove from and initialise TO-DO
lists stored directly in `~/.config/todopy/`.

## Installation

TODOpy ships as a [Nix flake](https://nixos.wiki/wiki/Flakes). The flake exposes:

| Output | Description |
| --- | --- |
| `packages.<system>.todopy` (also `default`) | The `todo` executable |
| `overlays.default` | Adds `todopy` to `pkgs` |
| `devShells.<system>.default` | Dev shell with Python 3.14 and `pyrefly` |

Supported systems: `x86_64-linux`, `aarch64-linux`, `aarch64-darwin`.

### Try it without installing

```sh
nix run github:eljangus/todopy
```

### Imperative install (any system with Nix + flakes)

```sh
nix profile install github:eljangus/todopy
todo
```

To update later:

```sh
nix profile upgrade todopy
```

### NixOS (flakes)

Add TODOpy as an input in your system `flake.nix`:

```nix
{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

    todopy.url = "github:eljangus/todopy";
    # Optional: build against your own nixpkgs revision
    todopy.inputs.nixpkgs.follows = "nixpkgs";
  };

  outputs = { self, nixpkgs, todopy, ... } @ inputs: {
    nixosConfigurations.my-host = nixpkgs.lib.nixosSystem {
      system = "x86_64-linux";
      specialArgs = { inherit inputs; };
      modules = [ ./configuration.nix ];
    };
  };
}
```

TODOpy does not ship a NixOS module, so add the package in one of two ways.

**Option A — reference the package directly**

In `configuration.nix`:

```nix
{ pkgs, inputs, ... }:
{
  environment.systemPackages = [
    inputs.todopy.packages.${pkgs.system}.default
  ];
}
```

**Option B — use the overlay**

```nix
{ pkgs, inputs, ... }:
{
  nixpkgs.overlays = [ inputs.todopy.overlays.default ];

  environment.systemPackages = [ pkgs.todopy ];
}
```

Rebuild:

```sh
sudo nixos-rebuild switch --flake .#my-host
```

The `todo` command is now available system-wide.

### Home Manager (flakes)

```nix
{ pkgs, inputs, ... }:
{
  # Option A: direct reference
  home.packages = [ inputs.todopy.packages.${pkgs.system}.default ];

  # Option B: via overlay
  # nixpkgs.overlays = [ inputs.todopy.overlays.default ];
  # home.packages = [ pkgs.todopy ];
}
```

Then `home-manager switch --flake .#you`.

### Development shell

```sh
git clone https://github.com/eljangus/todopy
cd todopy
nix develop            # or `direnv allow` (an .envrc with `use flake` is included)
python3 src/todo.py
```

## Usage

Run `todo` and follow the interactive menu:

```
1. List todo lists
2. Read todo lists
3. Append to todo lists
4. Remove Lines from todo lists
5. Delete todo lists
6. Create todo lists
7. Exit
```

Lists are plain `.txt` files under `~/.config/todopy/`; the first line of each
file is treated as its header.

## License

MIT — see [LICENSE](./LICENSE).
