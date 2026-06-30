param(
  [Parameter(ValueFromRemainingArguments = $true)]
  [string[]]$Args
)

$ErrorActionPreference = "Stop"
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$publisher = Join-Path $scriptDir "publish_docx.py"

function Test-Command($name) {
  $null -ne (Get-Command $name -ErrorAction SilentlyContinue)
}

if (Test-Command "python") {
  & python $publisher @Args
  exit $LASTEXITCODE
}

if (Test-Command "py") {
  & py -3 $publisher @Args
  exit $LASTEXITCODE
}

$bundled = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
if (Test-Path $bundled) {
  & $bundled $publisher @Args
  exit $LASTEXITCODE
}

Write-Error "No Python runtime found. Install Python 3, or run this from Codex where bundled Python is available."
exit 1
