import requests
import json

class Helper:
    def __init__(self, url, name, cam_passport):
         self.url = url
         self.name = name
         self.cam_passport = cam_passport

    def doGet(self, what):
        headers = {'Authorization': "CAMPassport " + self.cam_passport}
        response = requests.get(self.url+what, headers=headers)
        if response.ok:
            return response.content
        print "doGet FAILED"

    def getCubeNames(self):
        cubeNames = []
        object = self.doGet("/api/v1/Cubes")
        json_object = json.loads(object)
        nCubes = len(json_object.get("value"))
        for i in range(nCubes):
            cubeNames.append(json_object.get("value")[i].get("Name"))
        return cubeNames
