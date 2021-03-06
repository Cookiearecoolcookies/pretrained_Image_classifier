#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                                                           
# PROGRAMMER: Siva Maruti Ram Vadrevu Venkata 
# DATE CREATED: 23/02/2020
# REVISED DATE: 26/02/2020
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
import os

def get_pet_labels(image_dir: str) -> dict:
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    
    files = listdir(image_dir)

#     print("Files to remove : ", [file for file in files if file[0] is '.' ])
    
    # filter hidden file
    files = [ file for file in files if file[0] is not '.' ]
        
    results_dic = dict()
    
    for file in files:
        lable = file.lower() # lower case 
        lable = lable.split('.')[:-1] # remove .jpg extention
        lable = ".".join(lable) # concat string as we split above
        lable = lable.replace('_',' ') # replace _ 
        lable = ''.join([i for i in lable if not i.isdigit()]) # remove digits
        lable = lable.strip() # remove leading and trailing white spaces
        
        # check if file in dict
        if file not in results_dic:
            results_dic[file] = [lable]
        
    print(results_dic)
    
    return results_dic
