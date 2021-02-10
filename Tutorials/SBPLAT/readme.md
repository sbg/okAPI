 <img src = "https://github.com/sbg/okAPI/blob/master/_images/SB_logo.jpg" width = "300"> 
# tutor me
We are happy to share a few _use-cases_  that have been useful for our customers. We are even happier to hear your **needs** so we can make things run more smoothly for you. 

These scripts include [USER INPUTS] for particular _workflows_; however, they are _extensively commented_ so they can be easily adapted to other tasks.

## How do I get started with the platform?
The [**quickstart.ipynb**] tutorial creates a project, adds reference files and a workflow, creates a task, and finally shows the outputs. 

## How do I create and run a batch of tasks (over a _single-input_)? 
The [**batch\_o\_tasks\_standard.ipynb**] tutorial creates a project, copies WGS bam files from the [CCLE](https://igor.sbgenomics.com/u/sevenbridges/cancer-cell-line-encyclopedia-ccle/) project, uploads a workflow from a JSON, creates a batch of tasks over the _bam\_files_ input. If this batch of tasks passes _validation checks_, then the tasks will begin running.

## How do I provide out create and run tasks, wait for completion and then provide outputs to a second task?
The [**batch\_o\_tasks\_custom.ipynb**] tutorial shows an example of a simple task orchestration. The tutorial creates a project, copies WGS bam files from the [CCLE](https://igor.sbgenomics.com/u/sevenbridges/cancer-cell-line-encyclopedia-ccle/) project, uploads two workflows from a JSON, starts tasks with one workflow and monitors task execution. After all tasks in stage one are completed, this tutorial shows how to run the second workflow with the first workflow task outputs.

## How do I create and run a batch of tasks (over a _multiple inputs_)? 
[**Task automation with tumor-normal matched samples.ipynb**] is slightly more complex than the prior tutorial. Here, we create a project, copy WGS bam files from the [CCLE](https://igor.sbgenomics.com/u/sevenbridges/cancer-cell-line-encyclopedia-ccle/) project, uploads a workflow from a JSON, and work to organize the files into _normal_ and _tumor_ pairs. Then we use a for loop to create task for each pair of input files.

## How could I get VCF files to pass to a tertiary analysis software?
The [**Get\_my\_VCFs.ipynb**] tutorial searches for _VCF_ files within a particular project OR within a particular tasks inside of a particular project. 

### Notes
1. _Extensive_ and _beautiful_ API documentation for the Seven Bridges Platform is available [here](http://docs.sevenbridges.com/docs/the-api)