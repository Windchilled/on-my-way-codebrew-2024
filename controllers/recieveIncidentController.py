from models.incident import *

def retrieveAllIncidents():
    allIncidents = getIncidents()
    return allIncidents

def retrieveIncident(_id):
    IncidentDetails = getIncidentDetails(_id)
    #print(IncidentDetails)
    return IncidentDetails

def resolveIncident(_id):
    isResolved = deleteIncident(_id)
    #print(IncidentDetails)
    return isResolved