import cv2


cap = cv2.VideoCapture("D:\project.mp4")


running=True
while running:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame=cv2.resize(frame,(450,1050))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blur, 0, 255)
       
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)

        cv2.imshow('edges', frame)
        
        k=cv2.waitKey(25)

        if k==ord("e") or k==27:
            running=False

cap.release()
cv2.destroyAllWindows()
