# --- Script to Remove BOM from all metadata.json files ---

# Find all metadata.json files inside the 'pieces' directory
$files = Get-ChildItem -Path ".\pieces" -Recurse -Filter "metadata.json"

# Create the BOM-less encoding object (we proved this works)
$utf8WithoutBom = New-Object System.Text.UTF8Encoding $false

# Loop through each file found
foreach ($file in $files) {
    Write-Host "Processing: $($file.FullName)"

    # Read the entire content of the file. This automatically strips the BOM.
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8

    # Write the content back to the same file using BOM-less UTF-8 encoding
    [System.IO.File]::WriteAllText($file.FullName, $content, $utf8WithoutBom)
    
    Write-Host "✅ BOM removed successfully."
}

Write-Host "All metadata.json files have been cleaned."