# Default configuration for FastApi
$env:DATABASE_HOST = "localhost";
$env:DATABASE_USER = "root";
$env:DATABASE_PASSWORD = "";
$env:DATABASE_PORT = "3306";
$env:DATABASE_NAME = "ctf-cm";

# Starting process's
$mysqlProcess = Start-Process -FilePath "mysql_start.bat" -PassThru -NoNewWindow
$apiProcess = Start-Process -FilePath "uvicorn.exe" -ArgumentList "main:app", "--host", "0.0.0.0", "--port", "9999", "--reload" -WorkingDirectory "$PSScriptRoot/api" -PassThru -NoNewWindow
$appProcess = Start-Process -FilePath "npm.cmd" -ArgumentList "run", "dev" -WorkingDirectory "$PSScriptRoot/frontend" -PassThru -NoNewWindow
$allProcess = Get-Process $mysqlProcess.Id, $apiProcess.Id, $appProcess.Id

# Life loop
while ($true)
{
    # If one process exit, exit from loop
    $finishedProcess = $allProcess | Where-Object {$_.HasExited}
    if ($finishedProcess.Count -gt 0)
    {
        break
    }

    # Get messeges from process's
    try{
        $mysqlOutput = $mysqlProcess.StandardOutput.ReadAsync()
        $apiOutput = $apiProcess.StandardOutput.ReadAsync()
        $appOutput = $appProcess.StandardOutput.ReadAsync()

        Write-Output $mysqlOutput
        Write-Output $apiOutput
        Write-Output $appOutput
    } catch
    {
        # pass
    }

}