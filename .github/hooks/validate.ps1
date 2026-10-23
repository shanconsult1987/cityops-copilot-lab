$inputData = [Console]::In.ReadToEnd()

Write-Host "CityOps Hook: validating agent tool request..."

# Simple demonstration rule:
# Block attempts to modify protected production configuration.

if ($inputData -match "production-config") {
    Write-Host "BLOCKED: production-config is protected."
    exit 1
}

Write-Host "ALLOWED: tool request passed validation."
exit 0
