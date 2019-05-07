# QR video detection

Under construction.

## Dependencies

It's mandatory to download a model trained in the Tsinghua-Tencent 100K dataset.

If you're a conda user, you can create an environment from the ```environment.yml``` file using the Terminal or an Anaconda Prompt for the following steps:

1. Create the environment from the ```environment.yml``` file:

    ```conda env create -f environment.yml```
2. Activate the new environment:
    * Windows: ```activate traffic-signals-keras```
    * macOS and Linux: ```source activate traffic-signals-keras``` 

3. Verify that the new environment was installed correctly:

    ```conda list```
    
You can also clone the environment through the environment manager of Anaconda Navigator.

## Use

A *config.ini* file is given to easily change the behaviour of the application. These fields are.
* **source:** Supports several inputs: 
    > * Integer from 0 to *N* (where *N* is the number of cameras connected to your computer). Select one of your choice.
    > * String containing the path to a video (absolute or relative to the execution directory) or a wab stream.
* **resolution:** Set of three integers, expecting number of channels (3 for RGB), desired image's height and width (e.g. 3, 320, 320).
* **classes_of_interest:** List of labels (comma separated) from the dataset to be detected.
* **weights_path:** Path where the weights are stored (.hdf5 format).
* **nms_threshold:** (0.0 - 1.0) Overlapping factor for which the Non-Maxima-Supression will keep/remove duplicated detections.
* **detection_threshold:** (0.0 - 1.0) Minimum confidence to reach for a detection in order to be considered as such.

Once the *config.ini* file has been modified as desired, simply activate the virtual environment and execute the Python scripts.

### *python SSD300-Tsinghua100K-predictor-video.py*

The program will load a SSD300 model from the given weights, open the corresponfing video source and perform a traffic signal detection and recognition. At the end, a JSON message containing relevant information about the detections is outputed.

### instance_segmentation.py

This program will take the input image file, feed it into the Segmentation model and generate two windows with the original and the processed image. Use example:

```
python instance_segmentation.py -i images/my_image.jpg
```

By default, if not images are provided, this output'll be displayed.

![instance_segmented_image](segmented_images/scotty.jpg "instance_segmented_image")

### instance_segmentation_images.py

The script will process every *.jpg* image in the *images/* folder and save them in the *segmented_images/* folder.

### instance_segmentation_webcam.py

Here, the instance segmentation'll be applied to the frame captured by the first available webcam. Press the 'q' button in the generated floating windows or *Ctrl+C* to stop the execution. It's also possible to discriminate among the trained classes: when calling the ```run_inference_for_single_image``` function, pass as an optional argument a list containing the id's of the COCO classes you want to detect. The model will just display the detected instances of those classes.  
Note that this is a high demanding task in computational terms, even when using the most lightweight model available. Consider using GPU acceleration for this purposes.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [TF Object Detection](https://github.com/tensorflow/models/tree/master/research/object_detection)
