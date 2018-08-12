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