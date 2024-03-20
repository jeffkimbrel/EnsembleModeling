import datetime
import logging
import uuid

import rpy2
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr, data

from installed_clients.WorkspaceClient import Workspace as Workspace
from installed_clients.KBaseReportClient import KBaseReport

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


        ensembletools = importr('ensembletools', lib_loc="/usr/local/lib/R/site-library")
        logging.info(ensembletools.__version__)


        return({})

        