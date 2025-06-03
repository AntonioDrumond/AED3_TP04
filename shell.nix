{
  pkgs ? import <nixpkgs> { },
}:
pkgs.mkShell {
  buildInputs = with pkgs; [
    python312
    python312Packages.pyqt6
    python312Packages.anyqt
    python312Packages.pyqtdarktheme
    python312Packages.pandas
    python312Packages.numpy
  ];

  shellHook = ''
    alias py="python"
    echo ""
    echo "Packages loaded: Python, anyqt, pyqtdarktheme, pandas and numpy"
  '';

}
