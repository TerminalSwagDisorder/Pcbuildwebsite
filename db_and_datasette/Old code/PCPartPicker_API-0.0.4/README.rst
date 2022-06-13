PCPartPicker-API
================

Python3 API for pulling information from
`PcPartPicker <https://pcpartpicker.com>`__

Everything is pulled directly from there, no data is stored in this
package

What can this do?
~~~~~~~~~~~~~~~~~

Currently this library contains these features:

-  Select what region to use ("uk", "ca", etc.)

-  The ``lists`` class - for interacting with pages that are lists of
   products, as seen under the "browse by individual parts" tab on the
   PCPartPicker website (such as
   `products/cpu-cooler <https://pcpartpicker.com/products/cpu-cooler>`__).
   All product lists are supported except the ones under the
   ``SOFTWARE`` catergory, although those may be supported in the future

Installation
============

``pip install PCPartPicker_API``

See the PyPi page
`here <https://pypi.python.org/pypi/PCPartPicker-API>`__

Quickstart
==========

A quick demonstration of what this API can do

.. code:: python

    # Import pcpartpicker
    from PCPartPicker_API import pcpartpicker

    # Print the total amount of pages for CPUs
    print("Total CPU pages:", pcpartpicker.lists.total_pages("cpu"))

    # Pull info from page 1 of CPUs
    cpu_info = pcpartpicker.lists.get_list("cpu", 1)

    # Print the names and prices of all the CPUs on the page
    for cpu in cpu_info:
        print(cpu["name"], ":", cpu["price"])

    # Change the region to UK
    pcpartpicker.set_region("uk")
    print("\nRegion changed to UK")

    # Pull info from all CPU pages (this may take a minute)
    cpu_info_2 = pcpartpicker.lists.get_list("cpu")

    # Print the names and prices of all the CPUs on all pages
    # The prices will now be in GBP (£) instead of USD ($)
    for cpu in cpu_info_2:
        print(cpu["name"], ":", cpu["price"])

Documentation
=============

To start using the API, import ``pcpartpicker`` from
``PCPartPicker_API``

A list of ``part_type``\ s and their dictionary keys are available in
`*pages*\ data <https://github.com/thatguywiththatname/PcPartPicker-API/blob/master/PCPartPicker_API/_pages_data.py>`__

``pcpartpicker`` contains these (public) functions:

+-------------------------+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Function name           | Paramaters                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+=========================+=============================+====================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| ``set_region``          | ``region``                  | The region of PCPartPicker that this API uses. ``region`` must be one of: ``"au", "be", "ca", "de", "es", "fr", "in", "ie", "it", "nz", "uk", "us"``. The defualt is for this library is ``"us"``. As far as I can tell this only changes the currency                                                                                                                                                                                                                                                                                                                                                                                                                             |
+-------------------------+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``lists.get_list``      | ``part_type, page_num=0``   | This function returns a list of dictionaries. Each ``part_type`` will have different dictionary keys. To see what keys exist for each ``part_type``, you can look them up in `*pages*\ data <https://github.com/thatguywiththatname/PcPartPicker-API/blob/master/PCPartPicker_API/_pages_data.py>`__. Every dictionary will always contain the keys ``name``, ``price``, ``ratings`` and ``id`` (although they may not always have a value). ``page_num`` is set to ``0`` by default. ``0`` means it will scrape all pages and gather all the info it can. If you only want to get information from, for example, page 2 of the cpu results, you would set ``page_num`` to ``2``   |
+-------------------------+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``lists.total_pages``   | ``part_type``               | This function simply returns the amount of pages of results there are for a particular ``part_type``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+-------------------------+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

ToDo
====

-  support the ``SOFTWARE`` catergory in ``pcpartpicker.lists``

