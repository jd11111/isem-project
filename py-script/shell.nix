{ pkgs ? import <nixpkgs> {} }:
(pkgs.buildFHSEnv {
  name = "simple-python-env";
  targetPkgs = pkgs: (with pkgs; [
    python3
    zlib
  ]);
  runScript ="bash";
}).env

