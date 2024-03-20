import datetime
import logging
import uuid
import os

import rpy2
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr, data

from installed_clients.WorkspaceClient import Workspace as Workspace
from installed_clients.KBaseReportClient import KBaseReport

import EnsembleModeling.utils.r_functions as r

class AnalyzeEnsembleModelUtil:

    def __init__(self, config):
        self.config = config
        self.timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        self.callback_url = config['SDK_CALLBACK_URL']
        self.scratch = config['scratch']
        self.kbr = KBaseReport(self.callback_url)
        self.ws_client = Workspace(config["workspace-url"])


    def run(self, ctx, params):
        logging.info("*****Running run method of AnalyzeEnsembleModelUtil")


        et = importr('ensembletools', lib_loc="/usr/local/lib/R/site-library")
        logging.info(et.__version__)

        # get ensemble json path
        if 'debug' in params and params['debug'] is True:
            json_path = os.path.join(
                '/kb/module/test/test_data', params['json_path'])
        else:
            # needs to be updated to take API data
            json_path = os.path.join("/staging/", params['json_path'])

        logging.info(json_path)

        # make ensemble object
        logging.info("Making ensemble object")
        ensemble = r.ensemble(json_path, scale=params['rescale'])
        logging.info(ensemble)

        # ordinate solutions
        logging.info("Ordinating solutions")
        ensemble = r.ordinate_solutions(ensemble,
                                         distance = params['distance_metric'],
                                         quiet = False)
        
        logging.info(ensemble)
        #logging.info(et.stress(ensemble))

        # cluster solutions
        logging.info("Clustering solutions")
        ensemble = r.cluster_solutions(ensemble, k = params['clusters'])
        logging.info(et.sil_widths(ensemble))
        logging.info(et.medioids(ensemble))

        # plot clusters
        r.plot_clusters(ensemble, file_path=os.path.join(self.scratch, "clusters.png"))

        return({})

        