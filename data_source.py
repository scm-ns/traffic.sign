"""
    This file will provide functions to lead the data set and provide it to the trainer
"""
import os
import skimage.data
import skimage.transform
import numpy as np
import matplotlib.pyplot as plt


def load_belgium_dataset(dataset_dir):
  
    """
    In the beligum case, a directory is created for each label. 
        With in each label, there are multiple images belonging to this label. 
        Plus there is a CSV file providing some information about their label, But it is redundant. We know label from the current directory
    """

    label_dirs = [f for f in os.listdir(dataset_dir)
                        if os.path.isdir(os.path.join(dataset_dir , f))]

    data_x = []
    data_y = []

    for d in label_dirs : 
        label_dir = os.path.join(dataset_dir , d)
        # get all the files in the folder correponding to a single directory , that is a label
        file_names = [os.path.join(label_dir , f)
                        for f in os.listdir(label_dir)
                            if f.endswith(".ppm")]

        # get the image from the file names and the get the label from the directory name
        for f in file_names : 
            data_x.append(skimage.data.imread(f))
            data_y.append(int(d))
    return data_x , data_y 

def display_imgs_labels(images, labels):

    labels_set = set(labels);

    plt.figure(figsize = (15,15))

    idx = 1 ;
    for label in labels_set : 
        img = images[labels.index(label)]
        plt.subplot(8 , 8 , idx)
        plt.axis('off')
        plt.title("Label {0} ({1})".format(label , labels.count(label)))
        idx += 1; 
        _ = plt.imshow(img)
    plt.show()


def dataset_info(images , limit = 5):
    for image in images[:limit]:
        print("shape: {0}, min: {1}, max: {2}".format(image.shape, image.min(), image.max()))


def load_belgium_train_set():
    current_dir = os.getcwd();
    train_data_dir = os.path.join(current_dir, "dataset/Training") 
    return load_belgium_dataset(train_data_dir);


def load_belgium_test_set():
    current_dir = os.getcwd();
    test_data_dir = os.path.join(current_dir, "dataset/Testing") 
    return load_belgium_dataset(test_data_dir);



"""
    Assumption : 
        There exists a dataset directory in the directory where this file is run and we will be able to find the images and lebels inside the dataset dir
"""
if __name__ == "__main__":

    current_dir = os.getcwd();

    train_data_dir = os.path.join(current_dir, "dataset/Training") 
    test_data_dir = os.path.join(current_dir , "dataset/Testing") 

    images , labels = load_belgium_dataset(train_data_dir)

    # Do a few tests on the images
    print("Labels : {0}\n Total # images : {1}\n ".format(len(set(labels)) , len(images)))


    display_imgs_labels(images , labels)
    


    # 32 x 32 images
    images32 = [skimage.transform.resize(img , (32 , 32))  
                        for img in images]

    display_imgs_labels(images32 , labels);


    dataset_info(images32) 

