/*
A KBase module: EnsembleModeling
*/

module EnsembleModeling {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef estimate_reaction_probabilities(mapping<string,UnspecifiedObject> params) 
        returns (ReportResults output) authentication required;
    funcdef build_ensemble_model(mapping<string,UnspecifiedObject> params) 
        returns (ReportResults output) authentication required;
    funcdef run_ensemble_FBA(mapping<string,UnspecifiedObject> params) 
        returns (ReportResults output) authentication required;
    funcdef gapfill_ensemble_model(mapping<string,UnspecifiedObject> params) 
        returns (ReportResults output) authentication required;
    funcdef analyze_ensemble_model(mapping<string,UnspecifiedObject> params) 
        returns (ReportResults output) authentication required;
    
    funcdef run_EnsembleModeling(mapping<string,UnspecifiedObject> params) 
        returns (ReportResults output) authentication required;


};
