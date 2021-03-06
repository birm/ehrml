ehrml
=====

Electronic Medical Record Machine Learning Utilities for using Models
with health data.

.. image:: https://badge.fury.io/py/ehrml.svg
    :target: https://badge.fury.io/py/ehrml

Configuration:
--------------

These utilities are very dependent on a particular configuration format.
In python, it is a list of dicts, where each dict represents
configuration for a particular field. The keys in this dict are as
follows:

+-----------------------------------+-----------------------------------+
| field                             | Description                       |
+===================================+===================================+
| index                             | The index to write the value (or  |
|                                   | in the case of any one-hot field, |
|                                   | to start writing values) in the   |
|                                   | numpy array.                      |
+-----------------------------------+-----------------------------------+
| missing_flag_index                | The index to write a one to if    |
|                                   | the data is missing               |
|                                   | (pre-imputation) in the numpy     |
|                                   | array. Do not set if no such      |
|                                   | missing data flag is desired for  |
|                                   | this field.                       |
+-----------------------------------+-----------------------------------+
| rwb_src                           | The value used to represent the   |
|                                   | value for all observation lists.  |
|                                   | Also, the field name associated   |
|                                   | with the “flat” data source,      |
|                                   | without any time suffix.          |
+-----------------------------------+-----------------------------------+
| api_parent                        | The key in the layered data which |
|                                   | contains relevant data for this   |
|                                   | field.                            |
+-----------------------------------+-----------------------------------+
| api_time_src                      | Which field in the layered data   |
|                                   | contains a reference to datetime  |
|                                   | for this observation.             |
+-----------------------------------+-----------------------------------+
| api_src                           | Regarding the layered data,       |
|                                   | either the direct access field    |
|                                   | for each item in the list under   |
|                                   | api_parent, or the desired value  |
|                                   | of api_by.                        |
+-----------------------------------+-----------------------------------+
| api_by                            | If a field in layered data is not |
|                                   | direct access, this is the field  |
|                                   | under api_parent which contains   |
|                                   | the name matching api_src. Do not |
|                                   | set for direct access values.     |
+-----------------------------------+-----------------------------------+
| api_from                          | If a field in layered data is not |
|                                   | direct access, this is the field  |
|                                   | under api_parent which contains   |
|                                   | the value. Do not set for direct  |
|                                   | access values.                    |
+-----------------------------------+-----------------------------------+
| transformation                    | The name of a transformation or   |
|                                   | encoding to be executed on this   |
|                                   | field.                            |
+-----------------------------------+-----------------------------------+
| one_hot_vals                      | An array of values corresponding  |
|                                   | to a one hot encoding for this    |
|                                   | field. Different for each         |
|                                   | encoding, unused for numerical    |
|                                   | transformations.                  |
+-----------------------------------+-----------------------------------+
| mean                              | For numeric transformations, the  |
|                                   | precomputed mean.                 |
+-----------------------------------+-----------------------------------+
| std                               | For numeric transformations, the  |
|                                   | precomputed standard deviation.   |
+-----------------------------------+-----------------------------------+
| min                               | For numeric transformations,      |
|                                   | replace any value lower than this |
|                                   | value with this value. Also used  |
|                                   | in some transformations.          |
+-----------------------------------+-----------------------------------+
| max                               | For numeric transformations,      |
|                                   | replace any value higher than     |
|                                   | this value with this value. Also  |
|                                   | used in some transformations.     |
+-----------------------------------+-----------------------------------+

Documentation
-------------

This tool uses a few different input and output structures in order to
facilitate computation and analysis. Descriptions of these formats,
along with descriptions of the methods and their inputs are in the
python docstrings for these methods.

Note
----

At this point, the utilities here may be very specific to a particular
kind of EHR and model.
