 <img src = "https://github.com/sbg/okAPI/blob/master/_images/SB_logo.jpg" width = "300"> 
# tutor me
We are happy to share a few _use-cases_  that have been useful for our customers. We are even happier to hear your **needs** so we can make things run more smoothly for you. 

These scripts include [USER INPUTS] for particular _workflows_; however, they are _extensively commented_ so they can be easily adapted to other tasks.

## How do I create and run a batch of tasks (over a _single-input_)? 
The [**batch\_o\_tasks\_standard.ipynb**] tutorial creates a project, copies WGS bam files from the [CCLE](https://igor.sbgenomics.com/u/sevenbridges/cancer-cell-line-encyclopedia-ccle/) project, uploads a workflow from a JSON, creates a batch of tasks over the _bam\_files_ input. If this batch of tasks passes _validation checks_, then the tasks will begin running.

## How do I create and run a batch of tasks (over a _multiple inputs_)? 
[**batch\_o\_tasks\_standard.ipynb**] is slightly more complex than the prior tutorial. Here, we create a project, copy WGS bam files from the [CCLE](https://igor.sbgenomics.com/u/sevenbridges/cancer-cell-line-encyclopedia-ccle/) project, uploads a workflow from a JSON, and work to organize the files into _normal_ and _tumor_ pairs. Then we use a for loop to create task for each pair of input files.

## How do I get started with RNA-seq?
The [**quickstartOpenData.ipynb**] tutorial creates an **open-data** project, add reference files and reference apps, create a task, and finally download the outputs. 

## How could I get VCF files to pass to a tertiary analysis software?
The [**Get\_my\_VCFs.ipynb**] tutorial searches for _VCF_ files within a particular project OR within a particular tasks inside of a particular project. 

### Notes
1. _Extensive_ and _beautiful_ API documentation for the Seven Bridges Platform is available [here](http://docs.sevenbridges.com/docs/the-api)