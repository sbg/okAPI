# ok, API
Code samples for using Seven Bridges' APIs.      
### Official [master branch]
To help people maximize the _extensibility_ and _automation_ capability of Seven Bridges products, we're happy to share example **API** code. These examples have been used to address common user _wants_ and _needs_. They are divided into **recipes** & **tutorials**. 

* **_"How do I do this one thing?"_** You want a **recipe**, which is a _modular_ example of common operations. 
* **_"How do I complete my entire analysis?"_** You want a **tutorial**, which may _combine multiple recipes_ to go from start to finish of an analysis. 

The recipes and tutorials in this repository cover the Seven Bridges Plaform and the Cancer Genomics Cloud.

To learn more about the Seven Bridges Platform or Cancer Genomics Cloud, see their documentation.
* The documentation for the Seven Bridges Platform is available at docs.sevenbridges.com/. In particular, see the the [API documentation](http://docs.sevenbridges.com/docs/the-api). 

* The documentation for the Cancer Genomics Cloud is available at docs.cancergenomicscloud.com/. In particular, see the the [API documentation](http://docs.cancergenomicscloud.org/docs/the-cgc-api). 

The _recipe_ and _tutorial_ folders in this repository are subdivided into **CGC** (the Cancer Genomics Cloud) and **SBPLAT** (the Seven Bridges Platform). This separation ensures we link to the appropriate docs. Switching environments is as easy as changing

```python
# [USER INPUT] specify platform {cgc, sbpla}
prof = 'cgc'
```

to 

```python
# [USER INPUT] specify platform {cgc, sbpla}
prof = 'sbpla'
```
in the second code cell of any recipe (Note some features are available on one platform but not the other). Each folder has it's own _readme_ files within each folder which details the scripts. Feedback and improvements are welcome. Good luck & have fun!

## Branches
Note there are two branches of this repository. You are on the **master** branch. We are currently _in transition_ and will populate this branch _as soon as possible_.

 * **master**: This was released April 2016 and uses _sevenbridges-python_, the **official** Python bindings supported by Seven Bridges. This branch includes most of the API functionality and is compatible with Python 2.6+ and 3.
 * **advanced\_access**: This was developed from January to May 2016 and uses _apimethods.py_. This is an **unofficial** branch where we may roll out new features. Currently there are more notebooks here. It is _only compatible_ with Python 2.7.


### Notes
0. We ask that you limit parallel tasks to **300** at a time. If you need to run more, that is **great**, but please get in touch with us so we don't _run out of cloud_.
1. This is compatible with **Python 2.6+ and Python 3**.
2. This is an **beta** and we are constantly working on improving our examples. Expect the awesomeness to continue.
3. Please share your _feedback_ on our [CGC forum](http://docs.cancergenomicscloud.org/discuss) or [SBG forum](http://docs.sevenbridges.com/discuss).
4. We are happy to recieve Pull Requests with your _improvements_.
