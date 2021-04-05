# UpCurve_DataExtraction
Project carried out with the Petroleum Division Collegiate Council for the UpCurve Energy company. Code to extract data from the universitylands site, plot figures for analysis in HEEDS Post, and create surrogate models with SMT from NASA

You'll find here ### files

HEEDSPost_Script.py is the function to open the software for data post processing HEEDS Post from Simcenter Simens. Ensure that the path point to the right data set. For more information about the HEEDS API visit https://www.redcedartech.com/

surrogated.py is the function to evaluate the surrogated model, you should change the path to the folder exported by the main function and also the parameters that you want to plot. We highly recommend do some exploration to ensure that the kriging model is good for the parameters to be evaluated. The tools for post processing as HEEDS could be helpful. For more information refer to: https://smt.readthedocs.io/en/latest/_src_docs/surrogate_models/krg.html 
