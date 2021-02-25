#!/bin/bash

#NOTICE: bash's 'set -e' may trigger errors in sourcing .bash_profile

function echo_red
{
  echo -e '\033[3;31m'"$@"'\033[0m'
}

echo_red "brew install miniconda"
brew install miniconda
echo_red "conda init"
conda init "$(basename "${SHELL}")"
echo_red "source .bash_profile"
. $HOME/.bash_profile
echo_red "download environment.yaml"
[ -e ./environment.yaml ] || wget https://tudat-space.readthedocs.io/en/latest/_downloads/2ff196b0ef4830f53d754f6a3972d2e8/environment.yaml
echo_red "conda env create"
conda env create -f environment.yaml
echo_red "conda activate tudat-space"
conda activate tudat-space
echo_red "conda config --add channels tudat-team"
conda config --add channels tudat-team
echo_red "conda install tudat"
conda install --yes -c tudat-team tudat
echo_red "conda install tudatpy"
conda install --yes -c tudat-team tudatpy
for i in 1 2 3 10
do
  echo_red "download tutorial_$i.py"
  [ -e tutorial_$i.py ] || wget https://raw.githubusercontent.com/tudat-team/tudatpy/feature/po_updates/examples/tutorial_$i.py
  echo_red "test tutorial_$i.py"
  python3 tutorial_$i.py
done