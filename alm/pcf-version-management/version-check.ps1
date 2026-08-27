param(
    [Parameter(Mandatory = $true)]
    [string]$ManifestPath,

    [Parameter(Mandatory = $true)]
    [string]$ExpectedVersion
)

[xml]$manifest = Get-Content -Path $ManifestPath
$control = $manifest.manifest.control

if (-not $control) {
    throw "Control node was not found in the PCF manifest."
}

$actual = [string]$control.version
Write-Host "Manifest version: $actual"
Write-Host "Expected version: $ExpectedVersion"

if ($actual -ne $ExpectedVersion) {
    throw "PCF manifest version does not match the release version."
}

$properties = @($control.property | ForEach-Object { $_.name })
Write-Host "Manifest properties: $($properties -join ', ')"
Write-Host "Version contract check passed."
