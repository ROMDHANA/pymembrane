=========================================
pymembrane Documentation
=========================================

Welcome to the `pymembrane` documentation version |release|.
This module is a Python library for modeling, simulating, and optimizing spiral membrane-based processes.

This document will guide you through the configuration of available classes, the key inputs and outputs, and a complete usage example.

**Author**: Hedi Romdhana  
**Version**: |release|  
**Email**: hedi.romdhana@agroparistech.fr

Contents
========

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   Installation
   pymembrane Module
   Input and Output Arguments
   Usage Example

Installation
============

To install `pymembrane`, you can use `pip` from PyPI. Here is the command:

.. code-block:: bash

    pip install pymembrane

If you want to install the latest version directly from the GitHub repository, use the following command:

.. code-block:: bash

    pip install git+https://github.com/ROMDHANA/pymembrane.git

Make sure to have Python 3.7 or a later version.

pymembrane Module
=================

This module defines classes and functions to simulate spiral membrane filtration processes.

Classes
-------

- **res_membrane** : Class for storing and calculating membrane simulation results.
- **dwsim** : Interface to communicate with DWSIM for process simulation.
- **spiral_membrane** : Main class that simulates the spiral membrane process.

The classes are described below with detailed information about each attribute and method.

Input and Output Arguments
==========================

This section describes the inputs required by the spiral membrane model as well as the outputs generated during the simulation.

Inputs
------

The following table lists the key inputs required by the `spiral_membrane` class, along with their units and descriptions.

+-------------------+-----------+--------------------------+----------------------------------------------------+
| Parameter Name    | Type      | Units                    | Description                                        |
+===================+===========+==========================+====================================================+
| **dwsim**         | dict      | -                        | Configuration for DWSIM integration.               |
+-------------------+-----------+--------------------------+----------------------------------------------------+
| **k_correlation** | bool      | -                        | Whether to use k-correlation.                      |
+-------------------+-----------+--------------------------+----------------------------------------------------+
| **k_parameters**  | list      | -                        | Correlation parameters for mass transfer.          |
+-------------------+-----------+--------------------------+----------------------------------------------------+
| **l**             | float     | m                        | Membrane width.                                    |
+-------------------+-----------+--------------------------+----------------------------------------------------+
| **Δm**            | float     | m                        | Spacing or clearance.                              |
+-------------------+-----------+--------------------------+----------------------------------------------------+
| **Vin**           | float     | m3/h                     | Inlet volumetric flow rate.                        |
+-------------------+-----------+--------------------------+----------------------------------------------------+
| **T**             | float     | °C                       | Inlet temperature.                                 |
+-------------------+-----------+--------------------------+----------------------------------------------------+
| **Patm**          | float     | bar                      | Atmospheric pressure.                              |
+-------------------+-----------+--------------------------+----------------------------------------------------+
| **Pin**           | float     | bar                      | Inlet pressure.                                    |
+-------------------+-----------+--------------------------+----------------------------------------------------+
| **S**             | float     | m2                       | Membrane area.                                     |
+-------------------+-----------+--------------------------+----------------------------------------------------+
| **L**             | float     | m                        | Membrane length.                                   |
+-------------------+-----------+--------------------------+----------------------------------------------------+
| **Aw**            | float     | m/h/bar                  | Water permeability.                                |
+-------------------+-----------+--------------------------+----------------------------------------------------+
| **DP**            | float     | bar                      | Pressure loss across the membrane.                 |
+-------------------+-----------+--------------------------+----------------------------------------------------+
| **Cin**           | list      | mol/m3                   | Inlet solute concentrations.                       |
+-------------------+-----------+--------------------------+----------------------------------------------------+
| **solutes**       | list      | -                        | List of solutes in the feed stream.                |
+-------------------+-----------+--------------------------+----------------------------------------------------+
| **B**             | list      | m/h                      | Membrane mass transfer coefficients.               |
+-------------------+-----------+--------------------------+----------------------------------------------------+
| **k**             | list      | m/h                      | Boundary layer mass transfer coefficients.         |
+-------------------+-----------+--------------------------+----------------------------------------------------+

Outputs
-------

The following table describes the outputs of the spiral membrane model.

+-----------------------+-----------+------------------------+--------------------------------------------------------+
| Output Name           | Type      | Units                  | Description                                            |
+=======================+===========+========================+========================================================+
| **Vr_out**            | float     | m3/h                   | Retentate volumetric flow rate at the membrane outlet. |
+-----------------------+-----------+------------------------+--------------------------------------------------------+
| **Vp_out**            | float     | m3/h                   | Permeate volumetric flow rate at the membrane outlet.  |
+-----------------------+-----------+------------------------+--------------------------------------------------------+
| **Cr_out**            | ndarray   | mol/m3                 | Solute concentrations in the retentate at the outlet.  |
+-----------------------+-----------+------------------------+--------------------------------------------------------+
| **Cp_out**            | ndarray   | mol/m3                 | Solute concentrations in the permeate at the outlet.   |
+-----------------------+-----------+------------------------+--------------------------------------------------------+
| **net_balance**       | float     | m3/h                   | Net volumetric mass balance.                           |
+-----------------------+-----------+------------------------+--------------------------------------------------------+
| **solute_net_balance**| ndarray   | mol/h                  | Solute mass balance.                                   |
+-----------------------+-----------+------------------------+--------------------------------------------------------+
| **FRV_out**           | float     | -                      | Flow rate volume ratio at the membrane outlet.         |
+-----------------------+-----------+------------------------+--------------------------------------------------------+
| **T_out**             | ndarray   | mol/mol                | Transmission coefficient at the membrane outlet.       |
+-----------------------+-----------+------------------------+--------------------------------------------------------+
| **R_out**             | ndarray   | -                      | Rejection coefficient at the membrane outlet.          |
+-----------------------+-----------+------------------------+--------------------------------------------------------+

Usage Example
=============

Below is an example of how to use the `pymembrane` module to simulate the spiral membrane process.

1. **Import the module and define the inputs**:

   .. code-block:: python

       from pymembrane.membrane import spiral_membrane

       # Define the input parameters
       inputs = {
           'k_correlation': True,
           'l': 2.114,
           'Δm': 8.64e-4,
           'Vin': 1,
           'T': 20,
           'Patm': 1,
           'Pin': 10,
           'S': 100,
           'L': 1,
           'Aw': 5.3e-3,
           'DP': 1,
           'Cin': [0.1, 0.05],  # Solute concentrations
           'solutes': ['Solute1', 'Solute2'],
           'B': [0.001, 0.002],
           'k': [0.005, 0.006]
       }

       # Instantiate the spiral_membrane class
       membrane = spiral_membrane(**inputs)

2. **Run the calculation**:

   .. code-block:: python

       # Run the simulation
       membrane.calcul(solver_method='fsolve', taylor_terms=2, diffusion=False)

3. **Print the results**:

   .. code-block:: python

       # Access and print some of the results
       print("Retentate flow rate at outlet (Vr_out):", membrane.res.Vr_out)
       print("Permeate flow rate at outlet (Vp_out):", membrane.res.Vp_out)
       print("Transmission coefficient at outlet (T_out):", membrane.res.T_out)

Explanation of Results
----------------------

- **Vr_out**: Represents the volumetric flow rate of the retentate stream at the outlet of the membrane module.
- **Vp_out**: Represents the volumetric flow rate of the permeate stream.
- **T_out**: Represents the transmission coefficient of the solutes in the permeate at the outlet.

This simple example illustrates how to set up and run a spiral membrane simulation. You can adjust the inputs to model different scenarios and membrane configurations.

---

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
