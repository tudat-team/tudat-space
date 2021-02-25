#!/bin/bash -ue

function echo_red
{
  echo -e '\033[3;31m'"$@"'\033[0m'
}

if [ ! -z "$(which conda)" ]
then
  echo_red "conda deactivate tudat-space"
  conda deactivate tudat-space || echo_red "Ignoring previous error: the tudat-space environment is not active"
  echo_red "conda remove tudat-space"
  conda remove --yes -n tudat-space --all
  echo_red "conda remove channel tudat-team"
  conda config --remove channels tudat-team || echo_red "Ignoring previous error: the tudat-team channel has already been removed"
else
  echo_red "conda has already been uninstalled"
fi
echo_red "brew remove miniconda"
brew remove miniconda