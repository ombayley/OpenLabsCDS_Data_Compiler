# OpenLab CDS v2.7 Data Compiler

---
### Description

This is a very basic program to deal with the lack of 3D data exporting in OpenLabs CDS v2.7.
The program relies on an Analysis Processing Method (found in the lcms_sample_processing_template directory) which takes the raw data and exports chromatograms every 2 nm as separate files.
The processing script in this program then reads all of these files, interpolates missing data and exports the collated data as a single csv file. The compiler at the centre of the program can also be used to return a pandas.DataFrame containing the 3D DAD data.
interpolation of the missing data is performed to give the final 3D data with a resolution of 1 nm as this resolution can sometimes be required by some spectral analysis methods.

---
### Useage

This package can be run directly as an executable file, or from the gui.py script via commandline or a Python IDE.

If running the program from the python script, it is recomnded that you creating an isolated conda environment to avoid any problems with your installed Python packages.
For this purpose, the environment .yml file is provided which can be used to create the conda environment and to install the program dependencies.

    conda env create -f CDS_Data_Compiler_env.yml
    conda activate CDS_Data_Compiler

Once the environment is created and the dependancies installed, the **CDS_Data_Compiler** can be run from the command line using:
    
    python gui.py

Once the program is running, a small box should appear with ``Start``, ``Stop`` and ``Open`` buttons.
Select the desired directory to be monitored using the ``Open`` button. Once the directory is selected, press ``Start``.


Once a project directory is specified using the ``Open`` button, the program will check the specified directory (which contains the subdirectories that have the '**.sirslt**' tag). 
If the program finds any '**.sirslt**' directories that contain no '**3D_UV_Data.csv**' files but do contain the single wavelength CSV data in a '**.rsltcsv**' sub-directory, it will automatically generate the corresponding **3D_UV_Data.csv** file.


After the directory has been selected, the ``Start`` will become active. Once clicked, the program will actively monitor the project directory for changes and create the '**3D_UV_Data.csv**' files upon the creation of a '**.rsltcsv**' sub-directory.

---
### Updating the exectutable

The executable file is built from the python source code using pyinstaller. If the program needs to be run from the .exe but changes need to be made to the source ode, the python scripts can be edited and the desired exectuible remade using the commandline command: 
    
    pyinstaller --onefile -w --name OpenLabCDS_Data_Compiler gui.py

