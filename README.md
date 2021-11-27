<center><h1>Tensorfood</h1></center>
This is an image classifier that categorises images as one of twelve Singaporean dishes:

1. chilli crab
2. curry puff
3. dim sum
4. ice kacang
5. kaya toast
6. nasi ayam
7. popiah
8. roti prata
9. sambal stingray
10. satay
11. tau huay
12. wanton noodle

## 1. Model architecture
Tensorfood is based on the MobileNetV2 architecture, with a custom output net comprising one dense layer of 128 nodes, followed by a softmax output layer with 12 nodes.   

The default settings is set to:
1. 13 Epoch 
2. learning rate of 0.0001.
3. dropout rate of 0.2

The model was trained with these default params.
1. rotation_range: 40
2. width_shift_range: 0.2
3. height_shift_range: 0.2
4. zoom_range: 0.5
5. horizontal_flip: True
6. fill_mode: nearest
7. validation_split:  0.2
8. batch_size: 9

## 2. Expected data format
Tensorfood expects raster mages in colour. Input files will be converted to 256*256 in RGB mode.

## 3. Training dataset
Tensorfood makes use of pre-trained weights in the MobileNetV2 architecture via transfer learning. This base architecture was originalyl trained on ImageNet. Additional training was performed on the custom output layers using ~900 images of the twelve Singaporean dishes.

## 4. Model performance
Tensorfood has a validation accuracy of 84%.


## 5. Model deployment
Tensorfood is deployed on a flask app where users can upload images via a HTML page.

Continuous integration: Committed updates to the source code in each branch are subject to unit tests to ensure that the necessary functionality is achieved. The updates can then be merged into the master branch.

Continuous deployment:
The updated and merged code is then pushed to servers for deployment. Clients will be able to interface with the most updated app.

<img src="https://www.edureka.co/blog/content/ver.1531719070/uploads/2018/07/Asset-33-1.png" alt="CI/CD pipeline" width="600"/>

Image from https://dzone.com/articles/learn-how-to-setup-a-cicd-pipeline-from-scratch


## To Run
Simply run src/app.py