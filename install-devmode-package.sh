#/bin/bash
# https://packaging.python.org/guides/distributing-packages-using-setuptools/#working-in-development-mode
pushd .
cd ./src/
pip3 install -e ./
popd

echo; echo "Showing package info:"

pip3 show ConfiguroMoxa
