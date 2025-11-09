# -------------------------------------------------
# Validate Domino Pieces repository
# -------------------------------------------------
Write-Host "Validating Domino Pieces repository..."

# 1. Check if .github folder exists (should NOT be there after migration)
if (Test-Path ".github") {
    Write-Host "ERROR: .github folder should not exist for Pieces workflow."
    exit 1
}

# 2. Check if .domino folder exists (SHOULD exist now)
if (!(Test-Path ".domino")) {
    Write-Host "ERROR: .domino folder not found!"
    exit 1
}

# 3. Check pieces/ folder exists (SHOULD exist)
if (!(Test-Path "pieces")) {
    Write-Host "ERROR: pieces folder not found!"
    exit 1
} else {
    Write-Host "OK: .domino folder exists."
}

# 4. Check for each Piece folder
$pieceFolders = Get-ChildItem -Path "pieces" -Directory
foreach ($folder in $pieceFolders) {
    $pieceName = $folder.Name
    $metadataPath = "pieces\$($pieceName)\metadata.json"
    if (Test-Path $metadataPath) {
        Write-Host "OK: $pieceName/metadata.json exists."
    } else {
        Write-Host "WARNING: $pieceName/metadata.json missing."
    }
}

# 5. Check dependencies folder exists (SHOULD exist)
if (!(Test-Path "dependencies")) {
    Write-Host "ERROR: dependencies folder not found!"
    exit 1
} else {
    Write-Host "OK: dependencies folder exists."
}

# 6. Summary
Write-Host "Validation complete. Ready to proceed to Domino import."
