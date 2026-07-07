```powershell
# 1. Define the default Wireshark installation path
$wiresharkPath = "C:\Program Files\Wireshark"

# 2. Verify that tshark.exe actually exists there
if (Test-Path "$wiresharkPath\tshark.exe") {
    Write-Host "✅ tshark.exe found at: $wiresharkPath" -ForegroundColor Green
    
    # 3. Get your current User PATH variable
    $currentPath = [Environment]::GetEnvironmentVariable("Path", "User")
    
    # 4. Check if the Wireshark path is already in your PATH
    if ($currentPath -split ';' -contains $wiresharkPath) {
        Write-Host "ℹ️ Wireshark is already in your PATH. You are good to go!" -ForegroundColor Yellow
    } else {
        # 5. Append the Wireshark path to your existing PATH
        $newPath = "$currentPath;$wiresharkPath"
        
        # 6. Save the new PATH permanently to your User environment
        [Environment]::SetEnvironmentVariable("Path", $newPath, "User")
        
        # 7. Update the current PowerShell session so it works immediately
        $env:PATH = "$env:PATH;$wiresharkPath"
        
        Write-Host "🚀 Successfully added Wireshark to your PATH!" -ForegroundColor Cyan
    }
} else {
    Write-Host "❌ Could not find tshark.exe in $wiresharkPath." -ForegroundColor Red
    Write-Host "Please make sure Wireshark is installed, or update the `$wiresharkPath variable if you installed it elsewhere." -ForegroundColor Red
}
```