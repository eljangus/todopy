{
  mkShell,
  python314,
  pyrefly,
}:
mkShell {
  packages = [
    python314
    pyrefly
  ];
}
