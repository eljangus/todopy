{
  description = "A python TO-DO list tool.";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = {
    self,
    nixpkgs,
    ...
  }: let
    inherit (nixpkgs) lib;

    systems = [
      "x86_64-linux"
      "aarch64-linux"
      "aarch64-darwin"
    ];

    forEachSystem = perSystem:
      lib.genAttrs systems (
        system:
          perSystem {
            pkgs = nixpkgs.legacyPackages.${system};
            inherit system;
          }
      );
  in {
    overlays.default = final: prev: {
      todopy = final.callPackage ./nix/package.nix {};
    };

    packages = forEachSystem (
      {pkgs, ...}: rec {
        todopy = pkgs.callPackage ./nix/package.nix {};
        default = todopy;
      }
    );

    devShells = forEachSystem (
      {pkgs, ...}: {
        default = pkgs.callPackage ./nix/shell.nix {};
      }
    );
  };
}
