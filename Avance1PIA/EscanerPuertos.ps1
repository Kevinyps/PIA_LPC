# Parametro para la direccion ip a escanear
#
[string]$direccion_ip = 127.0.0.1
#
# Definimos un array con puertos a escanear
# Establecemos una variable para Waittime
#
$portstoscan = @(1..500)
$waittime = 100
#
# Generamos bucle foreach para evaluar cada puerto
#
foreach ($p in $portstoscan)
{
    $TpcObject = New-Object System.Net.Sockets.TcpClient
        try{
         $resultado = $TpcObject.ConnectAsync($direccion_ip,$p).Wait($waittime)
         }
        catch{
        }
        if ($resultado -eq "True")
        {
            Write-Host "Puerto abierto:" + $p
        }
}