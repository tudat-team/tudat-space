===========================
Custom environment settings
===========================

When working with a very specific model or application, it may happen that the model you want to use is not implemented in Tudat. If this is the case, we have the option for users to define 'custom' environment models. The use of these custom settings requires the user to define their own function for the specific environment model, as is shown below with a number of examples. Below, you can find a list of the currently supported custom environment models in Tudat:

* TODO: insert links to API

In each case, the user is required to define their own function, with a predefined set of inputs and outputs, which are different for each specific environment model (see API links above). 

For most environment models, the custom model can be fully defined by a standalone function , and can be fully defined by a free function (which may of course call other functions from tudat, other packages or your own code

Example custom model: Mars atmosphere
=====================================



Example custom model: Neptune ephemeris
=======================================
