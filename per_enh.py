import cv2
import numpy as np
import PIL

def mouse_handler(event, x, y, flags, data):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(data['im'], (x, y), 3, (0, 0, 255), 5, 16);
        cv2.imshow("Image", data['im']);
        if len(data['points']) < 4:
            data['points'].append([x, y])
def get_four_points(im):
    data = {}
    data['im'] = im.copy()
    data['points'] = []
    cv2.imshow("Image", im)
    cv2.setMouseCallback("Image", mouse_handler, data)
    cv2.waitKey(0)
    points = np.vstack(data['points']).astype(float)
    return points


if __name__ == '__main__' :
    # Read in the image.  # Image Enhancement Functions
    path = "rF:\College\Semester_10\Vision\Project2\TestingImages"
    im_src = cv2.imread(path + "3.jpeg",0) # Remove 0 for coloured functions
    newImg = cv2.resize(im_src, (800, 800), fx=0.75, fy=0.75)
    equ = cv2.equalizeHist(newImg)
    blur_image = cv2.GaussianBlur(newImg, (7, 7), 0)
    edge_img = cv2.Canny(newImg, 100, 200)
    #denimage = cv2.fastNlMeansDenoisingColored(newImg, None, 10, 10, 5, 10)
    cv2.imshow("Equalized_Image", equ)
    cv2.imshow("Blurred", blur_image)
    cv2.imshow("Edge_Det_Image", edge_img)



    '''
    # Destination image
    rows = im_src.shape[0]
    cols = im_src.shape[1]
    size = (rows ,cols ,3)
    im_dst = np.zeros(size, np.uint8)
    pts_dst = np.array(
        [
            [0 ,0],
            [size[0] - 1, 0],
            [size[0] - 1, size[1] -1],
            [0, size[1] - 1]
        ], dtype=float
    )

    print
    

        Click on the four corners of the book -- top left first and

        bottom left last -- and then hit ENTER

    cv2.imshow("Image", im_src)
    pts_src = get_four_points(im_src);
    # Calculate the homography
    h, status = cv2.findHomography(pts_src, pts_dst)
    # Warp source image to destination
    im_dst = cv2.warpPerspective(im_src, h, size[0:2])
    # Show output
    cv2.imshow("Image", im_dst)
    '''
    cv2.waitKey(0)