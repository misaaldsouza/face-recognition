## Face Recognition
It is one of the many wonders that AI research has brought forward to the world. A technology capable of verifying a person from a digital image or a video frame from a video     source. Generally, they work by comparing selected facial attributes from given image with faces within a database (unknown folder). 

### Installation
___
Python provides a simple *face_recognition* command line tool that allows us to do face recognition on a folder of images. Before installing the library we need [dlib](https://www.youtube.com/watch?v=HqjcqpCNiZg) library pre-installed.


The following command will install the tool.
> ##### pip3 install face_recognition

The library works in three simple steps :

    • Identify a face in a given image
    • Identify specific features in the face
    • Compare it with the unknown images 
    • If found , it generates a face encoding vector of 128 values
-- based on this encoding, we can measure the similarity between two face images that can tell us if they belong to the same person.

### Screenshots 
_______
 
*findfaces.py*                                     
<img width="441" alt="Capture" src="https://user-images.githubusercontent.com/52240946/94113297-51284600-fe64-11ea-8528-cb4d10f75054.PNG">

*pullfaces.py* 

<img width="390" alt="capt" src="https://user-images.githubusercontent.com/52240946/94113771-0824c180-fe65-11ea-9700-baafd354e36b.PNG">

### Applications 
____
• Access Control

• Criminal Identification

• Healthcare

• Smarter Advertising

