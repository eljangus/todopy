{
  mkShell,
  python314,
  python314Packages,
  pyrefly,
}:
mkShell {
  packages = [
    python314
    python314Packages.textual
    pyrefly
  ];
}
