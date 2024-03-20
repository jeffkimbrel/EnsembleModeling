import rpy2.robjects as ro
from rpy2.robjects.packages import importr, data
from rpy2.robjects.lib.dplyr import DataFrame
from rpy2.robjects.lib import ggplot2
from rpy2.robjects import rl



# Helpers

## https://stackoverflow.com/questions/63901279/how-to-change-the-default-value-of-rs4-class-attribute-rpy2
get_r_at = ro.baseenv['@']
get_r_dollar = ro.baseenv['$']

# Functions

et = importr('ensembletools', lib_loc="/usr/local/lib/R/site-library")
# et = importr('ensembletools')

def ensemble(json_path,
             scale = True):
    
    if scale == 0:
        scale = False
    else:
        scale = True


    e = et.ensemble(json_path, 
                    scale = scale)
    return(e)

def ordinate_solutions(e, distance = "euclidean", quiet = True):
    ordination = et.ordinate_solutions(e,
                        distance = distance,
                        quiet = quiet)
    
    return(ordination)


def cluster_solutions(e, k = 0):
    clusters = et.cluster_solutions(e, k = k)

    return(clusters)


def plot_clusters(clusters, file_path):
    g = et.plot_clusters(clusters)
    ro.r.ggsave(filename = file_path,
                plot = g,
                width = 150,
                height = 150,
                unit = 'mm')
    

def get_solutions(e):
    df = DataFrame(get_r_at(e, 'solutions'))
    return(df)

def get_biomass_plot(e, file_path):
    g = et.plot_biomass(e)
    ro.r.ggsave(filename = file_path,
                plot = g,
                width = 100,
                height = 100,
                unit = 'mm')



# if __name__ == "__main__":

#     # import R package and print version
#     et = importr('ensembletools')
#     print(f"ensembletools R package v{et.__version__}")

#     json_path = "/Users/kimbrel1/Github/EnsembleModeling/test/test_data/SampleFBA.json"

#     e = ensemble(json_path, scale = True)

#     get_biomass_plot(e, file_path = "/Users/kimbrel1/Github/EnsembleModeling/test/test_data/biomass.png")

#     e.e = ordinate_solutions(e,
#                             quiet = True)

#     print(f"Stress is {et.stress(e.e)}")


#     e.e = cluster_solutions(e.e, k = 4)

#     # print(et.sil_widths(e.e))
#     # print(et.medioids(e.e))

#     plot_clusters(e.e, file_path="/Users/kimbrel1/Github/EnsembleModeling/test/test_data/clusters.png")


