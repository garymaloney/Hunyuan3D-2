# Get the total height of the scrollback buffer
$TotalLines = [Console]::BufferHeight

# Get the height of the visible console window
$VisibleLines = [Console]::WindowHeight

# Calculate the number of full screens (using [Math]::Ceiling to round up)
$TotalScreens = [Math]::Ceiling($TotalLines / $VisibleLines)

Write-Host "Total screens to capture: $TotalScreens"
