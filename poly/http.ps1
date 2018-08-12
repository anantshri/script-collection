#!/bin/bash

# Credits
# 1. https://stackoverflow.com/a/39422067 : For eval idea
# 2. https://gist.github.com/obscuresec/71df69d828e6e05986e9 : Basic powershell webserver code
# 3. https://gist.github.com/theit8514/58a31895ae901206f6957a382f61618b : mimetype collection and indexpage addition and 404
# 

# TODO's
# 1. take commandline argument in powershell also
# 1. exit in powershell gracefully at ctrl + c or ctrl + break (c not working break not tested)
# 1. find way to remove extension to remove ambiguity that its only ps1 script

#bash PORT=${1:-8000}
#bash shift
#bash if which python &> /dev/null; then
#bash 	PY=`python -c 'import platform; print(platform.python_version())' | cut -f1 -d"."`
#bash 	if [ $PY == 2 ]
#bash 	then
#bash 		python -m SimpleHTTPServer $PORT $*
#bash 	else
#bash 		python -m http.server $PORT $*
#bash 	fi
#bash elif which ruby &> /dev/null; then
#bash 	ruby -run -ehttpd . -p$PORT $*
#bash elif which php &> /dev/null; then
#bash 	php -S 127.0.0.1:$PORT $*
#bash else
#bash 	echo "Python/Ruby/PHP not found"
#bash fi
function RUNSERVER {
    eval "$(grep '^#bash' $0 | sed -e 's/^#bash //')"
} 
"RUNSERVER"
"exit"


function Get-MimeType() {
    param($extension);
    switch($extension) {
        ".gif" {"image/gif"}
        ".png" {"image/png"}
        {$_ -in ".jpg",".jpeg"} {"image/jpeg"}
        {$_ -in ".htm",".html"} {"text/html"}
        ".js" {"application/x-javascript"}
        ".css" {"text/css"}
        ".pdf" {"application/pdf"}
        ".zip" {"application/zip"}
        ".txt" {"text/plain"}
        default {"application/octet-stream"}
    }
}

Add-Type -AssemblyName "System.Web";
$Hso=New-Object Net.HttpListener;
$Hso.Prefixes.Add("http://localhost:8000/");
$Hso.Start();
While ($Hso.IsListening){
    $HC=$Hso.GetContext();
    $HRes=$HC.Response;
    $path = Join-Path (pwd) $HC.Request.RawUrl;
    if ([System.IO.Directory]::Exists($path)) {
        $path = $path + "index.html";
    }
    Write-Host $path;
    if ([System.IO.File]::Exists($path)) {
        $Stream=[System.IO.File]::OpenRead(($path));
        $HRes.ContentLength64=$Stream.Length;
        $ext = [System.IO.Path]::GetExtension($path);
        $HRes.ContentType=Get-MimeType $ext;
        $Stream.CopyTo($HRes.OutputStream);
        $Stream.Close();
    } else {
        $HRes.StatusCode = 404;
    }
    $HRes.Close()
};
$Hso.Stop();