# API Recipes for the Seven Bridges Platform (SBPLAT)
Our goals are: 

* Educate users about how the API works by using a friendly Python wrapper
* Provide re-usable blocks of API code to solve common problems

## How does the Seven Bridges Platform work?
An important first concept is how the Seven Bridges Platform (and CGC) works. A user has access to multiple **projects**, she may either be the owner of those projects or a member of someone else's project. Within each project, there is a collection of **files** and **apps**. The owner can combine a set of files, configuration inputs, and an app to generate a **task**. Once this task is complete, any **output files** will be put into
the project where the task was started.

![CGC Overview](images/CGC_overview-02.png)

## Recipes in this cookbook
 
Each Seven Bridges Platform component is accessible by the API. These recipes are _purposefully_ repetitive to highlight the logic of the API and hopefully help users understand some of the tools available to solve problems. The current _cookbook_ includes<sup>1</sup> the following recipes:

* Projects
  * list [projects\_listsAll.ipynb]
  * get details [projects\_detailOne.ipynb]
  * get members [projects\_membersOne.ipynb]
  * make new [projects\_makeNew.ipynb]
  * add members [projects\_addMembers.ipynb]
  
* Files
 * list (within a project) [files\_listAll.ipynb]
 * get details [files\_detailOne.ipynb]
 * copy Public Reference file [files\_copyFromMyProject.ipynb]
 * copy from another project [files\_copyFromPublicReference.ipynb]
 
* Apps
 * list [apps\_listAll.ipynb]
 * get details [apps\_detailOne.ipynb]
 * copy from Public Apps [apps\_copyFromPublicApps.ipynb]
 * copy from another project [apps\_copyFromMyProject.ipynb]
 * install (upload) from a Common Workflow Language JSON [apps\_installFromJSON.ipynb]
 
* Tasks
 * create and start [tasks\_create.ipynb]
 * monitor & get outputs [tasks\_monitorAndGetResults.ipynb]

* Volumes<sup>2</sup>
 * mount and write to volume [volumes\_writeToCloudStorage.ipynb]
 * mount and read from volume [volumes\_readFromCloudStorage.ipynb]
 
### Notes
<sup>1</sup> We are happy to add more recipes, please request what helps you most effectively get stuff done. Already in the queue are:

* [files\_upload_and_setMetadata.ipynb] Upload files with the API; set their metadata
* [files\_screenbyMetadata.ipynb] make a file list based on metadata - showcase blazing speed.
* [billing\_\*] we definity have neglected billing, sorry. 

<sup>2</sup> These recipes will be updated to use the sevenbridges-python library which now (version >= 0.4.0) supports Volumes API.