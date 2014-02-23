#
# WAM - a web asset manager
# Copyright (C) 2014 Christopher Kelley   <tsukumokun(at)icloud.com>
# 
# This work is licensed under the 
# Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 
# International License. To view a copy of this license, visit 
# http://creativecommons.org/licenses/by-nc-nd/4.0/deed.en_US.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
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

sudo echo -n

echo "${BLUE}Uninstalling executable...${NORMAL}"
sudo rm -f $PREFIX/bin/wam
echo "${BLUE}Unstalling support files...${NORMAL}"
sudo rm -rf $PREFIX/lib/wam/


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