#!/bin/bash

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