#
# WAM - a web asset manager
# Copyright (C) 2014 Christopher Kelley   <tsukumokun(at)icloud.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http:// www.gnu.org/licenses/>
#

if [[ -z $PREFIX ]]; then PREFIX=/usr/local; fi

if [ -t 1 ]; then

    ncolors=$(tput colors)

    if test -n "$ncolors" && test $ncolors -ge 8; then
        BOLD="$(tput bold)"
        UNDERLINE="$(tput smul)"
        STANDOUT="$(tput smso)"
        NORMAL="$(tput sgr0)"
        BLACK="$(tput setaf 0)"
        RED="$(tput setaf 1)"
        GREEN="$(tput setaf 2)"
        YELLOW="$(tput setaf 3)"
        BLUE="$(tput setaf 4)"
        MAGENTA="$(tput setaf 5)"
        CYAN="$(tput setaf 6)"
        WHITE="$(tput setaf 7)"
    fi
fi

echo "${BLUE}Searching for java...${NORMAL}"
if type -p java; then
    _java=java
elif [[ -n "$JAVA_HOME" ]] && [[ -x "$JAVA_HOME/bin/java" ]];  then
    _java="$JAVA_HOME/bin/java"
else
    echo "${RED}Not Found: java - install java >v1.5 and retry.${NORMAL}"
    exit 1
fi

if [[ "$_java" ]]; then
    version=$("$_java" -version 2>&1 | awk -F '"' '/version/ {print $2}')
    echo version "$version"
    if [[ "$version" > "1.4" ]]; then
        echo "${NORMAL}"
    else         
        echo "${RED}Not Found: java correct version - install java >v1.5 and retry.${NORMAL}"
        exit 1
    fi
fi

echo "${BLUE}Cloning WAM (Web-Asset-Manager)...${NORMAL}"
hash git >/dev/null && /usr/bin/env git clone https://github.com/Tsukumokun/web-asset-manager.git /tmp/wam || {
  echo "${RED}Not Found: git - install git and retry.${NORMAL}"
  exit 1
}

echo "${BLUE}Installing executable...${NORMAL}"
mkdir -p $PREFIX/bin/
if [[ "$OSTYPE" == "darwin"* ]]; then
    install -o root -g wheel -m 755 /tmp/wam/bin/wam $PREFIX/bin/wam
else
    install -o root -g root -m 755 /tmp/wam/bin/wam $PREFIX/bin/wam
fi
echo "${BLUE}Installing support files...${NORMAL}"
mkdir -p $PREFIX/lib/wam/
if [[ "$OSTYPE" == "darwin"* ]]; then
    install -o root -g wheel -m 644 /tmp/wam/lib/* $PREFIX/lib/wam/
else
    install -o root -g root -m 644 /tmp/wam/lib/* $PREFIX/lib/wam/
fi
echo "${BLUE}Removing temporary files...${NORMAL}"
rm -rf /tmp/wam/

echo "${GREEN}You've got...${NORMAL}"
echo
echo "${YELLOW}  (\`\ .-') /\`  ('-.     _   .-')    ${NORMAL}"
echo "${YELLOW}   \`.( OO ),' ( OO ).-.( '.( OO )_  ${NORMAL}"
echo "${YELLOW},--./  .--.   / . --. / ,--.   ,--.)${NORMAL}"
echo "${YELLOW}|      |  |   | \-.  \  |   \`.'   | ${NORMAL}"
echo "${YELLOW}|  |   |  |,.-'-'  |  | |         | ${NORMAL}"
echo "${YELLOW}|  |.'.|  |_)\| |_.'  | |  |'.'|  | ${NORMAL}"
echo "${YELLOW}|         |   |  .-.  | |  |   |  | ${NORMAL}"
echo "${YELLOW}|   ,'.   |   |  | |  | |  |   |  | ${NORMAL}"
echo "${YELLOW}'--'   '--'   \`--' \`--' \`--'   \`--' ${NORMAL}"
echo 
echo "${GREEN}Enjoy!${NORMAL}"
