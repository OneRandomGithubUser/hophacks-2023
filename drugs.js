class Database {
    constructor() {
        this.original_database = new Object();
        this.property_dicts = new Map();
        this.index_properties = new Array();
    }
    search_in_drug_info(drug_infos, property) {}
    update_database(json) {
        // clear previous data
        for (property in this.index_properties) {
            this.property_dicts.delete(property);
        }
        this.index_properties = new Array();
        // parse new json
        this.original_database = json;
        // set new pointers to original_database elements in property_dicts
        for (const drugInfo of this.original_database) {
            for (const [property, propertyData] of Object.entries(drugInfo)) {
                if (!this.index_properties.includes(property)) {
                    // add new unseen property to all in database, should not occur in the current database except on the first drugInfo
                    /*
                    for (const drugInfo in this.original_database) {
                        drugInfo[property] = null;
                    }
                    */
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
    get_drugs_by_property(property) {
        let property_dict = this.property_dicts.get(property)
        return property_dict;
    }
    get_drug_info_by_property(property, propertyData) {
        // example: get_drug_info_by_property("ActiveIngredient", "ACETAMINOPHEN")
        // example: get_drug_info_by_property("DrugName", "TYLENOL")
        let property_dict = this.get_drugs_by_property(property);
        let property_dict_entry = property_dict.get(propertyData);
        return property_dict_entry;
    }
    verify_data(drugNameOrActiveIngredient, form=null, strength=null) {
        try {
            possibleDrugInfos = new Array();
            possibleDrugInfos.push(get_drug_info_by_property("ActiveIngredient", drugNameOrActiveIngredient));
            possibleDrugInfos.push(get_drug_info_by_property("DrugName", drugNameOrActiveIngredient));
        } catch (e) {
            if (e instanceof ReferenceError) {
                return ReferenceError("drug name or active ingredient not found")
            } else {
                throw e;
            }
        };

    }
}

var database = null

/*
var req = new XMLHttpRequest();
req.onload = function(){
    process_webgl_data(this.responseText);
};
req.open('GET', './output-onlinetsvtools.json');
req.send();
*/
window.addEventListener('load', function() {
    fetch('./drugs.json')
        .then((response) => response.json())
        .then((json) => {database = new Database(); database.update_database(json);});
})