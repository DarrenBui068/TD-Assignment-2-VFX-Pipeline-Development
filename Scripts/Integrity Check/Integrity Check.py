Deletes unknown/unused nodes 

FUNCTION deleteBlankNodes()
	FOR each node in scene
		IF node is blank
			delete node
		END IF
	END FOR
END FUNCTION
	

Checks naming convention of the asset

FUNCTION checkName(object)
IF object name good
RETURN true
   	ELSE
		print “Object name is invalid”
        		RETURN false
   	END IF
END FUNCTION


Round very small decimals

FUNCTION roundAttributes(object)
   	FOR each attribute in object
        		IF attribute is floating point and has 5 dp
            		round to 4 dp
        		END IF
    	END FOR
END FUNCTION


Set position and pivot to origin

FUNCTION centerObject(object)
	set position to 0,0,0
	set pivot to 0,0,0
END FUNCTION




Check for invalid set references

FUNCTION checkReferences(set)
	FOR each setPiece
		IF invalid reference
			print “Reference error in “ [setPiece]
	RETURN true
END FUNCTION


Validate asset with the above functions

FUNCTION asset()
get asset from scene
    	IF checkName(asset)
        		print "This asset is ok"
    	END IF

	centerObject(asset)
	roundAttributes(asset)
	deleteBlankNodes()
END FUNCTION


Validate set with the above functions

FUNCTION set()
	get set from scene
    	IF checkName(set) & checkReferences(set)
        		print "This set is ok"
    	END IF

	centerObject(set)
	roundAttributes(set)
	deleteBlankNodes()
END FUNCTION


Check camera aperture

FUNCTION checkAperture(camera)
	IF camera aperture is 16:9
		RETURN true
	ELSE
		print “Camera aperture is invalid”
		RETURN false
	END IF
END FUNCTION



Check camera focal length

FUNCTION checkFocalLength(camera)
	focalLengths = {...}
	IF camera focalLength in focalLenghts
		RETURN true
	ELSE
print “Camera focal length is invalid”
		RETURN false
	END IF
END FUNCTION



Check camera f-stop

FUNCTION checkFStop(camera)
	fStops = {...}
	IF camera fStop in fStops
		RETURN true
	ELSE
		print “Camera f-stop is invalid”
		RETURN false
	END IF
END FUNCTION

Check camera with the functions above

FUNCTION camera()
	get camera from scene
	IF checkAperture(camera) & checkFocalLength(camera) & checkFStop(camera)
		print “This camera is ok”
	END IF
END FUNCTION
