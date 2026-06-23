$ProjectRoot = Split-Path -Parent $PSScriptRoot
$VenvPath = Join-Path $ProjectRoot ".venv"
$ActivatePath = Join-Path $VenvPath "Scripts\Activate.ps1"

if (-Not (Test-Path $VenvPath)) {
    Write-Host ".venv not found, creating virtual environment..."
    python -m venv $VenvPath
}

if (-Not (Test-Path $ActivatePath)) {
    Write-Host "Activate.ps1 not found. Virtual environment may be broken."
    exit 1
}

Write-Host "Activating virtual environment..."
& $ActivatePath

Write-Host "Virtual environment activated."
python --version