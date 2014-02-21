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

echo "${BLUE}Uninstalling executable...${NORMAL}"
rm -f -v $PREFIX/bin/wam
echo "${BLUE}Unstalling support files...${NORMAL}"
rm -rf -v $PREFIX/lib/wam


echo "${GREEN}You've removed...${NORMAL}"
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
echo "${GREEN}Hope it was helpful!${NORMAL}"