# tutor me
We are happy to share a few _use-cases_  that have been useful for our customers. We are even happier to hear your **needs** so we can make things run more smoothly for you. 

These four scripts have been hard-coded in a few places depending on the _workflow_ used. However, they are _extensively commented_ so they can be easily adapted to other tasks.

## How do I get started with RNA-seq?
The [**quickstart.ipynb**] tutorial will run an API version of the GUI [quickstart](http://docs.cancergenomicscloud.org/docs/quickstart) that we _assume_ you've already completed. Note, this works with **TCGA-restricted** data

## How do I get started with _open-data_? 
The [**quickstartOpenData.ipynb**] tutorial creates an **open-data** project, add reference files and reference apps, create a task, and finally download the outputs. 

## How do I create a _batch_ of tasks and _dynamically_ choose a workflow for all my files?
The [**batch_SAMtoolsView.ipynb**] tutorial creates a **batch** of tasks for all appropriate files in a project. _Prerequisite_ a project must be configured in the GUI and data already added for processing. The apps must also be there. This will look for all unprocessed files within a project and create tasks for them.

## How do I _parallelize_ and _split_ a workflow?
The [**thyroid.py**] tutorial creates a a Multi-Input Single Output (MISO) tasks, here RNA Sequencing Differential expression via cufflinks. 
_Prerequisite_ a project must be configured in the GUI and data already added for processing. Project scans all available files, matches _tumor_ and _normal_ samples, adds the reference files, and starts the task.

## defs/apimethods.py
Common functions and objects for all of the files. Note, this will **eventually** be replaced by _new_, _cleaner_ Python wrapper. However, any code developed with this apimethods.py wrapper will **remain functional**.

### Notes
1. _Extensive_ and _beautiful_ API documentation for the CGC is available [here](http://docs.cancergenomicscloud.org/docs/the-cgc-api)
