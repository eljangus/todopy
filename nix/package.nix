{
  stdenvNoCC,
  lib,
  pkgs,
  python314,
  makeWrapper,
}:
stdenvNoCC.mkDerivation {
  pname = "todopy";
  version = "0.1.0";

  nativeBuildInputs = [makeWrapper];
  buildInput = [pkgs.python314Packages.textual];
  dontUnpack = true;
  dontBuild = true;

  installPhase = ''
    runHook preInstall

    install -Dm644 ${../src/todo.py} $out/share/todopy/todo.py

    makeWrapper ${python314}/bin/python3 $out/bin/todo \
      --add-flags $out/share/todopy/todo.py

    runHook postInstall
  '';

  meta = with lib; {
    mainProgram = "todo";
    description = "A python TO-DO list";
    homepage = "https://github.com/eljangus/todopy";
    license = licenses.mit;
    platforms = platforms.all;
  };
}
