#!/usr/bin/env python
 
'''
Uses SURF to match two images.
 
Based on the sample code from opencv:
  samples/python2/find_obj.py
 
USAGE
  find_obj.py <image1> <image2>
'''
 
import numpy
import cv2
 
import sys
 
###############################################################################
# Image Matching
###############################################################################
 
def match_images(img1, img2):
    """Given two images, returns the matches"""
    detector = cv2.SURF(400, 5, 5)
    matcher = cv2.BFMatcher(cv2.NORM_L2)
 
    kp1, desc1 = detector.detectAndCompute(img1, None)
    kp2, desc2 = detector.detectAndCompute(img2, None)
    print 'img1 - %d features, img2 - %d features' % (len(kp1), len(kp2))
 
    raw_matches = matcher.knnMatch(desc1, trainDescriptors = desc2, k = 2) #2
    kp_pairs = filter_matches(kp1, kp2, raw_matches)
    return kp_pairs
 
def filter_matches(kp1, kp2, matches, ratio = 0.75):
    mkp1, mkp2 = [], []
    for m in matches:
        if len(m) == 2 and m[0].distance < m[1].distance * ratio:
            m = m[0]
            mkp1.append( kp1[m.queryIdx] )
            mkp2.append( kp2[m.trainIdx] )
    kp_pairs = zip(mkp1, mkp2)
    return kp_pairs
    
    
###############################################################################
# Match Diplaying
###############################################################################
 
def explore_match(win, img1, img2, kp_pairs, status = None, H = None):
    
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]
    vis = numpy.zeros((max(h1, h2), w1+w2), numpy.uint8)
    vis[:h1, :w1] = img1
    vis[:h2, w1:w1+w2] = img2
    vis = cv2.cvtColor(vis, cv2.COLOR_GRAY2RGB)
 
    if H is not None:
        corners = numpy.float32([[0, 0], [w1, 0], [w1, h1], [0, h1]])
        corners = numpy.int32( cv2.perspectiveTransform(corners.reshape(1, -1, 2), H).reshape(-1, 2) + (w1, 0) )
        cv2.polylines(vis, [corners], True, (255, 255, 255))
 
    if status is None:
        status = numpy.ones(len(kp_pairs), numpy.bool_)
        
    p1 = numpy.int32([kpp[0].pt for kpp in kp_pairs])
    p2 = numpy.int32([kpp[1].pt for kpp in kp_pairs]) + (w1, 0)
 
    green = (0, 255, 0)
    red = (0, 0, 255)
    white = (255, 255, 255)
    kp_color = (51, 103, 236)
    
    for (x1, y1), (x2, y2), inlier in zip(p1, p2, status):
        if inlier:
            col = green
            cv2.circle(vis, (x1, y1), 2, col, -1)
            cv2.circle(vis, (x2, y2), 2, col, -1)
        else:
            col         = red
            r           = 2
            thickness   = 2
            lineType    = 8
            shift       = 0
            
            cv2.circle(vis, (x2-r, y2+r), 10, col, thickness, lineType, shift)
    
    vis0 = vis.copy()
    
# to print lines
#
#     for (x1, y1), (x2, y2), inlier in zip(p1, p2, status):
#         if inlier:
#             cv2.line(vis, (x1, y1), (x2, y2), green)
 
    cv2.imshow(win, vis)
 
def draw_matches(window_name, kp_pairs, img1, img2):
    """Draws the matches for """
    mkp1, mkp2 = zip(*kp_pairs)
    
    p1 = numpy.float32([kp.pt for kp in mkp1])
    p2 = numpy.float32([kp.pt for kp in mkp2])
    
    if len(kp_pairs) >= 4:
        H, status = cv2.findHomography(p1, p2, cv2.RANSAC, 5.0)
        print '%d / %d  inliers/matched' % (numpy.sum(status), len(status))
    else:
        H, status = None, None
        print '%d matches found, not enough for homography estimation' % len(p1)
    
    if len(p1):
        explore_match(window_name, img1, img2, kp_pairs, status, H)
        
    return numpy.sum(status) / len(status)
 
###############################################################################
# Test Main
###############################################################################
 
if __name__ == '__main__':

    fn1 = 'stormTrooper1.png'
    fn2 = 'stormTrooper2.png'
    
    fn3 = 'Capture.png'
    fn4 = 'Capture2.png'
 
    fn5 = 'Untitled1.png'
    fn6 = 'Untitled2.png'
 
    img1 = cv2.imread(fn6, 0)
    img2 = cv2.imread(fn6, 0)
    
    if img1 is None:
        print 'Failed to load fn1:', fn1
        sys.exit(1)
        
    if img2 is None:
        print 'Failed to load fn2:', fn2
        sys.exit(1)
 
    kp_pairs = match_images(img1, img2)
    
    if kp_pairs:
        print draw_matches('find_obj', kp_pairs, img1, img2)
        cv2.waitKey()
        cv2.destroyAllWindows()    
else:
        print "No matches found"