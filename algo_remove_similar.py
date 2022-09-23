import cv2
import numpy as np
import os

class rmduplicate:

    def __init__(self):
        count = 0

        while True:
            start = count + 1
            end = count + 11
            for i in range(start,end):

                try:
                    A = cv2.imread("/root/Documents/frames/imgN"+str(count)+".jpg")
                    print("current count is ",count)


                    try:

                        B = cv2.imread("/root/Documents/frames/imgN"+str(i)+".jpg")

                        height , width ,channel = A.shape

                        #
                        #B[0:width//2,:,:] = (0,0,255)

                        errorL2 = cv2.norm( A, B, cv2.NORM_L2 )
                        similarity = 1 - errorL2 / ( height * width )
                        print('Similarity = ',similarity)

                        if similarity >= 0.90:
                            print("match")
                            os.remove("/root/Documents/frames" +"/" +"imgN"+str(i)+".jpg")
                            print("deleting imgN"+str(i)+",jpg")
                            i+=1

                        elif cv2.waitKey(0) & 0xFF == ord("q"):
                                  break



                        else:
                            print("moving nextimgN"+str(i)+".jpg")
                            i+=1


                    except Exception as exception:
                        print("file not found",exception)
                        i+=1


                except Exception as e:
                    print("sorry",e)
                    count+=1

            count += 1

            if count >= 530:
                print("thanks for using programe")
                break


