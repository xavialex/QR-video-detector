# QR video detection

Every script of this project performs QR code detection for every frame recorded from a camera wired to a computer. It aims to see the diferences in performance of the actual solutions tested.

## Dependencies

If you're a conda user, you can create an environment from the ```environment.yml``` file using the Terminal or an Anaconda Prompt for the following steps:

1. Create the environment from the ```environment.yml``` file:

    ```conda env create -f environment.yml```
2. Activate the new environment:
    * Windows: ```activate qr-detector```
    * macOS and Linux: ```source activate qr-detector``` 

3. Verify that the new environment was installed correctly:

    ```conda list```
    
You can also clone the environment through the environment manager of Anaconda Navigator.

## Use

Simply launch any script with an available webcam wired to your computer to see how the algorithm works. Point it through one or more QR codes and see how accurately they predict its location

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
