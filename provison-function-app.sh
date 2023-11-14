#!/bin/bash
# Function app and storage account names must be unique.

# Variable block
location="westeurope"
resourceGroup="adr-viewer-rg"
tag="create-function-app-consumption"
storage="adrviewersa"
functionApp="adr-viewer"
skuStorage="Standard_LRS"
functionsVersion="4"

# Create a resource group
echo "Creating $resourceGroup in "$location"..."
az group create --name $resourceGroup --location "$location" --tags $tag

# Create an Azure storage account in the resource group.
echo "Creating $storage"
az storage account create --name $storage --location "$location" --resource-group $resourceGroup --sku $skuStorage

# Create a serverless function app in the resource group.
echo "Creating $functionApp"
az functionapp create --name $functionApp \
    --storage-account $storage \
    --consumption-plan-location "$location" \
    --resource-group $resourceGroup \
    --functions-version $functionsVersion \
    --runtime python \
    --runtime-version "3.10" \
    --os-type Linux
