tisserande.tracking.annotations
===============================

.. py:module:: tisserande.tracking.annotations

.. autoapi-nested-parse::

   Type annotations for marking function arguments with their provenance role.

   Usage::

       from tisserande.tracking.annotations import DataFile, Param

       @track
       def process(input_file: DataFile[str], threshold: Param[float]) -> DataFile[str]:
           ...



Attributes
----------

.. autoapisummary::

   tisserande.tracking.annotations.T
   tisserande.tracking.annotations.DataFile
   tisserande.tracking.annotations.ConfigFile
   tisserande.tracking.annotations.ConfigDict
   tisserande.tracking.annotations.Param
   tisserande.tracking.annotations.ArrayArg
   tisserande.tracking.annotations.ObjectArg
   tisserande.tracking.annotations.Untracked
   tisserande.tracking.annotations.ANNOTATION_MAP


Module Contents
---------------

.. py:data:: T

.. py:data:: DataFile

.. py:data:: ConfigFile

.. py:data:: ConfigDict

.. py:data:: Param

.. py:data:: ArrayArg

.. py:data:: ObjectArg

.. py:data:: Untracked

.. py:data:: ANNOTATION_MAP
   :type:  dict[str, str]

