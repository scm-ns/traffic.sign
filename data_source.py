"""
    This file will provide functions to lead the data set and provide it to the trainer
"""
import os



def load_belgium_dataset(dataset_dir):
  
    """
    In the beligum case, a directory is created for each label. 
        With in each label, there are multiple images belonging to this label. 
        Plus there is a CSV file providing some information about their label, But it is redundant. We know label from the current directory
    """

    label_dirs = [f for f in os.listdir(dataset_dir)
                        if os.path.isdir(os.path.join(dataset_dir , f))]

    x = []
    y = []

    for d in label_dirs : 
        label_dir = os.path.join(dataset_dir , d)
        # get all the files in the folder correponding to a single directory , that is a label
        file_names = [os.path.join(label_dir , f)
                        for f in os.listdir(label_dir)
                            if f.endswith(".ppm")]

        # get the image from the file names and the get the label from the directory name
        for f in file_names : 
            x.append(skimage.data.imread(f))
            y.append(int(d))
    return images , labels


train_data_dir = (os.path("./data/BelgiumTSC/Training") 
test_data_dir = (os.path("./data/BelgiumTSC/Testing") 

load_belgium_dataset(train_data_dir)



