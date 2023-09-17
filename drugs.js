class Database {
    constructor() {
        this.original_database = new Object();
        this.property_dicts = new Map();
        this.index_properties = new Array();
    }
    update_database(json) {
        // clear previous data
        for (property in update_database.index_properties) {
            update_database.property_dicts.delete(property);
        }
        this.index_properties = new Array();
        // parse new json
        this.original_database = json;
        // set new pointers to original_database elements in property_dicts
        for (const drugInfo in this.original_database) {
            for (const [property, propertyData] in drugInfo) {
                if (!this.index_properties.includes(property)) {
                    // add new unseen property to all in database, should not occur in the current database except on the first drugInfo
                    for (const drugInfo in this.original_database) {
                        drugInfo[property] = null;
                    }
                    this.index_properties.push(property);
                    this.property_dicts.set(property, new Map());
                }
                let property_dict = this.property_dicts.get(property)
                if (!(property_dict.has(propertyData))) {
                    property_dict.set(propertyData, new Array());
                }
                let property_dict_entry = property_dict.get(propertyData);
                property_dict_entry.push(drugInfo);
            }
        }
    }
    get_drug_info_by_property(property, propertyData) {
        // example: get_drug_info_by_property("ActiveIngredient", "ACETAMINOPHEN")
        // example: get_drug_info_by_property("DrugName", "TYLENOL")
        let property_dict = this.property_dicts.get(property)
        return property_dict.get(propertyData);
    }
}

/*
var req = new XMLHttpRequest();
req.onload = function(){
    process_webgl_data(this.responseText);
};
req.open('GET', './output-onlinetsvtools.json');
req.send();
*/

fetch('./output-onlinetsvtools.json')
    .then((response) => response.json())
    .then((json) => update_database(json));