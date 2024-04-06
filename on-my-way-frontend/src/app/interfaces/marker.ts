export interface Marker {
    type: string, //Feature,
    geometry : {
        type : string, //Point
        coordinates: number[] //num,num
    },
    properties : { //This needs to expand to allow for an array of properties 
        database_id : string, 
        severity : string, // Moderate, High, Severe, Extreme
        dateTime : string, //DW about DateTime formating dd/mm/yy HH/MM
        description: string
    }
}