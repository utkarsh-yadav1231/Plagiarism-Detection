print("Hello User, This is a Python Plagiarism Detection program")
print("This project detects plagiarized images.\n\n") #if not plagiarized then it prints the difference
import numpy as np									  # image which should not be black.
import cv2


image1 = cv2.imread("red200.jpg")
image2 = cv2.imread("red203.jpg")

difference = cv2.subtract(image1,image2)

res = not np.any(difference)
print("Result of Plagiarism Detection : ")

if res is True:
    print("These two are Same Images ")
else:
    print("\nThese two are Different images\n")
    cv2.imwrite("Resv1.jpg", difference)
    print("Check the root file for the Resulting image formed")
    print("which shows the difference between two source images input")
    print("\n")
print("Program ends here")
