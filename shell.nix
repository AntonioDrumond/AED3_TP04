{
  pkgs ? import <nixpkgs> { },
}:
pkgs.mkShell {
  buildInputs = with pkgs; [
    python312
    python312Packages.tkinter
    python312Packages.pandas
    python312Packages.numpy
  ];

  shellHook = ''
    alias py="python"
    echo ""
    echo "Packages loaded: Python, tkinter, pandas and numpy"
  '';

}
