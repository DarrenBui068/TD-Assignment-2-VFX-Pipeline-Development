Save

 FUNCTION saveFile(assetName, assetType)
    	# Generate file name
   	versionNumber = getNextVersion(assetName)
    	fileName = assetName + versionNumber

	# Save the file to the WIP folder
    	save file to WIP folder with fileName

    	print "File saved to “ [path]
END FUNCTION

Publish

FUNCTION publishFile(assetName, assetType)
# Get the current WIP version
    	versionNumber = getCurrentVersion(assetName)

    	# Copy the WIP file to the publishing source folder
    	source_file = os.path.join(wip_directory, asset_type, f"{asset_name}_v{version_number:01}.ma")
    	publish_source_folder = os.path.join(publish_directory, asset_type)
    	publish_source_file = os.path.join(publish_source_folder, f"{asset_name}_v{version_number:01}.ma")
    	shutil.copy2(source_file, publish_source_file)

    	Print "File published to source folder: {publish_source_file}"
END FUNCTION

Main

assetName = "myAsset"   # Replace with the actual asset name
assetType = assetTypes.get(assetName, "")

IF assetType is not empty 
        	saveFile(assetName, assetType)
       	publishFile(assetName, assetType)
ELSE
       	print "Invalid asset name."
END IF
