 <img src = "../../_images/SB_logo.eps" width = "300"> 
# tutor me
We are happy to share a few _use-cases_  that have been useful for our customers. We are even happier to hear your **needs** so we can make things run more smoothly for you. 

These scripts include [USER INPUTS] for particular _workflows_; however, they are _extensively commented_ so they can be easily adapted to other tasks.

## How could I access TCGA data on Amazon Web Services via _Datasets API_?
The [**access\_TCGA\_on\_AWS\_via\_DatasetsAPI.ipynb**] tutorial  strives to empower the public to access [TCGA](https://wiki.nci.nih.gov/display/TCGA/TCGA+Home) data via [Amazon Web Services](https://aws.amazon.com/). It uses the **Datasets API** SPARQL query, which allows easily formatting a query across phenomic fields. The difference relative to the _next_ tutorial is that here you need to use an additional API. However, this allows you to use **simple key-value** pairs to completely define the query.

## How could I access TCGA data on Amazon Web Services via _SPARQL_?
The [**access\_TCGA\_on\_AWS.ipynb**] tutorial  strives to empower the public to access [TCGA](https://wiki.nci.nih.gov/display/TCGA/TCGA+Home) data via [Amazon Web Services](https://aws.amazon.com/). It uses a **SPARQL query**, which allows rapidly querying and returning a list of more than 4,000 Cases. The difference relative to the _prior_ tutorial is that here you need to be able to write the SPARQL query. However, this extra work allows you to use **more advanced syntax** and also **returns metadata** which can be _directly used_ for additional processing.

## How could I get VCF files to pass to a tertiary analysis software?
The [**Get\_my\_VCFs.ipynb**] tutorial searches for _VCF_ files within a particular project OR within a particular tasks inside of a particular project. 

### Notes
1. _Extensive_ and _beautiful_ API documentation for the Seven Bridges Platform is available [here](http://docs.cancergenomicscloud.org/docs/the-cgc-api)
2. The **advanced-access** branch still has MUCH better tutorials.