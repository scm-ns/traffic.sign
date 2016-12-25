import data_source
import tensorflow as tf

"""
    Create a class which holds the graph with in it. Create a temlate that can be used without too much effort in differnt situations. 
    
    Create an abstract class in python
"""



def build_model(labels , images32):
    labels_np = np.array(labels)
    images32_np = np.array(images32)
    

    graph = tf.Graph()

    with graph.as_default():
        img_ph = tf.placeholder(tf.float32 , [None , 32 , 32 , 3])
        label_ph = tf.placeholder(tf.int32 , [None ])

        img_flat_op = tf.contrib.layers.flatten(img_ph)

        logits_op = tf.contrib.layers.fully_connected(img_flat , 62 , tf.nn.relu)

        predicted_label_op = tf.argmax(logits , 1)  # Not depended on the labels, so can be used for prediction



        loss_op = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits , label_ph))

        
        train_op = tf.train.AdamOptimizer(learning_rate = 0.001).minimize(loss)

        tf.initialize_all_variables();

    print("img_flat " , img_flat)
    print"logits " , logits)
    print"loss " , loss)
    print("predicted loss ", predicted_label)

    return graph , train , loss



def train():
    graph, train , loss  = build_model();
    sess = tf.Session(graph = graph)

    for i in range(100):
        _ , loss_val = sess.run([train,loss] , feed_dict = {img_ph :images32_np , label_ph: labels_np})


        if i % 10 == 0 : 
            print("Loss : " , loss_val)

    
def inference():
    sample_idx = random.sample(range(len(images32) + 10))
    sample_img = [images32[idx] for idx in sample_idx]
    sample_label = [labels[idx] for idx in sample_idx]

    predicted = session.run([predicted_label_op] , feed_dict = {img_ph : sample_img })
    return predicted ; 


def display_prediction_truth():
    # Create the figure
    fig = plt.figure((10,10)) 
    
    # Go thru each of the prediction and the labels and see if they are smae or differnt
    
    for i in range(len(sample_idx)):
        true_label  = sample_label[i];
        predicted_label = prediction[i];
        plt.subplot(5 , 2 , i + 1) 
        plt.axis('off')
        color = 'green' if true_label == predicted_label else 'red'














