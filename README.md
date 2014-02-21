Web Asset Manager
==========

How to install
----------
With `curl`<br/>
    > curl -L https://raw.github.com/install.sh | sh
With `wget`<br/>
    > wget --no-check-certificate https://raw.github.com/install.sh -O - | sh

How to use
----------
JS:<br/>
Add `require("file.js")` to any javascript file.<br/>
`file.js` will then upon compilation be inserted at exactly that spot.<br/>
CSS:<br/>
As usual add `@import "file.css";` to any css file.<br/>
`file.css` will then upon compilation be inserted at exactly that spot.<br/>

How to compile
----------
js-compile main.js<br/>
css-compile main.css

Optional flags
----------
-m : only minify files (files will be placed in file.min.js)<br/>
-M : don't minify output file<br/>
-b : specify a different location for compiled code (default is current directory)


Author
--- 
Christopher Kelley<br/>
[tsukumokun@icloud.com](mailto:tsukumokun@icloud.com)

Notes from the Authors
---


License
----------
See LICENCE file in project root.