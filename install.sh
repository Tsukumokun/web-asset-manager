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
fi

if [[ "$_java" ]]; then
    version=$("$_java" -version 2>&1 | awk -F '"' '/version/ {print $2}')
    echo version "$version"
    if [[ "$version" >= "1.5" ]]; then
        echo "Found it!"
    else         
        echo "${RED}Not Found: java correct version - install java >v1.5 and retry.${NORMAL}"
    fi
fi

echo "${BLUE}Cloning WAM (Web-Asset-Manager)...${NORMAL}"
hash git >/dev/null && /usr/bin/env git clone https://github.com/Tsukumokun/web-asset-manager.git /tmp/wam || {
  echo "${RED}Not Found: git - install git and retry.${NORMAL}"
  exit
}

mkdir -p $PREFIX/bin/
install -o root -g root -m 755 /tmp/wam/bin $PREFIX/bin/wam
mkdir -p $PREFIX/lib/wam/
install -o root -g root -m 311 /tmp/wam/lib/* $PREFIX/lib/wam

rm -rf /tmp/wam/

echo "${GREEN}  (\`\ .-') /\`  ('-.     _   .-')    ${NORMAL}"
echo "${GREEN}   \`.( OO ),' ( OO ).-.( '.( OO )_  ${NORMAL}"
echo "${GREEN},--./  .--.   / . --. / ,--.   ,--.)${NORMAL}"
echo "${GREEN}|      |  |   | \-.  \  |   \`.'   | ${NORMAL}"
echo "${GREEN}|  |   |  |,.-'-'  |  | |         | ${NORMAL}"
echo "${GREEN}|  |.'.|  |_)\| |_.'  | |  |'.'|  | ${NORMAL}"
echo "${GREEN}|         |   |  .-.  | |  |   |  | ${NORMAL}"
echo "${GREEN}|   ,'.   |   |  | |  | |  |   |  | ${NORMAL}"
echo "${GREEN}'--'   '--'   `--' `--' `--'   `--' ${NORMAL}"