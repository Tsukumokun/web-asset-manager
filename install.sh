echo "\033[0;34mSearching for java...\033[0m"
if type -p java; then
    _java=java
elif [[ -n "$JAVA_HOME" ]] && [[ -x "$JAVA_HOME/bin/java" ]];  then    
    _java="$JAVA_HOME/bin/java"
else
    echo "\033[0;31mNot Found: java - install java >v1.5 and retry.\033[0m"
fi

if [[ "$_java" ]]; then
    version=$("$_java" -version 2>&1 | awk -F '"' '/version/ {print $2}')
    echo version "$version"
    if [[ "$version" >= "1.5" ]]; then
        echo "Found it!"
    else         
        echo "\033[0;31mNot Found: java correct version - install java >v1.5 and retry.\033[0m"
    fi
fi

echo "\033[0;34mCloning WAM (Web-Asset-Manager)...\033[0m"
hash git >/dev/null && /usr/bin/env git clone https://github.com/Tsukumokun/web-asset-manager.git ~/.wam || {
  echo "\033[0;31mNot Found: git - install git and retry.\033[0m"
  exit
}